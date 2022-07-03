from lab import *
import numpy as np

if __name__ == "__main__":
    print(random_exp(1/15))

    queue = Queue(15, 3, lambda n: 64 - n**(1.5), lambda n: 5 + 3*n)
    queue.simulation(1000)
