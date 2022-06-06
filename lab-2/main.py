from lab import *

if __name__ == "__main__":

    words = load_words("test.txt")
    results = create_model(words, 1)
    #print(results)

    for r in range(len(results[0])):
        print(r, results[1][r], results[0][r])
    generate_word(results, 1)