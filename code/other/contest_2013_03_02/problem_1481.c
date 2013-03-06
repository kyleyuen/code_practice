#include <stdio.h>
#include <string.h>

#define MAX_NODES 100

/* use adjacent matrix to represent tree */
int tree[MAX_NODES][MAX_NODES];
int tran[MAX_NODES];

int tran_index(int tag, int* pn);
int solve(int tree[MAX_NODES][MAX_NODES], int n);
int dfs(int tree[MAX_NODES][MAX_NODES], int n, int node, int state[MAX_NODES]);

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
			tree[start][end] = 1;
		} while (scanf("%d %d", &start, &end) != EOF);

		int result = solve(tree, index);
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
	++*pn;
	return n;
}

int solve(int tree[MAX_NODES][MAX_NODES], int n)
{
    if (n == 0) {
        return 1;
    }

	int state[MAX_NODES];
	memset(state, 1, sizeof(state));

    int i, j;
	for (i = 0; i < n; ++i) {
		for (j = 0; j < n; ++j) {
			if (tree[i][j] == 1) {
				state[j] = 0;
			}
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
		if (state[i] == 1) {
			flag = 0;
			break;
		}
	}
	return flag;
}

int dfs(int tree[MAX_NODES][MAX_NODES], int n, int node, int state[MAX_NODES])
{
	state[node] = 0;
	int i;
	for (i = 0; i < n; ++i) {
	    if (tree[node][i] == 0) {
            continue;
        }
		if (state[i] == 0) {
			return 0;
		}
        if (dfs(tree, n, i, state) == 0) {
        	return 0;
        }
	}
	return 1;
}
