from lab import *

if __name__ == "__main__":

    words = load_words("test.txt")
    results = create_model(words, 2)
    print(results[1])

    #for r in range(len(prob_matrix)):
    #    print(prob_matrix[r])
