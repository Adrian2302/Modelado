from lab import *
import random

if __name__ == "__main__":

    words = load_words("pokemon.csv")

    model1 = create_model(words, 1)
    model2 = create_model(words, 2)
    model3 = create_model(words, 3)

    # word1 = generate_word(model1, 17)
    # word2 = generate_word(model2, 42)
    # word3 = generate_word(model3, 21)

    # print("model(n=1), seed=17", word1)
    # print("model(n=2), seed=42", word2)
    # print("model(n=3), seed=21", word3)

    word = "MEW"
    result = get_probability(model1, word)
    result2 = get_probability(model2, word)
    result3 = get_probability(model3, word)

    print(result)
    print(result2)
    print(result3)
