import random
import math
def random_exp(lambd):
    random_number = random.uniform(0, 1)
    return - math.log(1 - random_number)/lambd