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
    dict_list = [{} for _ in range(seq_length)]
    # por cada secuencia, iterar por cada palabra buscando la secuencia que le sigue y agregarla a su respectivo diccionario
    seq_index = 0
    for s in sequences:
        for w in words:
            index = 0
            jump_size = len(s)
            while index < len(w):
                current_seq = w[index:index+jump_size]
                next_seq = w[index+jump_size:index+2*jump_size]
                if current_seq == s and next_seq != '':
                    if next_seq not in dict_list[seq_index].keys():
                        dict_list[seq_index][next_seq] = 1
                    else:
                        dict_list[seq_index][next_seq] += 1
                index += 1
        seq_index += 1

    # Ver las ocurrencias que le siguen a cada secuencia y cuantas veces aparecieron. A partir de estos números se saca la probabilidad para ir a llenar la matriz
    for r in range(seq_length):
        count = sum(dict_list[r].values())
        for c in range(seq_length):
            if sequences[c] in dict_list[r].keys():
                prob_matrix[r][c] = dict_list[r][sequences[c]] / count
            else:
                prob_matrix[r][c] = 0

    return prob_matrix


def create_model(words, ngrams):
    decorated = add_decorators(words, "$", ngrams)
    sequences = get_sequences(decorated, ngrams)
    prob_matrix = calculate_transitions(decorated, sequences)

    return(prob_matrix, sequences)


def generate_word(model, seed):
    r = random.Random()
    r.seed(seed)
    row = 0
    finish = False
    new_word = ""

    while finish == False:
        random_number = r.uniform(0, 1)
        found = False
        prob_dict = {}
        sum = 0
        for column in range(len(model[0][row])):
            if model[0][row][column] != 0:
                sum = sum + model[0][row][column]
                prob_dict[column] = sum
        for key in prob_dict:
            if(random_number <= prob_dict[key] and found == False):
                found = True
                row = key
                new_word = new_word + model[1][key]
        if bool(prob_dict) == False or row == 0:
            finish = True

    return new_word
