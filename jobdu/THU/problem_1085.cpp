#include <iostream>

using namespace std;

long long solve(long long x, long long y, long long n);

int main()
{
	int x, y, k;
	while (cin >> x >> y >> k) {
		int result = solve(x, y, k - 1);
		if (result == 0) {
			result = k - 1;
		}
		cout << result << endl;
	}
}

long long solve(long long x, long long y, long long n)
{
	long long result = 1;
	while (y != 0) {
		if (y & 1) {
			result = result * x % n;
		}
		x = x * x % n;
		y >>= 1;
	}
	return result;
}
