#include <iostream>

int shift_and_set(int n, int m, int i, int j);

using std::cout;
using std::endl;

int main()
{
	cout << shift_and_set(1024, 21, 2, 6) << endl;
	return 0;
}


int shift_and_set(int n, int m, int i, int j)
{
	int mask = (-1 << (j+1)) | ((1 << i) - 1);
	int result = (n & mask) | (m << i);
	return result;
}