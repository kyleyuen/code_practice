#include <iostream>

using std::cout;
using std::endl;

int get_next_smallest(int n);
int get_next_largest(int n);
void get_key_position(int n, int& c0, int& c1);

int main()
{
	int n = 13948;

	cout << n << "'s next smallest number is: ";
	cout << get_next_smallest(n) << endl;
	cout << n << "'s next largest number is: ";
	cout << get_next_largest(n) << endl;

	return 0;
}


int get_next_smallest(int n)
{
	int c0, c1;
	get_key_position(n, c0, c1);
	int result = n - (1<<c1) - (1<<(c0-1)) + 1;
	return result;
}


int get_next_largest(int n)
{
	int c0 = 0;
	int c1 = 0;
	get_key_position(n, c0, c1);
	int result = n + (1<<c0) + (1<<(c1-1)) - 1;
	return result;
}


void get_key_position(int n, int& c0, int& c1)
{
	int c = n;
	while (((c&1) == 0) && (c!=0)) {
		++c0;
		c >>= 1;
	}

	while ((c&1) == 1) {
		++c1;
		c >>= 1;
	}
}