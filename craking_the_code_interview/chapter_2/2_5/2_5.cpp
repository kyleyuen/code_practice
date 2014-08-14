#include <iostream>
#include "../list.h"
#include "../utility.h"

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

	cout << "List Elements:" << endl;
	cout << list.to_string() << endl;

	Node* source = list.get_nth_node(4);
	Node* target = list.get_nth_node(2);
	source->set_next_pointer(target);
	cout << source->get_value() << "\t" << target->get_value() << endl;
	
	cout << "verify circular list:" << endl;
	cout << verify_circular_list(list)->get_value() << endl;

	return 0;
}