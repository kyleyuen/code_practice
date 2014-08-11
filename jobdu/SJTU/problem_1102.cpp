#include <iostream>
#include <vector>

using namespace std;

int solve(const vector< vector<int> >& matrix, int k);

int main()
{
	int n, m, k;
	while (cin >> n >> m >> k) {
		vector< vector<int> > matrix(n + 1, vector<int>(m + 1));
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) {
				cin >> matrix[i][j];
			}
		}
		cout << solve(matrix, k) << endl;
	}
	return 0;
}

int solve(const vector< vector<int> >& matrix, int k)
{
	int row = matrix.size() - 1;
	int column = matrix[0].size() - 1;

	vector< vector<int> > dp(row + 1, vector<int>(column + 1, 0));
	for (int i = 1; i <= row; ++i) {
		for (int j = 1; j <= column; ++j) {
			dp[i][j] = matrix[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1];
		}
	}

	int minimum = row * column + 1;
	for (int i = 1; i <= row; ++i) {
		for (int j = 1; j <= column; ++j) {
			for (int m = i; m <= row; ++m) {
				for (int n = j; n <= column; ++n) {
					int result = dp[m][n] - dp[i - 1][n] - dp[m][j - 1] + dp[i - 1][j - 1];
					if (result >= k) {
						int area = (m - i + 1) * (n - j + 1);
						if (minimum > area) {
							minimum = area;
						}
					}
				}
			}
		}
	}

	if (minimum > row * column) {
		return -1;
	}
	else {
		return minimum;
	}
}