#include "list.h"

void SingleLinkedList::insert_node(int value) {
	Node* new_node = new Node(value);

	new_node->set_next_pointer(this->get_head());
	this->set_head(new_node);
}


void SingleLinkedList::delete_node(Node* target) {
	Node* iterator = this->get_head();
	while (iterator != NULL) {
		if (iterator->get_next_pointer() == target) {
			break;
		}
		iterator = iterator->get_next_pointer();
	}

	iterator->set_next_pointer(target->get_next_pointer());
	delete target;
}


void SingleLinkedList::remove_duplicate_node() {
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


string SingleLinkedList::to_string() {
	stringstream result;

	Node* iterator = this->get_head();
	while (iterator != NULL) {
		result << iterator->get_value() << "\t";
		iterator = iterator->get_next_pointer();
	}

	return result.str();
}