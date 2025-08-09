#Recebe o arquivo de texto e tranforma em uma string
def get_book_text(path_to_file):
    with open(path_to_file) as text:
        file_contents = text.read()
        #Retorna o arquivo em string
        return file_contents

#Separa as palavras do texto e transforma em lista
def get_book_words(path_to_file):
    book_text = get_book_text(path_to_file)
    #Conta e armazena quantas palavras tem no texto
    number_of_words = len(book_text.split())
    #Retorna o numero de palavras na string
    return number_of_words

#Conta a quantidade de cada char no texto
def get_book_chars(path_to_file):
    book_text = get_book_text(path_to_file)
    dictionary = {}
    #deixa o texto em letra minuscula e retira os espaços
    lower_text = book_text.lower()
    ready_text = "".join(lower_text.split())

    #Analisa char por char e conta
    for character in ready_text:
        if character.isalpha():
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
    
    return dictionary

#retorna uma lista ordenada de dicionários
def list_of_dictionary(dictionary):
    
    list_dictionary = []
    #Cria uma lista de dicionários
    for character, quant in dictionary.items():
        temp_dictionary = {"char" : character, "num" : quant}

        list_dictionary.append(temp_dictionary)
    
    def sort_on(items):
        return items["num"]
    
    list_dictionary.sort(reverse=True, key=sort_on)

    return list_dictionary