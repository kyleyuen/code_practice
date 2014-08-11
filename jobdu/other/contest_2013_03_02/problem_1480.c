#include <stdio.h>

#define MAX_SIZE 1000

int dp[MAX_SIZE + 1];

int solve(int* array, int n);

int main()
{
	int i;
	int n;

	int array[MAX_SIZE + 1];
	while (scanf("%d", &n) != EOF) {
		for (i = 1; i <= n; ++i) {
			scanf("%d", &array[i]);
		}
		int result = solve(array, n);
		printf("%d\n", result);
	}
	return 0;
}

int solve(int* array, int n)
{
	int i, j;

	memset(dp, 0, sizeof(dp));
	int result = -1;
	for (i = 1; i <= n; ++i) {
		for (j = 0; j < i; ++j) {
			if (array[i] <= array[j]) {
				continue;
			}

			if (dp[i] < dp[j] + array[i]) {
				dp[i] = dp[j] + array[i];
			}
		}

		if (result < dp[i]) {
			result = dp[i];
		}
	}
	return result;
}
