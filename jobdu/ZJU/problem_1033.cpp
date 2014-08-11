#include <iostream>
#include <vector>
#include <set>
#include <stack>

using namespace std;

void solve(const vector<int>& numbers);
void calculate(int n, set<int>& record);

int main()
{
	int n;
	while (cin >> n) {
		if (n == 0) {
			break;
		}

		vector<int> numbers(n);
		for (int i = 0; i < n; ++i) {
			cin >> numbers[i];
		}
		solve(numbers);
	}
	return 0;
}

void solve(const vector<int>& numbers)
{
	stack<int> result;
	set<int> record;
	for (int i = 0; i < numbers.size(); ++i) {
        calculate(numbers[i], record);
	}

	bool flag = false;
	for (int i = numbers.size() - 1; i >= 0; --i) {
		if (record.count(numbers[i]) == 0) {
			if (flag) {
				cout << " ";
			}
			cout << numbers[i];
			flag = true;
		}
	}
	cout << endl;
}

void calculate(int n, set<int>& record)
{
	while (n != 1) {
		if (n % 2 == 1) {
			n = n * 3 + 1;
		}
		n /= 2;

		if (record.count(n) == 0) {
			record.insert(n);
		}
		else {
			break;
		}
	}
}
