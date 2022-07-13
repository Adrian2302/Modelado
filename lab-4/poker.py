#COLORS
COLORS = ["SPADES","HEARTS","CLUBS","DIAMONDS"]
#VALUES
VALUES = [1,2,3,4,5,6,7,8,9,10,11,12,13]
class Card():

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def get_color(self):
        return self.color
    
    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.value) + self.color

class Hand():

    def __init__(self, cards: list[Card]):
        self.cards: list[Card] = cards
        self.dist = {i:0 for i in range(1, 15)}
        self.values = []
        for card in self.cards:
            val = card.get_value()
            self.values.append(val)
            self.dist[val] += 1
        self.dist[14] = self.dist[1]
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
        for value in range(1, 14):
            if value == (exclude if exclude != 14 else 1):
                continue
            if self.dist[value] == num:
                return (value if value != 1 else 14)
        return None

    def calc_rank(self):
        if self.is_royal_flush():
            return 9
        if self.straight_high_card() is not None and self.is_flush():
            return 8
        if self.card_count(4) is not None:
            return 7
        if self.card_count(3) is not None and self.card_count(2) is not None:
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
    #Caso oponente tiene mejor mano
    elif player_hand.rank < opponent_hand.rank:
        return False
    #Caso son iguales
    else:
        return tie_break(player_hand, opponent_hand)

def tie_break(player: Hand, opponent: Hand):
    #Si son straights o straight flush:
    if player.straight_high_card() is not None:
        p_high_card = player.straight_high_card()
        o_high_card = opponent.straight_high_card()
        if p_high_card != o_high_card:
            return p_high_card > o_high_card
        else:
            return None
    
    #Para four of a kind, full house, three of a kind
    for i in range(2):
        if player.card_count(4-i) is not None:
            return player.card_count(4-i) > opponent.card_count(4-i)
    
    #Ver cuales son las parejas
    p_1 = player.card_count(2)
    o_1 = opponent.card_count(2)
    #Caso complejo, si son dos parejas
    if player.rank == 2:
        p_2 = player.card_count(2, exclude=p_1)
        o_2 = opponent.card_count(2, exclude=o_1)
        if p_2 != o_2:
            return p_2 > o_2
        else:
            if p_1 != o_1:
                return p_1 > o_1
            else: #kicker se refiere a la ultima carta que queda
                kicker_p = [c for c in player.values if (c if not(c == 1 and p_1 == 14) else p_1) not in (p_1, p_2)]
                kicker_o = [c for c in opponent.values if (c if not(c == 1 and p_1 == 14) else p_1) not in (o_1, o_2)]
                return highest_card(kicker_p, kicker_o)
    
    #Caso es una pareja:
    if player.rank == 1:
        if p_1 != o_1:
            return p_1 > o_1
        kickers_p = [c for c in player.values if (c if not(c == 1 and p_1 == 14) else p_1) != p_1]
        kickers_o = [c for c in opponent.values if (c if not(c == 1 and o_1 == 14) else o_1) != o_1]
        return highest_card(kickers_p, kickers_o)

    #Si son flush o no hay nada
    return highest_card(player.values, opponent.values)

def highest_card(player: list[int], opponent: list[int]):
    for c in range(len(player)):
        if player[c] == 1:
            player[c] = 14
    for c in range(len(opponent)):
        if opponent[c] == 1:
            opponent[c] = 14     
    h_player = max(player)
    h_opponent = max(opponent)
    if h_player != h_opponent:
        return h_player > h_opponent
    else:
        return None

def get_deck():
    cards: list[Card] = []
    for c in COLORS:
        for v in VALUES:
            cards.append(Card(v,c))
    return cards



if __name__ == "__main__":
    player = Hand([Card(1,"SPADES"), Card(1, "CLUBS"), Card(13, "HEARTS"), Card(13, "CLUBS"), Card(5,"SPADES")])
    opp = Hand([Card(1,"SPADES"), Card(1, "CLUBS"), Card(13, "HEARTS"), Card(13, "CLUBS"), Card(4,"SPADES")])

    print(tie_break(player, opp))