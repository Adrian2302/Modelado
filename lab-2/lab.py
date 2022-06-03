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
        words_copy.append(repeated_decorator + words[i].lower() + repeated_decorator)
        
    return words_copy


def get_sequences(words, n):
    final_vector = []
    # Primero se iterar por cada palabra del vector
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