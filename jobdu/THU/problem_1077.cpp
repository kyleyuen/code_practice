#include <iostream>
#include <vector>
#include <limits>

using namespace std;

long long solve(int n);

int main()
{
	int n;
	while (cin >> n) {
		cout << solve(n) << endl;
	}
	return 0;
}

long long solve(int n)
{
	vector<long long> numbers(n);
	vector<long long> sum(n);
	for (int i = 0; i < n; ++i) {
		cin >> numbers[i];
		sum[i] = numbers[i];
	}

	for (int i = 1; i < n; ++i) {
		if (sum[i] < sum[i - 1] + numbers[i]) {
			sum[i] = sum[i - 1] + numbers[i];
		}
	}

	long long result = numeric_limits<long long>::min();
	for (int i = 0; i < n; ++i) {
		if (result < sum[i]) {
			result = sum[i];
		}
	}
	return result;
}
