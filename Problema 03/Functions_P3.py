import csv # Para criar e manipular arquivos .csv.

def manipularCSV_ComLista(nome_arquivo, operacao, encoding, lista):
    # Vai escrever uma determinada lista na última linha do arquivo .csv.
    if operacao == 'append':
        if encoding == False:
            with open(nome_arquivo, 'a') as file:
                csv.writer(file).writerow(lista)
        elif encoding == 'utf8':
            with open(nome_arquivo, 'a', encoding='utf8') as file:
                csv.writer(file).writerow(lista)
    
    # Vai criar ou recriar o arquivo .csv.
    elif operacao == 'write':
        if encoding == False:
            with open(nome_arquivo, 'w') as file:
                csv.writer(file).writerow(lista)
        elif encoding == 'utf8':
            with open(nome_arquivo, 'w', encoding='utf8') as file:
                csv.writer(file).writerow(lista)
    
    # Vai copiar os dados do arquivo .csv para uma lista.
    elif operacao == 'copy_to_list':
        if encoding == False:
            with open(nome_arquivo, 'r') as file:
                lista_completa = []
                for linhas in csv.reader(file):
                    if linhas:
                        coluna = []
                        for colunas in linhas:
                            coluna.append(colunas)
                        lista_completa.append(coluna)
        elif encoding == 'utf8':
            with open(nome_arquivo, 'r', encoding='utf8') as file:
                lista_completa = []
                for linhas in csv.reader(file):
                    if linhas:
                        coluna = []
                        for colunas in linhas:
                            coluna.append(colunas)
                        lista_completa.append(coluna)
        return lista_completa

def verificacoesCSV(nome_arquivo, operacao):
    # Vai verificar se o arquivo .csv existe
    # e retornar um valor booleano.
    if operacao == 'existe':
        try:
            file = open(nome_arquivo)
            file.close
            return True        
        except FileNotFoundError:
            return False

def verificarNumerosNaString(string):
    # Vai verificar se o usuário colocou números em alguma string
    # que só poderia ser formada de letras.
    for letra in range(len(string)):
        try:
            assert string[letra].isdigit() == False
        except AssertionError:
            return True
    return False