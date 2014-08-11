#include <iostream>

using namespace std;

void solve(int A, int B, int N);

int main()
{
	int A, B, N;
	while (cin >> A >> B >> N) {
		solve(A, B, N);
	}
	return 0;
}

void solve(int A, int B, int N)
{
	int first = 0;
	int second = 0;
	while (second != N) {
		if (first == 0) {
			first = A;
			cout << "fill A" << endl;
		}
		else {
			int value = B - second;
			if (value > first) {
				value = first;
			}

			second += value;
			first -= value;
			cout << "pour A B" << endl;

			if (second == B) {
				second = 0;
				cout << "empty B" << endl;
			}
		}
	}
	cout << "success" << endl;
}