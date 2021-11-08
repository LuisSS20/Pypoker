import deck
from operator import itemgetter

class Player:

    cards_owned = []
    poker_hand = ""

    def add_new_card(self, new_card):
        self.cards_owned.append([])
        #adding value
        self.cards_owned[len(self.cards_owned)-1].append(new_card[0])
        #Adding suit
        self.cards_owned[len(self.cards_owned)-1].append(new_card[1])
    
    '''
    def sort_cards_owned(self):
        self.cards_owned = sorted(self.cards_owned, key=itemgetter(0))
        return self.cards_owned
    '''
    def get_poker_hand(self):
        pass

    def find_card(self, val):
        for i in range(len(self.cards_owned)):
            if self.cards_owned[i][0] == val:
                return True

        return False
    
    def find_card_with_suit(self, val):
        for i in range(len(self.cards_owned)):
            if self.cards_owned[i][0] == val[0] and self.cards_owned[i][1] == val[1]:
                return True

        return False

    def get_suit(self, value):
        for i in range(len(self.cards_owned)):
            if self.cards_owned[i][0] == value:
                return self.cards_owned[i][1]


    def check_royal_flush(self):
        suit = ""

        if self.find_card('10'):
            suit = self.get_suit('10')
            if self.find_card_with_suit(['J',suit]):
                if self.find_card_with_suit(['Q',suit]):
                    if self.find_card_with_suit(['K',suit]):
                        if self.find_card_with_suit(['A',suit]):
                            return True
        
        return False




        

