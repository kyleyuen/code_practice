#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

void solve(const string& line);
int countOne(char c);
void printInBinary(char c);

int main()
{
    string line;
    while (cin >> line) {
        solve(line);
    }
    return 0;
}

void solve(const string& line)
{
    for (string::const_iterator iter = line.begin(); iter != line.end(); ++iter) {
        char c = *iter;
        int counter = countOne(c);
        if (counter % 2 == 0) {
            int mask = (1 << 7);
            c |= mask;
        }
        printInBinary(c);
    }
}

int countOne(char c)
{
    int result = 0;
    int mask = 1;
    for (int i = 0; i < 8; ++i) {
        if ((c & mask) != 0) {
            ++result;
        }
        mask <<= 1;
    }
    return result;
}

void printInBinary(char c)
{
    int mask = 1 << 7;
    while (mask != 0) {
        if ((mask & c) != 0) {
            printf("1");
        }
        else {
            printf("0");
        }
        mask >>= 1;
    }
    printf("\n");
}

