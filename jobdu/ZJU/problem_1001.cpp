#include <iostream>
#include <vector>

using namespace std;

int solve(int m, int n)
int countMatrixZero(const vector< vector<int> >& matrix);
void matrixPlus(const vector< vector<int> >& matrixA, 
				const vector< vector<int> >& matrixB, 
				vector< vector<int> >& result);

int main()
{
	int m, n;
	while (cin >> m >> n) {
		cout << solve(m, n) << endl;
	}
	return 0;
}

int solve(int m, int n)
{
	vector< vector<int> > matrixA;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> matrixA[i][j];
		}
	}
	vector< vector<int> > matrixB;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> matrixB[i][j];
		}
	}

	vector< vector<int> > result(m, vector<int>(n));
	matrixPlus(matrixA, matrixB, result);
	return countMatrixZero(result);
}

void matrixPlus(const vector< vector<int> >& matrixA, 
				const vector< vector<int> >& matrixB, 
				vector< vector<int> >& result)
{
	int m = matrixA.size();
	int n = matrixA[0].size();
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			result[i][j] = matrixA[i][j] + matrixB[i][j];
		}
	}
}

int countMatrixZero(const vector< vector<int> >& matrix)
{
	int result = 0;
	for (int i = 0; i < m; ++i) {
		bool judge = true;
		for (int j = 0; j < n; ++j) {
			if (matrix[i][j] != 0) {
				judge = false;
				break;
			}
		}
		if (judge) {
			++result;
		}
	}

	for (int j = 0; j < n; ++j) {
		bool judge = true;
		for (int i = 0; i < m; ++i) {
			if (matrix[i][j] != 0) {
				judge = false;
				break;
			}
		}
		if (judge) {
			++result;
		}
	}

	return result;
}