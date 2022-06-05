from lab import *

if __name__ == "__main__":

    words = load_words("test.txt")
    words2 = add_decorators(words, "$", 2)
    print(words2)

    print(get_sequences(words2, 2))
