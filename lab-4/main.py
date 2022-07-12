from lab import *
from poker import *

if __name__ == "__main__":
    '''
    values = good_abm(16)

    generator = CongruentialGenerator(values[0], values[1], values[2])

    period = generator.period()

    print(values, period)
    '''
    '''
    player = []
    opponent = []
    for i in range(2):
        player.append(Card(1+i,'S'))
        opponent.append(Card(1+i,'S'))
    for i in range(2):
        player.append(Card(4+i,'C'))
        opponent.append(Card(4+i,'C'))
    player.append(Card(14,'S'))
    opponent.append(Card(13,'S'))
    
    print(compare_hands(player, opponent))
    '''
    '''
    values = good_abm(10000001)
    generator = CongruentialGenerator(3,2,34)
    period = generator.period()
    print(values[0], values[1], values[2])
    print(period)
    '''
    # Parte 5

    # a)
    values = good_abm(10000001)
    generator = CongruentialGenerator(values[0], values[1], values[2])

    # b)
    period = generator.period()
    print(values[2], period)

    # c)
    # i.
    card = Card(13, "SPADES")
    card2 = Card(13, "CLUBS")
    simulate([card,card2], 100000, generator)

    # ii.

    # iii.