#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve(int n, int m);

int main()
{
	int n, m;
	while (cin >> n >> m) {
		if (n == 0 && m == 0) {
			break;
		}
		solve(n, m);
	}
	return 0;
}

void solve(int n, int m)
{
	vector<int> people(n);
	for (int i = 0; i < n; ++i) {
		cin >> people[i];
	}
	sort(people.begin(), people.end());

	int counter = 0;
	bool flag = false;
	for (vector<int>::reverse_iterator iter = people.rbegin(); iter != people.rend(); ++iter) {
		++counter;
		if (counter > m) {
			break;
		}

		if (flag) {
			cout << " ";
		}
		flag = true;

		cout << *iter;
	}
	cout << endl;
}