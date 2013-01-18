#include <iostream>
#include <vector>

using namespace std;

void solve(int m, int n);

int main()
{
	int m, n;
	while (cin >> m >> n) {
		solve(m, n);
	}
	return 0;
}

void solve(int m, int n)
{
	vector< vector<int> > matrix(m, vector<int>(n));
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> matrix[i][j];
		}
	}

	for (int i = 0; i < m; ++i) {
		int sum = matrix[i][0];
		int index = 0;
		int maximum = matrix[i][0];

		for (int j = 1; j < n; ++j) {
			if (maximum < matrix[i][j]) {
				maximum = matrix[i][j];
				index = j;
			}
			sum += matrix[i][j];
		}
		matrix[i][index] = sum;
	}

	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n - 1; ++j) {
			cout << matrix[i][j] << " ";
		}
		cout << matrix[i][n - 1] << endl;
	}
}

