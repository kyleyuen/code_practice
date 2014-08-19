#include "graph.h"
#include <iostream>

using std::cout;

int DirectedGraph::ID_GENERATOR = 0;

void DirectedGraph::insert_node(int value, list<int> edges)
{
	increase_id_generator();
	Node new_node(ID_GENERATOR, value);
	for (list<int>::iterator iter = edges.begin(); iter != edges.end(); ++iter) {
		new_node.add_edge(*iter);
	}

	this->get_nodes().push_back(new_node);
	this->increase_size();
}


string DirectedGraph::depth_first_search(int start)
{
	stringstream ss;

	vector<bool> status(this->get_size());
	this->dfs(ss, status, start);

	return ss.str();
}


void DirectedGraph::dfs(stringstream& ss, vector<bool>& status, int current)
{
	status[current] = true;
	ss << current << "\t";

	list<int> edges = this->get_node_by_index(current).get_edges();
	for (list<int>::iterator iter = edges.begin(); iter != edges.end(); ++iter) {
		if (!status[*iter]) {
			this->dfs(ss, status, *iter);
		}
	}
}


string DirectedGraph::breadth_first_search(int start)
{
	stringstream ss;

	vector<bool> status(this->get_size());
	deque<int> queue;
	
	queue.push_back(start);
	status[start] = true;
	while (!queue.empty()) {
		int current = queue.front();
		queue.pop_front();
		ss << current << "\t";

		list<int> edges = this->get_node_by_index(current).get_edges();
		for (list<int>::iterator iter = edges.begin(); iter != edges.end(); ++iter) {
			if (!status[*iter]) {
				queue.push_back(*iter);
				status[*iter] = true;
			}
		}
	}

	return ss.str();
}


bool DirectedGraph::is_connected(int start, int end)
{
	vector<bool> status(this->get_size());
	bool result = this->search_path(status, start, end);
	return result;
}


bool DirectedGraph::search_path(vector<bool>& status, int current, int end)
{
	status[current] = true;

	list<int> edges = this->get_node_by_index(current).get_edges();
	for (list<int>::iterator iter = edges.begin(); iter != edges.end(); ++iter) {
		if (*iter == end) {
			return true;
		}

		if (!status[*iter]) {
			if (this->search_path(status, *iter, end)) {
				return true;
			}
		}
	}
	return false;
}