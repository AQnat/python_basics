from collections import namedtuple
import random

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


    def __init__(self):  # Tworzy talię kart, tzn. figurom przyporządkowuje kolory
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  # LISTA SKŁADANA

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __str__(self):
        return f'FrenchDeck has {len(self)} cards'

    #def __repr__(self):
        return f'FrenchDeck{id(self)}'


if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck)
    print(deck[5])
    #print(list(reversed(deck)))
    #print(len(deck))  # FrenchDeck.__len__(deck)