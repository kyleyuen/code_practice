#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void solve(vector<string>& lines);

bool compare(const string& lhs, const string& rhs)
{
	return lhs.size() < rhs.size();
}

int main()
{
	vector<string> lines;
	string line;
	while (cin >> line) {
		lines.push_back(line);
	}

	solve(lines);
	return 0;
}

void solve(vector<string>& lines)
{
	sort(lines.begin(), lines.end(), compare);
	cout << lines[0] << endl;
	for (int i = 1; i < lines.size(); ++i) {
		if (lines[i].size() != lines[i - 1].size()) {
			break;
		}
		cout << lines[i] << endl;
	}

	int start;
	for (int i = lines.size() - 2; i >= 0; --i) {
		if (lines[i].size() != lines[i + 1].size()) {
			start = i + 1;
			break;
		}
	}
	for (int i = start; i < lines.size(); ++i) {
		cout << lines[i] << endl;
	}
}

