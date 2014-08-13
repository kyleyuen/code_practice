#include <iostream>
#include "../list.h"

using std::cout;
using std::endl;

int main()
{
	SingleLinkedList list;

	list.insert_node(1);
	list.insert_node(2);
	list.insert_node(3);
	list.insert_node(4);
	list.insert_node(5);

	cout << list.to_string() << endl;

	cout << "Find 1st to last node:" << endl;
	cout << list.get_nth_last_node(1)->get_value() << endl;

	cout << "Find 2nd to last node:" << endl;
	cout << list.get_nth_last_node(2)->get_value() << endl;

	cout << "Find 4th to last node:" << endl;
	cout << list.get_nth_last_node(4)->get_value() << endl;

	cout << "Find 5th to last node:" << endl;
	cout << list.get_nth_last_node(5)->get_value() << endl;

	return 0;
}