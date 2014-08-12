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

	SingleLinkedList(): head(NULL) {}

	Node* get_head() { return head; }

	void insert_node(int value);
	void delete_node(Node* target);

	void remove_duplicate_node();

	string to_string();
private:

	void set_head(Node* p) { this->head = p; }

	Node* head;
};

#endif