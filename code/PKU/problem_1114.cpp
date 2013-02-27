#include <iostream>
#include <vector>

using namespace std;

const int VOLUME = 40;

int solve(const vector<int>& array);
void search(const vector<int>& array, int index, int value, int& result);

int main()
{
	int n;
	while (cin >> n) {
		vector<int> array(n);
		for (int i = 0; i < n; ++i) {
			cin >> array[i];
		}
		cout << solve(array) << endl;
	}
	return 0;
}

int solve(const vector<int>& array)
{
	int result = 0;
	search(array, 0, 0, result);
	return result;
}

void search(const vector<int>& array, int index, int value, int& result)
{
	if (value == VOLUME) {
		++result;
		return;
	}
	if (index > array.size()) {
		return;
	}

	search(array, index + 1, value, result);
	if (value + array[index] <= VOLUME) {
		search(array, index + 1, value + array[index], result);
	}
}