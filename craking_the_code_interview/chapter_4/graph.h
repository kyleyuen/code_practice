#ifndef GRAPH_H
#define GRAPH_H

#include <list>
#include <vector>
#include <stack>
#include <deque>
#include <string>
#include <sstream>

using std::list;
using std::vector;
using std::stack;
using std::deque;
using std::string;
using std::stringstream;

class Node {
public:
	Node(int i, int v=0): index(i), value(v) {}

	int get_index() { return index; }
	int get_value() { return value; }
	list<int>& get_edges() { return edges; }

	void set_index(int i) { index = i; }
	void set_value(int v) { value = v; }
	void add_edge(int e) { edges.push_back(e); }

private:
	int index;
	int value;
	list<int> edges;
};



class DirectedGraph {
public:
	DirectedGraph(): size(0) { nodes.push_back(Node(0)); }

	int get_size() { return size; }
	vector<Node>& get_nodes() { return nodes; }
	Node& get_node_by_index(int index) { return nodes[index]; }

	void insert_node(int value, list<int> edges);
	string depth_first_search(int start=1);
	string breadth_first_search(int start=1);

	bool is_connected(int start, int end);

private:
	static void increase_id_generator() { ++ID_GENERATOR; }
	static void decrease_id_generator() { --ID_GENERATOR; }
	
	void increase_size() { ++size; }
	void decrease_size() { --size; }
	void dfs(stringstream& ss, vector<bool>& status, int current);
	bool search_path(vector<bool>& status, int current, int end);

	int size;
	vector<Node> nodes;

	static int ID_GENERATOR;
};

#endif