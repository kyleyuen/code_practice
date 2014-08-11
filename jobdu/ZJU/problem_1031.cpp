#include <iostream>

using namespace std;

int solve(int n);

int main()
{
	int n;
	while (cin >> n) {
		if (n == 0) {
			break;
		}
		cout << solve(n) << endl;
	}
}

int solve(int n)
{
	int result = 0;
	while (n != 1) {
		if (n % 2 == 1) {
			n = n * 3 + 1;
		}
		n /= 2;
		++result;
	}
	return result;
}
