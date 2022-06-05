import csv


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
    print("Words:", words)
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

    for s in range(seq_length):
        print(f"--- {sequences[s]} ---")
        print(f'dict: {dict_list[s]}\n\n')
    # Ver las ocurrencias que le siguen a cada secuencia y cuantas veces aparecieron. A partir de estos números se saca la probabilidad para ir a llenar la matriz
    for r in range(seq_length):
        count = sum(dict_list[r].values())
        for c in range(seq_length):
            if sequences[c] in dict_list[r].keys():
                prob_matrix[r][c] = dict_list[r][sequences[c]] / count
            else:
                prob_matrix[r][c] = 0

    return prob_matrix
