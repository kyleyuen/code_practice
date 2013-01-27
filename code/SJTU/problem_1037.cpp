#include <iostream>
#include <string>

using namespace std;

string add(const string& lhs, const string& rhs);
string subtract(const string& lhs, const string& rhs);
void erasePrefixZero(string& s);
string multiply(const string& lhs, const string& rhs);

int main()
{
    string a, b;
    while (cin >> a >> b) {
        cout << add(a, b) << endl;
        cout << subtract(a, b) << endl;
        cout << multiply(a, b) << endl;
    }
    return 0;
}

string add(const string& lhs, const string& rhs)
{
    string result;
    if (lhs.size() < rhs.size()) {
        result = rhs;
    }
    else {
        result = lhs;
    }

    string::reverse_iterator iter = result.rbegin();
    for (string::const_reverse_iterator lit = lhs.rbegin(), rit = rhs.rbegin();
        lit != lhs.rend() && rit != rhs.rend(); ++lit, ++rit) {
        *iter = *lit + *rit - '0';
        ++iter;
    }

    for (string::reverse_iterator iter = result.rbegin(); iter != result.rend() - 1; ++iter) {
        if (*iter > '9') {
            *iter -= 10;
            ++*(iter + 1);
        }
    }
    if (*result.begin() > '9') {
        *result.begin() -= 10;
        result = "1" + result;
    }
    return result;
}

string subtract(const string& lhs, const string& rhs)
{
    string result;
    if ((lhs.size() < rhs.size())
        || ((lhs.size() == rhs.size()) && (lhs.compare(rhs) < 0))) {
        result = subtract(rhs, lhs);
        result = "-" + result;
        return result;
    }

    if (lhs.size() < rhs.size()) {
        result = rhs;
    }
    else {
        result = lhs;
    }

    string::iterator iter = result.end() - 1;
    for (string::const_iterator lit = lhs.end() - 1, rit = rhs.end() - 1;
        lit != lhs.begin() - 1 && rit != rhs.begin() - 1; --lit, --rit, --iter) {
        *iter = *lit - *rit + '0';
    }

    for (string::iterator iter = result.end() - 1; iter != result.begin(); --iter) {
        if (*iter < '0') {
            *iter += 10;
            --*(iter - 1);
        }
    }

    erasePrefixZero(result);
    return result;
}

string multiply(const string& lhs, const string& rhs)
{
    string result;

    for (string::size_type n = 0; n != rhs.size(); ++n) {
        string sum(lhs);
        int single(rhs[rhs.size() - n - 1] - '0');
        string::reverse_iterator isum = sum.rbegin();
        for (string::const_reverse_iterator iter = lhs.rbegin(); iter != lhs.rend(); ++iter) {
            *isum = (*iter - '0') * single;
            ++isum;
        }
        for (string::iterator iter = sum.end() - 1; iter != sum.begin(); --iter) {
            *(iter - 1) += *iter / 10;
            *iter = *iter % 10 + '0';
        }
        if (*sum.begin() > 9) {
            char c = *sum.begin() / 10 + '0';
            *sum.begin() = *sum.begin() % 10 + '0';
            sum = string(1, c) + sum;
        }
        else {
            *sum.begin() += '0';
        }
        sum += string(n, '0');
        result = add(result, string(sum));
    }

    return result;
}


void erasePrefixZero(string& s)
{
    if (s.size() == 0) {
        return;
    }
    for (string::iterator iter = s.begin(); iter != s.end(); ++iter) {
        if (*iter != '0') {
            s.erase(s.begin(), iter);
            return;
        }
    }
    s.erase(s.begin(), s.end() - 1);
}
