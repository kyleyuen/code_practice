#include <iostream>

using std::cout;
using std::endl;

int bits_required_to_convert(int a, int b);

int main()
{
	cout << bits_required_to_convert(31, 14) << endl;
	return 0;
}


int bits_required_to_convert(int a, int b)
{
	int result = 0;

	int n = a ^ b;
	while (n != 0) {
		result += n & 1;
		n >>= 1;
	}

	return result;
}