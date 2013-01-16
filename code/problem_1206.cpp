#include <iostream>
#include <string>

using namespace std;

string solve(const string& a, const string& b);

int main()
{
	string a, b;
	while (cin >> a >> b) {
		cout << solve(a, b) << endl;
	}
	return 0;
}

string solve(const string& a, const string& b)
{
	return a + b;
}
