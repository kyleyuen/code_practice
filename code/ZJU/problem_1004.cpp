#include <iostream>
#include <vector>

using namespace std;

int solve(const vector<int>& sequenceA, const vector<int>& sequenceB);

int main()
{
	int m;
	while (cin >> m) {
		vector<int> sequenceA(m);
		for (int i = 0; i < m; ++i) {
			cin >> sequenceA[i];
		}

		int n;
		cin >> n;
		vector<int> sequenceB(n);
		for (int i = 0; i < n; ++i) {
			cin >> sequenceB[i];
		}

		cout << solve(sequenceA, sequenceB) << endl;
	}
}

int solve(const vector<int>& sequenceA, const vector<int>& sequenceB)
{
	vector<int> result(sequenceA.size() + sequenceB.size());
	int indexA = 0;
	int indexB = 0;
	int index = 0;
	while (indexA < sequenceA.size() && indexB < sequenceB.size()) {
		if (sequenceA[indexA] < sequenceB[indexB]) {
			result[index] = sequenceA[indexA];
			++indexA;
		}
		else {
			result[index] = sequenceB[indexB];
			++indexB;
		}
		++index;
	}

	while (indexA < sequenceA.size()) {
		result[index] = sequenceA[indexA];
		++index;
		++indexA;
	}
	while (indexB < sequenceB.size()) {
		result[index] = sequenceB[indexB];
		++index;
		++indexB;
	}
	return result[(result.size() - 1) / 2];
}
