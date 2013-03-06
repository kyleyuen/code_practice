#include <stdio.h>

#define MAX_SIZE 1000

void solve(int n, int k, int* deck);
void shift(int* deck, int n, int x);
void flip(int* deck, int n);
void reverse(int* deck, int n, int start, int end);

int main()
{
	int deck[MAX_SIZE + 1];
	int n, k;
	while (scanf("%d %d", &n, &k) != 0) {
	    if (n == 0 && k == 0) {
            break;
        }
		solve(n, k, deck);
	}
	return 0;
}

void solve(int n, int k, int* deck)
{
	int i;
	for (i = 1; i <= n; ++i) {
		deck[i] = i;
	}

	for (i = 0; i < k; ++i) {
		int x;
		scanf("%d", &x);

		shift(deck, n, x);
		flip(deck, n);
	}

	for (i = 1; i <= n; ++i) {
		printf("%d ", deck[i]);
	}
	printf("\n");
}

void shift(int* deck, int n, int x)
{
	reverse(deck, n, 1, x);
	reverse(deck, n, x + 1, n);
	reverse(deck, n, 1, n);
}

void reverse(int* deck, int n, int start, int end)
{
	int i;
	for (i = 0; i < (end - start + 1) / 2; ++i) {
		int temp = deck[start + i];
		deck[start + i] = deck[end - i];
		deck[end - i] = temp;
	}
}

void flip(int* deck, int n)
{
	reverse(deck, n, 1, n / 2);
}
