#include <iostream>
#include "../list.h"

using std::cout;
using std::endl;

int main()
{
	SingleLinkedList list;

	list.insert_node(5);
	list.insert_node(4);
	list.insert_node(3);
	list.insert_node(2);
	list.insert_node(1);
	list.insert_node(1);
	list.insert_node(2);
	list.insert_node(3);
	list.insert_node(4);
	list.insert_node(5);
	list.insert_node(5);
	list.insert_node(4);
	list.insert_node(3);
	list.insert_node(2);
	list.insert_node(1);

	cout << "Before remove duplicate node:" << endl;
	cout << list.to_string() << endl;

	cout << "After remove duplicate node:" << endl;
	list.remove_duplicate_node();
	cout << list.to_string() << endl;
	return 0;
}