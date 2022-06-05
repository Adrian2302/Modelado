from lab import *

if __name__ == "__main__":

    words = load_words("test.txt")
    decorated = add_decorators(words, "$", 2)
    sequences = get_sequences(decorated, 2)
    prob_matrix = calculate_transitions(decorated, sequences)

    for r in range(len(prob_matrix)):
        print(prob_matrix[r])
