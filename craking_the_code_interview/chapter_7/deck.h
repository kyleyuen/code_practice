#ifndef DECK_H
#define DECK_H

#include <vector>

using std::vector;

enum Suit {
	Spade, Heart, Club, Diamond,
};



class Card {
public:
	Card(int n, Suit s) { number = n; suit_type = s; }

	int get_number() { return number; }
	Suit get_suit_type() { return suit_type; }

private:
	int number;
	Suit suit_type;
};



class Rule {
public:
	bool is_finished();
};



class Deck {
public:
	Deck(Rule = r);
	vector<Card> get_deck() { return deck; }

	void shuffle();
	Card get_card(int number, Suit suit);
	bool insert_card(const Card&);
	bool remove_card(int number, Suit suit);

private:
	vector<Card> deck;
	Rule game_rule;
};

#endif