#include <iostream>
#include <vector>

using namespace std;

void inverse(vector< vector<int> >& matrix, int n);

int main()
{
	int n;
	while (cin >> n) {
		vector< vector<int> > matrix(n, vector<int>(n));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> matrix[i][j];
			}
		}

		inverse(matrix, n);

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n - 1; ++j) {
				cout << matrix[i][j] << " ";
			}
			cout << matrix[i][n - 1] << endl;
		}
	}
	return 0;
}

void inverse(vector< vector<int> >& matrix, int n)
{
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			int temp = matrix[i][j];
			matrix[i][j] = matrix[j][i];
			matrix[j][i] = temp;
		}
	}
}
