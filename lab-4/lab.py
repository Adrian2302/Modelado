import time
import random
import numpy as np
import math


def good_abm(n):
    k = math.log(n,2)

    k = round(k) #V olverlo un numero entero

    m = 2 ** (k+1) # m = 2^k

    a = 4 * n + 1 # a = 4*c + 1

    b = n
    while checkOdd(b) == False: # Primer numero primo a partir de n
        b = b + 1

    return(a, b, m)
                
def checkOdd(n):
    found = True
    if n % 2 == 0:
        found = False
    return found

class CongruentialGenerator():
    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m
        self.x = round(time.time() * 1000)

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_m(self):
        return self.m

    def get_x(self):
        return self.x

    def seed(self, s):
        self.x = s

    def random(self):
        a = self.get_a()
        b = self.get_b()
        m = self.get_m()
        x = self.get_x()

        xi = (a * x + b) % m
        self.seed(xi)
        #print(xi/m)
        return xi/m

    def period(self):
        values = []
        exists = False
        count = 0

        while exists == False:
            x = self.random()
            if x in values:
                exists = True
            else:
                values.append(x)
                count = count + 1
        #print(count)
        return count




