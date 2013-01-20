#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Spell {
	string name;
	string effect;

};

void addSpell(vector<Spell>& spells, const string& line);
void solve(int n, const vector<Spell>& spells);
string lookUpInSpells(const vector<Spell>& spells, string& line);

int main()
{
	string line;
	vector<Spell> spells;
	while (getline(cin, line)) {
		if (line == "@END@") {
			break;
		}

		addSpell(spells, line);
	}

	int n;
	cin >> n;
	solve(n, spells);
	return 0;
}

void addSpell(vector<Spell>& spells, const string& line)
{
	size_t start = line.find('[');
	size_t end = line.find(']');

	Spell spell;
	spell.name = line.substr(start + 1, end - 1);
	spell.effect = line.substr(end + 2);
	spells.push_back(spell);
}

void solve(int n, const vector<Spell>& spells)
{
	string line;
	getline(cin, line);
	for (int i = 0; i < n; ++i){
		getline(cin, line);
		cout << lookUpInSpells(spells, line) << endl;
	}
}

string lookUpInSpells(const vector<Spell>& spells, string& line)
{
	if (line.find('[') != string::npos) {
		line = line.substr(1, line.size() - 2);
	}

	for (vector<Spell>::const_iterator iter = spells.begin(); iter != spells.end(); ++iter) {
		if (iter->name == line) {
			return iter->effect;
		}
		if (iter->effect == line) {
			return iter->name;
		}
	}
	return "what?";
}
