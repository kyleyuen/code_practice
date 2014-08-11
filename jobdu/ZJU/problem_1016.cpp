#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <cmath>

using namespace std;

string solve(const string& a, const string& b);
void getNumbers(const string& s, stack<int>& numbers);
void getPrimes(vector<int>& primes);
bool isPrime(int n);
void calculate(stack<int>& numbersA, stack<int>& numbersB, stack<int>& result, const vector<int>& primes);
void align(stack<int>& numbersA, stack<int>& numbersB);
void process(stack<int>& stk, int size);
string toString(stack<int>& result);
string numberToString(int number);

int main()
{
	string a, b;
	while (cin >> a >> b) {
		if (a == "0" || b == "0") {
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

	stack<int> result;
	calculate(numbersA, numbersB, result, primes);
	return toString(result);
}

void calculate(stack<int>& numbersA, stack<int>& numbersB, stack<int>& result, const vector<int>& primes)
{
	align(numbersA, numbersB);
	int index = 0;
	int carry = 0;
	while (!numbersA.empty() && !numbersB.empty()) {
		int a = numbersA.top();
		int b = numbersB.top();
		result.push((a + b + carry) % primes[index]);
		carry = (a + b + carry) / primes[index];

		numbersA.pop();
		numbersB.pop();
		++index;
	}
	if (carry == 1) {
		result.push(1);
	}
}

void align(stack<int>& numbersA, stack<int>& numbersB)
{
	if (numbersA.size() < numbersB.size()) {
		int size = numbersB.size() - numbersA.size();
		process(numbersA, size);
	}
	else {
		int size = numbersA.size() - numbersB.size();
		process(numbersB, size);
	}
}

void process(stack<int>& stk, int size)
{
	stack<int> temp;
	while (!stk.empty()) {
		temp.push(stk.top());
		stk.pop();
	}
	for (int i = 0; i < size; ++i) {
		stk.push(0);
	}
	while (!temp.empty()) {
		stk.push(temp.top());
		temp.pop();
	}
}

string toString(stack<int>& result)
{
	string s;
	s += numberToString(result.top());
	result.pop();
	while (!result.empty()) {
		s += ",";
		s += numberToString(result.top());
		result.pop();
	}
	return s;
}

string numberToString(int number)
{
	stringstream ss;
	ss << number;
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

void getPrimes(vector<int>& primes)
{
	for (int i = 2; i < 150; ++i) {
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
