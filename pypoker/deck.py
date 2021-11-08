class Deck:

    tam = 52
    num_of_suits= 4
    cards = []

    def __init__(self):
        
        cards_per_suit = self.tam / self.num_of_suits
        for i in range(self.tam):

            self.cards.append([])
            if i % cards_per_suit == 10:
                self.cards[i].append("Jack")
            elif i % cards_per_suit == 11:
                self.cards[i].append("Queen")
            elif i % cards_per_suit == 12:
                self.cards[i].append("King")
            else:
                self.cards[i].append(str((i+1) % 13))

            if len(self.cards) < 14:
                self.cards[i].append("Clubs")
            elif len(self.cards) < 27:
                self.cards[i].append("Diamonds")
            elif len(self.cards) < 40:
                self.cards[i].append("Hearts")
            else:
                self.cards[i].append("Spades")

