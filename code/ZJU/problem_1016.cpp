#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <cmath>

using namespace std;

string solve(const string& a, const string& b);
string toString(int result, const vector<int>& factors);
string numberToString(int n);
void getNumbers(const string& s, stack<int>& numbers);
int getNumber(stack<int>& stk, const vector<int>& factors);
void getFactors(vector<int>& factors, vector<int>& primes);
void getPrimes(vector<int>& primes);
bool isPrime(int n);

int main()
{
	string a, b;
	while (cin >> a >> b) {
		if (a == "0" && b == "0") {
			break;
		}
		cout << solve(a, b) << endl;
	}
	return 0;
}

string solve(const string& a, const string& b)
{
	stack<int> numbersA;
	getNumbers(a, numbersA);
	stack<int> numbersB;
	getNumbers(b, numbersB);

	vector<int> primes;
	getPrimes(primes);
	vector<int> factors;
	getFactors(factors, primes);

	int numberA = getNumber(numbersA, factors);
	int numberB = getNumber(numbersB, factors);
	int result = numberA + numberB;
	return toString(result, primes);
}

string toString(int n, const vector<int>& primes)
{
	stack<int> numbers;
	int index = 0;
	while (n != 0) {
		int remain = n % primes[index];
		numbers.push(remain);
		n /= primes[index];
		++index;
	}

	string result;
	result += numberToString(numbers.top());
	numbers.pop();
	while (!numbers.empty()) {
		result += ",";
		result += numberToString(numbers.top());
		numbers.pop();
	}
    return result;
}

string numberToString(int n)
{
	stringstream ss;
	ss << n;
	return ss.str();
}

void getNumbers(const string& s, stack<int>& numbers)
{
	stringstream ss(s);
	int number;
	char c;
	ss >> number;
	numbers.push(number);
	while (!ss.eof()) {
		ss >> c;
		ss >> number;
		numbers.push(number);
	}
}

int getNumber(stack<int>& stk, const vector<int>& factors)
{
	int result = 0;
	int index = 0;
	while (!stk.empty()) {
		result += stk.top() * factors[index];
		++index;
		stk.pop();
	}
	return result;
}

void getFactors(vector<int>& factors, vector<int>& primes)
{
	int acc = 1;
	factors.push_back(acc);
	for (vector<int>::size_type i = 0; i != primes.size(); ++i) {
		acc *= primes[i];
		factors.push_back(acc);
	}
}

void getPrimes(vector<int>& primes)
{
	for (int i = 2; i <= 23; ++i) {
		if (isPrime(i)) {
			primes.push_back(i);
		}
	}
}

bool isPrime(int n)
{
	for (int i = 2; i <= sqrt(n); ++i) {
		if (n % i == 0) {
			return false;
		}
	}
	return true;
}
