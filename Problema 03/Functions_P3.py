import csv

def manipularCSV_ComLista(nome_arquivo, operacao, encoding, lista):

    # Vai escrever uma determinada lista na última linha do arquivo .csv.
    if operacao == 'append':
        if encoding == False:
            with open(nome_arquivo, 'a') as file:
                csv.writer(file).writerow(lista)
        elif encoding == 'utf8':
            with open(nome_arquivo, 'a', encoding='utf8') as file:
                csv.writer(file).writerow(lista)
    
    # Vai criar/recriar o arquivo .csv.
    elif operacao == 'write':
        if encoding == False:
            with open(nome_arquivo, 'w') as file:
                csv.writer(file).writerow(lista)
        elif encoding == 'utf8':
            with open(nome_arquivo, 'w', encoding='utf8') as file:
                csv.writer(file).writerow(lista)

def verificacoesCSV(nome_arquivo, operacao):

    # Vai verificar se o arquivo .csv existe.
    if operacao == 'existe':
        try:
            file = open(nome_arquivo)
            file.close
            return True        
        except FileNotFoundError:
            return False

def verificarNumerosNaString(string):
    for letra in range(len(string)):
        try:
            assert string[letra].isdigit() == False
        except AssertionError:
            return True
    return False