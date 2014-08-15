#include "graph.h"

int DirectedGraph::ID_GENERATOR = 1;


void DirectedGraph::insert_node(int value, list<int> edges)
{
	Node new_node(ID_GENERATOR, value);
	for (list<int>::iterator iter = edges.begin(); iter != edges.end(); ++iter) {
		new_node.add_edge(*iter);
	}

	nodes.push_back(new_node);
	this->increase_size();
}


string DirectedGraph::depth_first_search()
{
	stringstream ss;

	vector<bool> status(this->get_size());
	for (vector<Node>::iterator iter = this->nodes.begin(); iter != this->nodes.end(); ++iter) {
		if (!status[iter->get_index()]) {
			dfs(ss, status, iter->get_index());
		}
	}

	return ss.str();
}


void DirectedGraph::dfs(stringstream& ss, vector<bool>& status, int current)
{
	status[current] = true;
	ss << (this->nodes)[current].get_value() << "\t";

	list<int> edges = (this->nodes)[current].get_edges();
	for (list<int>::iterator iter = edges.begin(); iter != edges.end(); ++iter) {
		if (status[*iter]) {
			continue;
		}

		dfs(ss, status, *iter);
	}
}


string DirectedGraph::breadth_first_search()
{

}


bool DirectedGraph::is_connected(int start, int end)
{

}