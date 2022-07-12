class Card():

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def get_color(self):
        return self.color
    
    def get_value(self):
        return self.value


class Hand():

    def __init__(self, cards: list[Card]):
        self.cards: list[Card] = cards
        self.dist = {i:0 for i in range(1, 15)}
        for card in self.cards:
            val = card.get_value()
            self.dist[val] += 1
        self.dist[1] = self.dist[14]
        #Calcular rank
        self.rank = self.calc_rank()

    def is_royal_flush(self):
        if not self.is_flush():
            return False
        srted = sorted(self.cards, key= lambda c: c.get_value())
        if all([self.dist[k] == 1 for k in range(10,15)]):
            return True
        return False

    def is_flush(self):
        return all([card.get_color() == self.cards[0].get_color() for card in self.cards[1:]])
    
    def straight_high_card(self):
        for value in range(1, 11):
            if all([self.dist[value + k] == 1 for k in range(5)]):
                return value + 4
        return None
    
    def card_count(self, num, exclude=None):
        for value in range(2, 15):
            if value == exclude:
                continue
            if self.dist[value] == num:
                return value
        return None

    def calc_rank(self):
        if self.is_royal_flush():
            return 9
        if self.straight_high_card() is not None and self.is_flush():
            return 8
        if self.card_count(4) is not None:
            return 7
        if self.card_count(3) is not None and card_count(2) is not None:
            return 6
        if self.is_flush():
            return 5
        if self.straight_high_card() is not None:
            return 4
        if self.card_count(3) is not None:
            return 3
        pair = self.card_count(2)
        if pair is not None:
            if self.card_count(2, exclude=pair) is not None:
                return 2
            return 1
        return 0

def compare_hands(player: list[Card], opponent: list[Card]):
    player_hand = Hand(player)
    opponent_hand = Hand(opponent)
    #Caso player tiene mejor mano
    if player_hand.rank > opponent_hand.rank:
        return True
    #Caso son iguales
    elif player_hand.rank < opponent_hand.rank:
        return False
    #Caso oponente tiene mejor mano
    else:
        return tie_break(player_hand, opponent_hand)


if __name__ == "__main__":
    cards1 = []
    for i in range(10,15):
        cards1.append(Card(i,"S"))
    cards2 = []
    for i in range(9,14):
        cards2.append(Card(i,"S"))
    print(compare_hands(cards2, cards1))