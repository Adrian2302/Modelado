from lab import *
import random

if __name__ == "__main__":

    words = load_words("pokemon.csv")

    #6
    model1 = create_model(words, 1)
    model2 = create_model(words, 2)
    model3 = create_model(words, 3)

    word1 = generate_word(model1, 17)
    word2 = generate_word(model2, 42)
    word3 = generate_word(model3, 21)

    print("model(n=1), seed=17", word1)
    print("model(n=2), seed=42", word2)
    print("model(n=3), seed=21", word3)

    #7
    word = "MEW"
    result = get_probability(model1, word)
    result2 = get_probability(model2, word)
    result3 = get_probability(model3, word)

    print(result)
    print(result2)
    print(result3, '\n')

    """

    a.  La probabilidad de formar un nombre parece aumentar conforme n incrementa porque entre más grande la n,
        el modelo va a tener aún más entrenamiento, lo que va a generar una mayor precisión en las respuestas.
    
    """

    """
    
    b.
        1.

        2.  Con la n=1 y la semilla=3828 el programa genera el nombre sshalitrglef
    
    """
    model_Question_8b = create_model(words, 1)
    word_Question_8b = generate_word(model_Question_8b, 3828)
    print("model(n=1), seed=3828", word_Question_8b)
    result_Question_8b = get_probability(model_Question_8b, word_Question_8b)
    print(result_Question_8b)

    """

    c.  Las cadenas de Markov están siendo utilizadas para modelas los nombres cuando se crea la ·······
    
    """
