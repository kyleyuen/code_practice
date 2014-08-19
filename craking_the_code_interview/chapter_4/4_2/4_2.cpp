#include <iostream>
#include "../graph.h"

using std::cout;
using std::endl;

int main()
{
	DirectedGraph graph;

	list<int> a;
	a.push_back(3);
	a.push_back(2);
	graph.insert_node(1, a);

	list<int> b;
	b.push_back(1);
	graph.insert_node(2, b);

	list<int> c;
	c.push_back(2);
	graph.insert_node(3, c);
	
	cout << graph.breadth_first_search() << endl;

	return 0;
}