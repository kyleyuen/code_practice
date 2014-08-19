#include <iostream>
#include <string>
#include <algorithm>

using std::cout;
using std::endl;
using std::string;

string translate_decimal_to_representation(double value);

int main()
{
	cout << translate_decimal_to_representation(11.51) << endl;
	return 0;
}


string translate_decimal_to_representation(double value)
{
	string result;

	int integer_part = int(value);
	while (integer_part != 0) {
		if (integer_part & 1 == 1) {
			result.append("1");
		}
		else {
			result.append("0");
		}
		integer_part >>= 1;
	}
	reverse(result.begin(), result.end());

	result.append(".");

	double decimal_part = value - int(value);
	double fraction = 0.5;
	while (decimal_part > 0) {
		if (result.size() > 64) {
			break;
		}

		if (decimal_part >= fraction) {
			result.append("1");
			decimal_part -= fraction;
		}
		else {
			result.append("0");
		}
		fraction /= 2;
	}
	return result;
}