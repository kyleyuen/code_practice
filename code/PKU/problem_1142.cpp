#include <iostream>

using namespace std;

const int PHYSICAL_CYCLE = 23;
const int EMOTIONAL_CYCLE = 28;
const int INTELLECTUAL_CYCLE = 33;

int solve(int physical, int emotional, int intellectual, int days);

int main()
{
	int physical;
	int emotional;
	int intellectual;
	int days;

	int counter = 0;
	while (cin >> physical >> emotional >> intellectual >> days) {
		if (physical == -1 && emotional == -1 && intellectual == -1 && days == -1) {
			break;
		}

		++counter;
		cout << "Case " << counter << ": the next triple peak occurs in ";
		cout << solve(physical, emotional, intellectual, days) << " days." << endl;
	}
	return 0;
}

int solve(int physical, int emotional, int intellectual, int days)
{
	physical %= PHYSICAL_CYCLE;
	emotional %= EMOTIONAL_CYCLE;
	intellectual %= INTELLECTUAL_CYCLE;

	int result = 0;
	while (true) {
		++result;

		if (result % PHYSICAL_CYCLE == physical
		 && result % EMOTIONAL_CYCLE == emotional
		 && result % INTELLECTUAL_CYCLE == intellectual) {
			break;
		}
	}
	return result - days;
}