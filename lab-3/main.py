from lab import *
import numpy as np

if __name__ == "__main__":
    queue = Queue(15, 3, lambda n: 64 - n**(1.5), lambda n: 5 + 3*n)
    queue.simulation(1000)
    print('\n')
    queue = Queue(15, 3, lambda n: 64 - n**(1.5), lambda n: 5 + 3*n)
    queue.simulation(1000)
    print('\n')
    queue = Queue(15, 3, lambda n: 64 - n**(1.5), lambda n: 5 + 3*n)
    queue.simulation(1000)
