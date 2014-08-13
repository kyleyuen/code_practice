#include "list.h"
#include <iostream>
using std::cout;


Node* SingleLinkedList::get_nth_node(int n)
{
	Node* iterator = this->get_head();
	for (int i = 0; i < n; ++i) {
		if (iterator == NULL) {
			return NULL;
		}
		iterator = iterator->get_next_pointer();
	}
	return iterator;
}


void SingleLinkedList::insert_node(int value)
{
	Node* new_node = new Node(value);

	new_node->set_next_pointer(this->get_head());
	this->set_head(new_node);
	this->increase_size();
}


void SingleLinkedList::delete_node(Node* target)
{
	Node* iterator = this->get_head();
	while (iterator != NULL) {
		if (iterator->get_next_pointer() == target) {
			break;
		}
		iterator = iterator->get_next_pointer();
	}

	iterator->set_next_pointer(target->get_next_pointer());
	delete target;
	this->decrease_size();
}


void SingleLinkedList::reverse_list()
{
	if (this->get_size() == 0) {
		return;
	}

	Node* previous = this->get_head();
	Node* current = previous->get_next_pointer();
	previous->set_next_pointer(NULL);

	while (current != NULL) {
		Node* temp = current->get_next_pointer();
		current->set_next_pointer(previous);
		previous = current;
		current = temp;
	}
	this->set_head(previous);
}


void SingleLinkedList::remove_duplicate_node()
{
	Node* iterator = this->get_head();
	while (iterator != NULL) {
		Node* temp = iterator->get_next_pointer();
		while (temp != NULL) {
			if (temp->get_value() == iterator->get_value()) {
				Node* target = temp;
				temp = temp->get_next_pointer();
				this->delete_node(target);
			} else {
				temp = temp->get_next_pointer();
			}

		}
		iterator = iterator->get_next_pointer();
	}
}


Node* SingleLinkedList::get_nth_last_node(int n)
{
	Node* target = this->get_head();
	Node* pioneer = this->get_nth_node(n);
	if (pioneer == NULL) {
		return target;
	}

	// move both pointers
	while (pioneer->get_next_pointer() != NULL) {
		pioneer = pioneer->get_next_pointer();
		target = target->get_next_pointer();
	}
	return target;
}


void SingleLinkedList::delete_node_in_the_middle(Node* target)
{
	// verify that node is in the middle of the list
	if (target == this->get_head()) {
		return;
	}
	if (target->get_next_pointer() == NULL) {
		return;
	}

	Node* temp = target->get_next_pointer();
	target->set_value(temp->get_value());
	target->set_next_pointer(temp->get_next_pointer());

	delete temp;
	this->decrease_size();
}


string SingleLinkedList::to_string()
{
	stringstream result;

	Node* iterator = this->get_head();
	while (iterator != NULL) {
		result << iterator->get_value() << "\t";
		iterator = iterator->get_next_pointer();
	}

	return result.str();
}