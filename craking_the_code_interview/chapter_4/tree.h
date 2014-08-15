#ifndef TREE_H
#define TREE_H

#include <string>
#include <sstream>
#include <cstdlib>
#include <algorithm>

using std::string;
using std::stringstream;
using std::max;

class Node {
public:
	Node(int v=0): value(v), left_pointer(NULL), right_pointer(NULL) {}

	int get_value() { return value; }
	Node* get_left_pointer() { return left_pointer; }
	Node* get_right_pointer() { return right_pointer; }

	void set_value(int v) { value = v; }
	void set_left_pointer(Node* target) { left_pointer = target; }
	void set_right_pointer(Node* target) { right_pointer = target; }
	
private:
	int value;
	Node* left_pointer;
	Node* right_pointer;
};



class BinarySearchTree {
public:
	BinarySearchTree(): root(NULL) {}

	Node* get_root() { return root; }
	void insert_node(int value);

	string pre_order_traversal();
	string in_order_traversal();
	string post_order_traversal();

	bool is_balanced();
	int check_height(Node* current);

private:
	void set_root(Node* target) { root = target; }

	void pre_order(stringstream& ss, Node* current);
	void in_order(stringstream& ss, Node* current);
	void post_order(stringstream& ss, Node* current);

	Node* root;
};

#endif