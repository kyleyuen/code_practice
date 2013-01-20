#include <iostream>
#include <vector>

using namespace std;

bool solve(int n, int m);

int main()
{
	int n, m;
	while (cin >> n) {
		if (n == 0) {
			break;
		}
		cin >> m;
		cout << solve(n, m) << endl;
	}
}

bool solve(int n, int m)
{
	vector<int> nodes(n + 1);
	for (int i = 0; i < m; ++i) {
		int start, end;
		cin >> start >> end;
		++nodes[start];
		++nodes[end];
	}

	for (int i = 1; i <= n; ++i) {
		if (nodes[i] % 2 == 1) {
			return false;
		}
	}
	return true;
}
