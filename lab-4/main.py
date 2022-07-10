from lab import *

if __name__ == "__main__":

    values = good_abm(16)

    generator = CongruentialGenerator(values[0], values[1], values[2])

    period = generator.period()

    print(values, period)