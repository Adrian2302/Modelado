#import random
import itertools
import time
import math
from poker import *

def good_abm(n):
    k = math.log(n,2)
    k = round(k) #Volverlo un numero entero
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

#Método de compare hands está en poker.py

def simulate(initial_cards: list[Card], rolls: int, generator):
    #Solo se pueden tener dos cartas
    if len(initial_cards) != 2:
        return (None, None, None)
    #Variables para generar los resultados
    win: float = 0
    lose: float = 0
    draw: float = 0
    #Cargar el maso de cartas
    deck: list[Card] = get_deck()
    #Ya vienen las cartas del jugador, entonces las quitamos del maso
    deck = remove_from_deck(deck, initial_cards)
    #Ciclo de n (rolls) simulaciones
    for i in range(rolls):
        #Se generan dos cartas aleatorias para el oponente
        opponent_hand = generate_random_hand(2, deck, generator)
        #Se quitan las cartas del oponente del deck
        deck = remove_from_deck(deck, opponent_hand)
        #Se generan las cartas de la mesa
        table_cards = generate_random_hand(5, deck, generator)
        deck = remove_from_deck(deck, table_cards)
        #Simulacion del juego
        p_best_hand = find_best_combination(table_cards, initial_cards)
        o_best_hand = find_best_combination(table_cards, opponent_hand)
        #Llevar score
        comparison = compare_hands(p_best_hand, o_best_hand)
        if comparison is not None:
            if comparison:
                win += 1
            else:
                lose += 1
        else: #Si es empate
            draw += 1
        #Se vuelven a colocar las cartas del oponente y de la mesa en el deck
        deck = deck + opponent_hand + table_cards
    #Fin de ciclo
    return (win/rolls, lose/rolls, draw/rolls)


def remove_from_deck(deck: list[Card], cards: list[Card]):
    for c in deck[:]:
        for i in cards[:]:
            if c.value == i.value and c.color == i.color:
                deck.remove(c)
    return deck

def find_best_combination(table_cards: list[Card], hand: list[Card]):
    all_cards = table_cards + hand
    # Se debe hacer un 7C5
    all_combs = itertools.combinations(all_cards, 5)
    # Se inicia la mejor mano como la primera
    combs_list = []
    for combinations in all_combs:
        combs_list.append(combinations)
    best_hand: list[Card] = combs_list[0]
    for comb in combs_list:
        if compare_hands(comb, best_hand):
            best_hand = comb
    return best_hand

def generate_random_hand(num_cards: int, deck: list[Card], generator):
    new_hand = []
    for i in range (0, num_cards):
        card = generator.random() * len(deck)
        card = round(card) - 1
        if card <= -1:
            card = 0
        while deck[card] in new_hand:
            card = generator.random() * len(deck)
            card = round(card) - 1
            if card <= -1:
                card = 0
        new_hand.append(deck[card])
    return new_hand

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
        return xi/m

    def period(self):
        a = self.get_a()
        b = self.get_b()
        m = self.get_m()
        x = 0

        exists = False
        count = 1

        while exists == False:
            x = (a * x + b) % m
            if x == 0:
                exists = True
            else:
                count = count + 1
        return count