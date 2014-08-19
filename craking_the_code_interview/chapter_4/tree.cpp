#include "tree.h"

#include <iostream>

using std::cout;

Node* BinarySearchTree::insert_node(int value)
{
	Node* current = this->get_root();
	if (current == NULL) {
		Node* new_node = new Node(value);
		this->set_root(new_node);
		return NULL;
	}

	while (current != NULL) {
		if (value < current->get_value()) {
			if (current->get_left_pointer() == NULL) {
				Node* new_node = new Node(value);
				current->set_left_pointer(new_node);
				return new_node;
			}
			current = current->get_left_pointer();
		}
		else {
			if (current->get_right_pointer() == NULL) {
				Node* new_node = new Node(value);
				current->set_right_pointer(new_node);
				return new_node;
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


void BinarySearchTree::create_minimal_height_tree(const vector<int>& array)
{
	this->create_tree_from_vector(array, 0, array.size()-1);
}


Node* BinarySearchTree::create_tree_from_vector(const vector<int>& array, int start, int end)
{
	if (start > end) {
		return NULL;
	}

	int middle = (start+end) / 2;
	Node* new_node = new Node(array[middle]);
	if (this->get_root() == NULL) {
		this->set_root(new_node);
	}

	Node* left_leaf = this->create_tree_from_vector(array, start, middle-1);
	Node* right_leaf = this->create_tree_from_vector(array, middle+1, end);
	new_node->set_left_pointer(left_leaf);
	new_node->set_right_pointer(right_leaf);

	return new_node;
}