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
    card = Card(13, "SPADES")
    card2 = Card(13, "CLUBS")
    wins, loses, draws = simulate([card,card2], 100000, generator)
    print(wins, loses, draws)
    # ii.

    # iii.