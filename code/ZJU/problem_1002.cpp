#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

double solve(int p, int t, int g1, int g2, int g3, int gj);

int main()
{
	int p;
	while (cin >> p) {
	    int t;
		cin >> t;
		int g1, g2, g3, gj;
		cin >> g1 >> g2 >> g3 >> gj;

		cout << setiosflags(ios::fixed) << setprecision(1);
		cout << solve(p, t, g1, g2, g3, gj) << endl;
	}
	return 0;
}

double solve(int p, int t, int g1, int g2, int g3, int gj)
{
	if (abs(g1 - g2) <= t) {
		return (g1 + g2) / 2.0;
	}

	if (abs(g1 - g3) <= t && abs(g2 - g3) <= t) {
		return max(max(g1, g2), g3);
	}

	if (abs(g1 - g3) > t && abs(g2 - g3) > t) {
		return gj;
	}

	if (abs(g1 - g3) < abs(g2 - g3)) {
		return (g1 + g3) / 2.0;
	}
	else {
		return (g2 + g3) / 2.0;
	}
}
