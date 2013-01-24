#include <iostream>
#include <vector>

using namespace std;

double solve(double limit, int numberOfChecks);
void search(int index, double result, double limit, const vector<double>& checks, double& max);

int main()
{
	double limit;
	int numberOfChecks;
	while (cin >> limit >> numberOfChecks) {
		if (numberOfChecks == 0) {
			break;
		}
		cout.setf(ios::fixed);
		cout.precision(2);
		cout << solve(limit, numberOfChecks) << endl;
	}
	return 0;
}

double solve(double limit, int numberOfChecks)
{
	vector<double> checks;
	for (int i = 0; i < numberOfChecks; ++i) {
		int n;
		cin >> n;
		double sum = 0;
		bool flag = true;
		for (int j = 0; j < n; ++j) {
			char type;
			char ignore;
			cin >> type >> ignore;
			double money;
			cin >> money;

			if (((type != 'A') && (type != 'B') && (type != 'C')) || money > 600) {
				flag = false;
			}
			sum += money;
		}
		if (flag && sum <= 1000) {
			checks.push_back(sum);
		}
	}

	double max = 0;
	search(0, 0, limit, checks, max);
	return max;
}

void search(int index, double result, double limit, const vector<double>& checks, double& max)
{
	if (index == checks.size()) {
		if (max < result) {
			max = result;
		}
		return;
	}

	if (result + checks[index] <= limit) {
		search(index + 1, result + checks[index], limit, checks, max);
	}
	search(index + 1, result, limit, checks, max);
}