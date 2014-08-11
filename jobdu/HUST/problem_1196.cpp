#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

struct Student {
	int id;
	int score;
};

bool compare(const Student& lhs, const Student& rhs) {
	if (lhs.score == rhs.score) {
		return lhs.id < rhs.id;
	}
	else {
		return lhs.score < rhs.score;
	}
}

void printResult(const vector<Student>& students);

int main()
{
	int n;
	while (scanf("%d",&n) != EOF) {
		vector<Student> students(n);
		for (int i = 0; i < n; ++i) {
			scanf("%d %d",&students[i].id,&students[i].score);
		}

		sort(students.begin(), students.end(), compare);
		printResult(students);
	}
	return 0;
}

void printResult(const vector<Student>& students)
{
	for (vector<int>::size_type i = 0; i != students.size(); ++i) {
		printf("%d %d\n", students[i].id, students[i].score);
	}
}

