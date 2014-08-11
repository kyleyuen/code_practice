#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Party {
	int happiness;
	int period;
	int endTime;
};

bool compare(const Party& lhs, const Party& rhs)
{
	return lhs.endTime < rhs.endTime;
}

int solve(vector<Party>& parties);

int main()
{
	int n;
	while (cin >> n) {
		if (n < 0) {
			break;
		}

		vector<Party> parties(n);
		for (int i = 0; i < n; ++i) {
			cin >> parties[i].happiness;
			cin >> parties[i].period;
			cin >> parties[i].endTime;
		}
		cout << solve(parties) << endl;
	}
	return 0;
}

int solve(vector<Party>& parties)
{
	sort(parties.begin(), parties.end(), compare);

	int endTime = parties[parties.size() - 1].endTime;
	int n = parties.size();
	vector< vector<int> > dp(n + 1, vector<int>(endTime + 1, 0));

	for (int i = 1; i <= n; ++i) {
  		for (int j = 0; j <= endTime; ++j) {
  		    dp[i][j] = dp[i - 1][j];
 			if ((j < parties[i - 1].period) || (j > parties[i - 1].endTime)) {
				continue;
			}

 			int benifit = dp[i - 1][j - parties[i - 1].period] + parties[i - 1].happiness;
			if (dp[i][j] < benifit) {
				dp[i][j] = benifit;
			}
		}
	}

	int max = 0;
	for (int j = 0; j <= endTime; ++j) {
        if (max < dp[n][j]) {
            max = dp[n][j];
        }
	}
	return max;
}
