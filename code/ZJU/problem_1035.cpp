#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve(int n, int m);
int search(int first, int second, const vector<int>& relation);
void printResult(int distance);

int main()
{
	int n, m;
	while (cin >> n >> m) {
		if (n == 0 && m == 0) {
			break;
		}
		solve(n, m);
	}
	return 0;
}

void solve(int n, int m)
{
	vector<int> relation(26, -1);
	string line;
	for (int i = 0; i < n; ++i) {
		cin >> line;
		if (line[1] != '-') {
			relation[line[1] - 'A'] = line[0] - 'A';
		}
		if (line[2] != '-') {
			relation[line[2] - 'A'] = line[0] - 'A';
		}
	}

	for (int i = 0; i < m; ++i) {
		cin >> line;
		int first = line[0] - 'A';
		int second = line[1] - 'A';

		int resultA = search(first, second, relation);
		if (resultA != 0) {
			printResult(resultA);
		}
		int resultB = search(second, first, relation);
		if (resultB != 0) {
			printResult(resultB * -1);
		}

		if (resultA == 0 && resultB == 0) {
			cout << "-" << endl;
		}
	}
}

int search(int first, int second, const vector<int>& relation)
{
	int distance = 0;
	while (relation[first] != -1) {
		++distance;
		first = relation[first];
		if (first == second) {
			return distance;
		}
	}
	return 0;
}

void printResult(int distance)
{
	string result;
	while (distance > 0) {
		if (distance == 1) {
			result += "parent";
		}
		else if (distance == 2) {
			result += "grand";
		}
		else {
			result += "great-";
		}
		--distance;
	}

	while (distance < 0) {
		if (distance == -1) {
			result += "child";
		}
		else if (distance == -2) {
			result += "grand";
		}
		else {
			result += "great-";
		}
		++distance;
	}
	cout << result << endl;
}
