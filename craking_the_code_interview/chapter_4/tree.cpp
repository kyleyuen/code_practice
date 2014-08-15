#include "tree.h"

#include <iostream>

using std::cout;

void BinarySearchTree::insert_node(int value)
{
	Node* current = this->get_root();
	if (current == NULL) {
		Node* new_node = new Node(value);
		this->set_root(new_node);
		return;
	}

	while (current != NULL) {
		if (value < current->get_value()) {
			if (current->get_left_pointer() == NULL) {
				Node* new_node = new Node(value);
				current->set_left_pointer(new_node);
				return;
			}
			current = current->get_left_pointer();
		}
		else {
			if (current->get_right_pointer() == NULL) {
				Node* new_node = new Node(value);
				current->set_right_pointer(new_node);
				return;	
			}
			current = current->get_right_pointer();
		}
	}
}


string BinarySearchTree::pre_order_traversal()
{
	stringstream ss;
	this->pre_order(ss, this->get_root());
	return ss.str();
}


void BinarySearchTree::pre_order(stringstream& ss, Node* current)
{
	if (current != NULL) {
		ss << current->get_value() << "\t";
		this->pre_order(ss, current->get_left_pointer());
		this->pre_order(ss, current->get_right_pointer());
	}
}


string BinarySearchTree::in_order_traversal()
{
	stringstream ss;
	this->in_order(ss, this->get_root());
	return ss.str();
}


void BinarySearchTree::in_order(stringstream& ss, Node* current)
{
	if (current != NULL) {
		this->in_order(ss, current->get_left_pointer());
		ss << current->get_value() << "\t";
		this->in_order(ss, current->get_right_pointer());
	}
}


string BinarySearchTree::post_order_traversal()
{
	stringstream ss;
	this->post_order(ss, this->get_root());
	return ss.str();
}


void BinarySearchTree::post_order(stringstream& ss, Node* current)
{
	if (current != NULL) {
		this->post_order(ss, current->get_left_pointer());
		this->post_order(ss, current->get_right_pointer());
		ss << current->get_value() << "\t";
	}
}


bool BinarySearchTree::is_balanced()
{
	int result = check_height(this->get_root());
	return (result != -1);
}


int BinarySearchTree::check_height(Node* current)
{
	if (current == NULL) {
		return 0;
	}

	// check left node
	int left_height = check_height(current->get_left_pointer());
	if (left_height == -1) {
		return -1;
	}

	// check right node
	int right_height = check_height(current->get_right_pointer());
	if (right_height == - 1) {
		return -1;
	}

	// verify current node is balanced or not
	int height_diff = abs(left_height - right_height);
	if (height_diff > 1) {
		return -1;
	}
	else {
		return max(left_height, right_height) + 1;
	}
}