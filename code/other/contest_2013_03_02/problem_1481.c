#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_NODES 10000

struct Node {
    int value;
    struct Node* next;
    struct Node* previous;
};

typedef struct Node Node;
/* create list, return a pointer of this list's head */
Node* createList();
/* return the length of list */
int length(Node* list);
/* insert a value into list in specific position */
int insert(Node* list, int position, int value);
/* push value into list's back */
int pushBackList(Node* list, int value);
/* destroy specific list */
void destroyList(Node* list);


Node* tree[MAX_NODES];
int tran[MAX_NODES];

int tran_index(int tag, int* pn);
int solve(Node* tree[MAX_NODES], int n);
int dfs(Node* tree[MAX_NODES], int n, int node, int state[MAX_NODES]);

int main()
{
	int start, end;
	int counter = 0;
	while (scanf("%d %d", &start, &end) != EOF) {
		if (start == -1 && end == -1) {
			break;
		}

		/* clean up array */
		memset(tree, 0, sizeof(tree));
		memset(tran, -1, sizeof(tran));

		int index = 0;
		do {
			if (start == 0 && end == 0) {
				break;
			}

			start = tran_index(start, &index);
			end = tran_index(end, &index);
			pushBackList(tree[start], end);
		} while (scanf("%d %d", &start, &end) != EOF);

		int result = solve(tree, index);
		int i;
		for (i = 0; i < index; ++i) {
			destroyList(tree[i]);
		}

		++counter;
		if (result) {
			printf("Case %d is a tree.\n", counter);
		}
		else {
		    printf("Case %d is not a tree.\n", counter);
		}
	}
	return 0;
}

int tran_index(int tag, int* pn)
{
	int i;
	int n = *pn;
	for (i = 0; i < n; ++i) {
		if (tag == tran[i]) {
			return i;
		}
	}

	tran[*pn] = tag;
	tree[*pn] = createList();
	++*pn;
	return n;
}

int solve(Node* tree[MAX_NODES], int n)
{
    if (n == 0) {
        return 1;
    }

	int state[MAX_NODES];
	memset(state, 1, sizeof(state));

    int i;
	for (i = 0; i < n; ++i) {
	    Node* indicator = tree[i]->next;
        while (indicator != tree[i]) {
            state[indicator->value] = 0;
            indicator = indicator->next;
        }
	}

	int root = -1;
	for (i = 0; i < n; ++i) {
		if (state[i] != 0) {
			root = i;
			break;
		}
	}
	if (root == -1) {
        return 0;
	}

	memset(state, 1, sizeof(state));
	if (dfs(tree, n, root, state) == 0) {
		return 0;
	}

	int flag = 1;
	for (i = 0; i < n; ++i) {
		if (state[i] != 0) {
			flag = 0;
			break;
		}
	}
	return flag;
}

int dfs(Node* tree[MAX_NODES], int n, int node, int state[MAX_NODES])
{
	state[node] = 0;
	Node* indicator = tree[node]->next;
    while (indicator != tree[node]) {
    	if (state[indicator->value] == 0) {
    		return 0;
    	}
    	if (dfs(tree, n, indicator->value, state) == 0) {
        	return 0;
        }
        indicator = indicator->next;
    }
	return 1;
}

/* create list, return a pointer of this list's head */
Node* createList()
{
    Node* result = NULL;
    while (result == NULL) {
        result = (Node *)malloc(sizeof(Node));
    }

    result->next = result;
    result->previous = result;
    return result;
}

/* return the length of list */
int length(Node* list)
{
    int result = 0;
    Node* indicator = list->next;
    while (indicator != list) {
        ++result;
        indicator = indicator->next;
    }
    return result;
}

/* insert a value into list in specific position */
int insert(Node* list, int position, int value)
{
    if (position > length(list)) {
        printf("no element exist in %dth position\n", position);
        return -1;
    }

    Node* indicator = list;
    while (position > 0) {
        indicator = indicator->next;
        --position;
    }

    Node* target = NULL;
    while (target == NULL) {
        target = (Node *)malloc(sizeof(Node));
    }

    /* set up inserted node's value */
    target->previous = indicator;
    target->next = indicator->next;
    target->value = value;

    /* upgrade node's pointer */
    indicator->next->previous = target;
    indicator->next = target;
    return 1;
}

/* push value into list's back */
int pushBackList(Node* list, int value)
{
    return insert(list, length(list), value);
}

/* destroy specific list */
void destroyList(Node* list)
{
    Node* indicator = list->next;
    while (indicator != list) {
        Node* temp = indicator;
        indicator = indicator->next;
        free(temp);
    }
    free(list);
}
