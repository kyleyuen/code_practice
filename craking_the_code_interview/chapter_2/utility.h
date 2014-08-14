#ifndef UTILITY_H
#define UTILITY_H

#include "list.h"

SingleLinkedList add_two_lists(SingleLinkedList left, SingleLinkedList right)
{
	SingleLinkedList result;
	Node* left_iterator = left.get_head();
	Node* right_iterator = right.get_head();

	int carry = 0;
	while (left_iterator != NULL && right_iterator != NULL) {
		int digit = left_iterator->get_value() + right_iterator->get_value() + carry;
		if (digit >= 10) {
			digit %= 10;
			carry = 1;
		}
		else {
			carry = 0;
		}

		result.insert_node(digit);
		left_iterator = left_iterator->get_next_pointer();
		right_iterator = right_iterator->get_next_pointer();
	}

	result.reverse_list();
	return result;
}


Node* verify_circular_list(SingleLinkedList list)
{
	Node* slower = list.get_head();
	Node* faster = list.get_head();

	// verify circular list by find collision
	while (slower != NULL && faster != NULL) {
		slower = slower->get_next_pointer();
		faster = faster->get_next_pointer();
		faster = faster->get_next_pointer();

		if (slower == faster) {
			slower = list.get_head();
			break;
		}
	}

	// find collision again
	while (slower != NULL && faster != NULL) {
		slower = slower->get_next_pointer();
		faster = faster->get_next_pointer();
		
		if (slower == faster) {
			return slower;
		}
	}
	return NULL;
}

#endif