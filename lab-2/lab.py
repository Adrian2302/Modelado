import csv
import random
import numpy as np


def load_words(filename):
    words = []

    with open(filename) as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            words.append(row[0])

    return words


def add_decorators(words, decorator, n):
    words_copy = []
    repeated_decorator = decorator*n
    # Para cada palabra en el vector words se pone en minuscula y se le agregan los decoradores
    for i in range(len(words)):
        words_copy.append(repeated_decorator +
                          words[i].lower() + repeated_decorator)

    return words_copy


def get_sequences(words, n):
    final_vector = []
    # Primero se itera por cada palabra del vector
    for word in words:
        counter = 0
        # Luego desde cada letra de la palabra, vamos sacando n letras
        while(counter < len(word)):
            result = ""
            for i in range(n):
                if(counter+n <= len(word)):
                    result = result + word[counter+i]
            # Se agrega al vector de resultados
            if result not in final_vector and result != "":
                final_vector.append(result)
            counter = counter+1
    final_vector = sorted(final_vector)
    return final_vector


def calculate_transitions(words, sequences):
    seq_length = len(sequences)
    # inicializar matriz y diccionario
    prob_matrix = [[0 for _ in range(seq_length)] for _ in range(seq_length)]
    dict_list = {}
    for s in range(len(sequences)):
        dict_list[sequences[s]] = {}
    # por cada secuencia, iterar por cada palabra buscando la secuencia que le sigue y agregarla a su respectivo diccionario
    for w in words:
        index = 0
        jump_size = len(sequences[0])
        while index < len(w)-jump_size:
            current_seq = w[index:index+jump_size]
            next_seq = w[index+1:index+1+jump_size]
            if next_seq not in dict_list[current_seq].keys():
                dict_list[current_seq][next_seq] = 1
            else:
                dict_list[current_seq][next_seq] += 1
            index += 1
    # Ver las ocurrencias que le siguen a cada secuencia y cuantas veces aparecieron. A partir de estos números se saca la probabilidad para ir a llenar la matriz
    for s in range(seq_length):
        count = sum(dict_list[sequences[s]].values())
        for c in range(seq_length):
            if sequences[c] in dict_list[sequences[s]].keys():
                prob_matrix[s][c] = dict_list[sequences[s]
                                              ][sequences[c]] / count
            else:
                prob_matrix[s][c] = 0

    return prob_matrix


def create_model(words, ngrams):
    decorated = add_decorators(words, "$", ngrams)
    sequences = get_sequences(decorated, ngrams)
    prob_matrix = calculate_transitions(decorated, sequences)
    return(prob_matrix, sequences)


def generate_word(model, seed):
    r = random.Random()
    r.seed(seed)

    prob_matrix = model[0]
    sequences = model[1]
    current_seq = 0
    built = False
    new_word = ""

    while not built:
        random_number = r.uniform(0, 1)
        for s in range(len(sequences)):
            if random_number < prob_matrix[current_seq][s]:
                if s == 0:
                    built = True
                else:
                    new_word += sequences[s][-1:]
                    current_seq = s
                break
            else:
                random_number -= prob_matrix[current_seq][s]
    return new_word.replace('$', '')


def get_probability(model, word):
    # setup
    prob_matrix = model[0]
    sequences = model[1]
    word = sequences[0] + word.lower() + sequences[0]
    seq_size = len(sequences[0])
    seq_index_dict = {}
    for s in range(len(sequences)):
        seq_index_dict[sequences[s]] = s
    # se inicializa la probabilidad y despues se va iterando en la matriz hasta llegar a la palabra
    probability = 1
    index = 0
    while index < len(word)-seq_size:
        current_seq = word[index:index + seq_size]
        next_seq = word[(index+1):(index+1) + seq_size]
        current_seq_index = seq_index_dict[current_seq]
        next_seq_index = seq_index_dict[next_seq]
        probability = probability * \
            prob_matrix[current_seq_index][next_seq_index]
        index += 1
    return probability
