#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

bool solve(vector< list<int> >& tree);
void dfs(vector< list<int> >& tree, int node, vector<bool>& state);

int main()
{
	int start, end;
	int counter = 0;
	while (cin >> start >> end) {
		if (start == -1 && end == -1) {
			break;
		}

		int index = 0;
		map<int, int > tran;
		vector< list<int> > tree;

		do {
			if (start == 0 && end == 0) {
				break;
			}

			if (tran.find(start) == tran.end()) {
				tran[start] = index;
				++index;
				tree.push_back(list<int>());
			}
			if (tran.find(end) == tran.end()) {
				tran[end] = index;
				++index;
				tree.push_back(list<int>());
			}

			start = tran[start];
			end = tran[end];
			tree[start].push_back(end);
		} while (cin >> start >> end);

		bool result = solve(tree);
		++counter;
		if (result) {
			cout << "Case " << counter << " is a tree." << endl;
		}
		else {
			cout << "Case " << counter << " is not a tree." << endl;
		}
	}
	return 0;
}

bool solve(vector< list<int> >& tree)
{
    if (tree.size() == 0) {
        return true;
    }

	vector<bool> state(tree.size(), true);
	for (int i = 0; i < tree.size(); ++i) {
		for (list<int>::iterator iter = tree[i].begin(); iter != tree[i].end(); ++iter) {
			state[*iter] = false;
		}
	}

	int root = -1;
	for (int i = 0; i < state.size(); ++i) {
		if (state[i]) {
			root = i;
			break;
		}
	}
	if (root == -1) {
        return false;
	}

	for (int i = 0; i < state.size(); ++i) {
		state[i] = true;
	}
	dfs(tree, root, state);

	bool flag = true;
	for (int i = 0; i < state.size(); ++i) {
		if (state[i]) {
			flag = false;
			break;
		}
	}
	return flag;
}

void dfs(vector< list<int> >& tree, int node, vector<bool>& state)
{
	state[node] = false;
	for (list<int>::iterator iter = tree[node].begin(); iter != tree[node].end(); ++iter) {
		if (!state[*iter]) {
			return;
		}
		dfs(tree, *iter, state);
	}
}
