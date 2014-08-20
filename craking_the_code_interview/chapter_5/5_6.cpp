#include <iostream>

using std::cout;
using std::endl;

int swap_odd_and_even_bits(int n);

int main()
{
	cout << swap_odd_and_even_bits(5) << endl;
	return 0;
}


int swap_odd_and_even_bits(int n)
{
	return ((n&0xaaaaaaaa)>>1) | ((n&0x55555555)<<1);
}