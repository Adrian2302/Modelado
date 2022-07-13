from lab import *
from poker import *

if __name__ == "__main__":
    # Parte 5
    # a)
    values = good_abm(10000001)
    generator = CongruentialGenerator(values[0], values[1], values[2])

    # b)
    period = generator.period()
    print(values[2], period)

    # c)
    # i.
    card = Card(1, "SPADES")
    card2 = Card(1, "CLUBS")
    wins, loses, draws = simulate([card,card2], 100000, generator)
    print(wins, loses, draws)
    # ii.
    values = good_abm(10000001)
    generator = CongruentialGenerator(values[0], values[1], values[2])
    card = Card(2, "SPADES")
    card2 = Card(2, "CLUBS")
    wins, loses, draws = simulate([card,card2], 100000, generator)
    print(wins, loses, draws)
    # iii.
    values = good_abm(10000001)
    generator = CongruentialGenerator(values[0], values[1], values[2])
    card = Card(2, "SPADES")
    card2 = Card(7, "CLUBS")
    wins, loses, draws = simulate([card,card2], 100000, generator)
    print(wins, loses, draws)