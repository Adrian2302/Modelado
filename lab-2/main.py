from lab import *

if __name__ == "__main__":

    words = load_words("pokemon.csv")
    words2 = add_decorators(words, "$", 2)

    #print(words)
    #print("AAAAAAAAAAAA")
    print(words2)

    get_sequences(words2, 2)