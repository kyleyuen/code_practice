#ifndef LIST_H
#define LIST_H

#include <sstream>
#include <string>

using std::stringstream;
using std::string;

class Node {
public:

	Node(int v = 0): value(v), next(NULL) {}

	int get_value() { return value; }
	void set_value(int v) { value = v; }

	void set_next_pointer(Node* p) { next = p; }
	Node* get_next_pointer() { return next; }
private:

	int value;
	Node* next;
};



class SingleLinkedList {
public:

	SingleLinkedList(): head(NULL), size(0) {}

	Node* get_head() { return head; }
	int get_size() { return size; }
	Node* get_nth_node(int n);

	void insert_node(int value);
	void delete_node(Node* target);
	void reverse_list();

	void remove_duplicate_node();
	Node* get_nth_last_node(int n);
	void delete_node_in_the_middle(Node* target);

	string to_string();
private:

	void set_head(Node* p) { this->head = p; }
	void increase_size() { ++size; }
	void decrease_size() { --size; }

	Node* head;
	int size;
};

#endif