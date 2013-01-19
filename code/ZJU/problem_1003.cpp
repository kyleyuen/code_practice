#include <iostream>
#include <string>

using namespace std;

int solve(const string& a, const string& b);
int transform(const string& str);

int main()
{
	string a, b;
	while (cin >> a >> b) {
		cout << solve(a, b) << endl;
	}
	return 0;
}

int solve(const string& a, const string& b)
{
	return transform(a) + transform(b);
}

int transform(const string& str)
{
	int result = 0;
	if (str[0] == '-') {
		for (string::size_type i = 1; i != str.size(); ++i) {
			if (str[i] == ',') {
			continue;
			}
			result = (str[i] - '0') + result * 10;
		}
		return -result;
	}
	else {
		for (string::size_type i = 0; i != str.size(); ++i) {
			if (str[i] == ',') {
				continue;
			}
			result = (str[i] - '0') + result * 10;
		}
		return result;
	}
}
