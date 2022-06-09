from lab import *
import random

'''
B93825 Adrián Hernández Young
B92277 Rodrigo Contreras Araya

Pregunta 8
a.  Esto se da porque se conforman relaciones entre secuencias de varios
    caracteres, lo que crea secuencias que se asemejan más a los nombres
    de los pokemones.
b.  Con n = 3 y semilla de 42069 se genera la palabra "star"
c.  Las cadenas de Markov se están utilizando para modelar los nombres
    cuando se sacan las probabilidades de que una secuencia siga a otra,
    pues dependen únicamente de la secuencia anterior. La matriz de
    probabilidades contiene dichas relaciones, donde se encuentra
    la probabilidad de que Y secuencia siga dada X secuencia.
'''

if __name__ == "__main__":

    words = load_words("pokemon.csv")

    model1 = create_model(words, 1)
    model2 = create_model(words, 2)
    model3 = create_model(words, 3)

    word1 = generate_word(model1, 17)
    word2 = generate_word(model2, 42)
    word3 = generate_word(model3, 21)
    word4 = generate_word(model3, 42069)

    print("model(n=1), seed=17", word1)
    print("model(n=2), seed=42", word2)
    print("model(n=3), seed=21", word3)

    word = "MEW"
    result = get_probability(model1, word)
    result2 = get_probability(model2, word)
    result3 = get_probability(model3, word)

    print(result)
    print(result2)
    print(result3)
    print("\nPregunta 8: model(n=3), seed=42069, palabra: ", word4)
