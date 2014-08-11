#include <stdio.h>
#include <string.h>

void solve(char* str);
int isDivide(char* str, int n);

int main()
{
	char line[31];
	while (1) {
		scanf("%s", line);
		if (strcmp(line, "-1") == 0) {
			break;
		}

		solve(line);
	}
	return 0;
}

void solve(char* str)
{
	int i;
	int flag = 0;
	int result[10] = { 0 };
	for (i = 2; i < 10; ++i) {
		if (isDivide(str, i)) {
			result[i] = 1;
			flag = 1;
		}
	}

	if (flag) {
		for (i = 2; i < 10; ++i) {
			if (result[i] == 1) {
				printf("%d", i);
				break;
			}
		}
		for (i = i + 1; i < 10; ++i) {
			if (result[i] == 1) {
				printf(" %d", i);
			}
		}
		printf("\n");
	}
	else {
		printf("none\n");
	}
}

int isDivide(char* str, int n)
{
	int i;
	int len = strlen(str);

	int temp;
	int value = 0;
	for (i = 0; i < len; ++i) {
		temp = (str[i] - '0') + value * 10;
		value = temp % n;
	}

	return value == 0;
}
