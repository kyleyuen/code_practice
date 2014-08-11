#include <iostream>
#include <string>

using namespace std;

bool judge(const string& line);

int main()
{
	string line;
	while (cin >> line) {
		if (judge(line)) {
			cout << "Yes!" << endl;
		}
		else {
			cout << "No!" << endl;
		}
	}
	return 0;
}

bool judge(const string& line)
{
	for (string::size_type i = 0; i != line.size() / 2; ++i) {
		if (line[i] != line[line.size() - i - 1]) {
			return false;
		}
	}
	return true;
}
