#include <iostream>
#include <string>
#include <map>

using namespace std;

string solve(const string& line);

int main()
{
	string line;
	while (cin >> line) {
		if (line == "E") {
			break;
		}
		cout << solve(line) << endl;
	}
	return 0;
}

string solve(const string& line)
{
	map<char, int> dictionary;
	for (string::size_type i = 0; i != line.size(); ++i) {
		++dictionary[line[i]];
	}

	string result;
	while (dictionary['Z'] > 0 || dictionary['O'] > 0 || dictionary['J'] > 0) {
		if (dictionary['Z'] > 0) {
			result += "Z";
			--dictionary['Z'];
		}
		if (dictionary['O'] > 0) {
			result += "O";
			--dictionary['O'];
		}
		if (dictionary['J'] > 0) {
			result += "J";
			--dictionary['J'];
		}
	}
	return result;
}
