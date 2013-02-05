#include <iostream>
#include <vector>

using namespace std;

struct Food {
	int rate;
	int price;
};

int solve(const vector<Food>& menu, int limit, int n);

int main()
{
	int limit, n;
	while (cin >> limit >> n) {
		vector<Food> menu(n);
		for (int i = 0; i < n; ++i) {
			cin >> menu[i].price >> menu[i].rate;
		}
		cout << solve(menu, limit, n) << endl;
	}
	return 0;
}

int solve(const vector<Food>& menu, int limit, int n)
{
	vector< vector<int> > dp(n + 1, vector<int>(limit + 1));

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= limit; ++j) {
			dp[i][j] = dp[i - 1][j];
			if (j < menu[i - 1].price) {
				continue;
			}

			int value = dp[i - 1][j - menu[i - 1].price] + menu[i - 1].rate;
			if (dp[i][j] < value) {
				dp[i][j] = value;
			}
		}
	}
	return dp[n][limit];
}
