#/*******************************************************************************
# Autor: José Victor de Oliveira Correia
# Componente Curricular: Algoritmos I
# Concluido em: **/05/2021
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

# Gerenciador de Manutenções da empresa do Seu Marcos.

import keyboard
import datetime # Para trabalhar com datas.
from time import sleep # Para dar um delay entre a execução das linhas de código.
import os # Para limpar o terminal.
import csv # Para criar e manipular arquivos .csv.
import platform # Vai verificar se o sistema é "Windows" ou "Linux" para criação dos diretórios.
import Functions_P3 # Onde estão as modularizações pessoais deste programa.

# Vai verificar qual o sistema operacional
# e criar os endereços para os diretórios dos arquivos.
sistema_operacional = platform.system()
if sistema_operacional == 'Windows':
    pasta_files = '.\Files'
    caminho_clientes = 'Files\Clientes.csv'
elif sistema_operacional == 'Linux':
    pasta_files = './Files'
    caminho_clientes = 'Files/Clientes.csv'

# Verificar se os arquivos já existem...
# Se não, eles serão criados e formatados!
if os.path.exists('Files') == False: # Vai verificar se a pasta "Files" já existe.
    os.makedirs(pasta_files) # Se não existir, será criada.
TemArquivoClientes = Functions_P3.verificacoesCSV(caminho_clientes, 'existe')
if TemArquivoClientes == True:
    pass
elif TemArquivoClientes == False:
    EstruturaCSV = ['Código do Cliente','Nome', 'Rua', 'Número da Casa',
                    'Estado', 'Cidade', 'Bairro', 'CEP', 'Nº de Telefone']
    Functions_P3.manipularCSV_ComLista(caminho_clientes, 'write', 'utf8', EstruturaCSV)

on_menu = True # Vai permitir a entrada no menu principal.
               # "True" > Entrar | "False" > Sair
while on_menu == True:
    os.system('cls')
    print("\nGerenciador de Manutenções\n"
    "\n1. Operações com clientes.\n"
    "2. Operações com manutenções.\n"
    "3. Verificar todos os dados.\n"
    "4. Sair.\n"
    )
    try:
        start_menu_options = int(input("Sua escolha: "))
    # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
    except ValueError:
        start_menu_options = 7 # O programa vai cair na condição de opção inválida!
    
    if start_menu_options == 1:
        on_menu_clientes = True # Vai permitir a entrada no sub-menu dos clientes.
                                # "True" > Entrar | "False" > Sair
        while on_menu_clientes == True:
            os.system('cls')
            print("\nOperações com Clientes\n"
            "\n1. Incluir novo cliente.\n"
            "2. Editar dados de um cliente.\n"
            "3. Excluir cliente.\n"
            "4. Ver a lista de clientes.\n"
            "5. Voltar ao menu principal.\n"
            "6. Sair do programa.\n"
            )
            try:
                menu_clientes_options = int(input("Sua escolha: "))
            # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
            except ValueError:
                menu_clientes_options = 6  # O programa vai cair na condição de opção inválida!
            
            # Vai entrar no sub-menu de cadastrar um novo cliente.
            if menu_clientes_options == 1:
                os.system('cls') # Vai limpar o terminal.

                # Vai copiar o código do último cliente.
                # Se não existirem clientes, o código do último será '0'. 
                # Para isso, o algoritmo vai copiar os dados do arquivo .csv para uma lista.
                with open(caminho_clientes) as file:
                    lista_clientes = []
                    for cliente in csv.reader(file):
                        if cliente:
                            informacoes_cliente = []
                            for informacao in cliente:
                                informacoes_cliente.append(informacao)
                            lista_clientes.append(informacoes_cliente)
                    # Vai copiar o código do último cliente para uma variável.
                    try:
                        ultimo_cliente = int(lista_clientes[len(lista_clientes)-1][0])
                    # Vai dar erro se não houver algum cliente, pois a lista irá retornar a string 'Código do Cliente',
                    # e não o número inteiro do código do cliente.
                    except ValueError: 
                        ultimo_cliente = 0

                # Vai criar a lista onde os dados do novo cliente serão inseridos,
                # definir o ID de usuário, tendo como base o ID do último cliente
                # com um incremento de +1, e registrar algumas informações pessoais dele.
                novo_cliente = []
                novo_cliente.append(ultimo_cliente+1)
                while True:
                    novo_cliente.append(str(input('Digite o nome do cliente: ')))
                    texto = novo_cliente[1]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                    if tem_numeros == True:
                        novo_cliente.pop(1)
                        os.system('cls')
                        print('Digite apenas letras!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                    else:
                        break
                while True:
                    novo_cliente.append(str(input('Rua: ')))
                    texto = novo_cliente[2]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                    if tem_numeros == True:
                        novo_cliente.pop(2)
                        os.system('cls')
                        print('Digite apenas letras!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                    else:
                        break
                while True:
                    try:
                        novo_cliente.append(int(input('Número da Casa: ')))
                        break
                    except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                        os.system('cls')
                        print('Digite apenas números inteiros!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                while True:
                    novo_cliente.append(str(input('Estado: ')))
                    texto = novo_cliente[4]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                    if tem_numeros == True:
                        novo_cliente.pop(4)
                        os.system('cls')
                        print('Digite apenas letras!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                    else:
                        break
                while True:
                    novo_cliente.append(str(input('Cidade: ')))
                    texto = novo_cliente[5]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                    if tem_numeros == True:
                        novo_cliente.pop(5)
                        os.system('cls')
                        print('Digite apenas letras!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                    else:
                        break               
                while True:
                    novo_cliente.append(str(input('Bairro: ')))
                    texto = novo_cliente[6]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                    if tem_numeros == True:
                        novo_cliente.pop(6)
                        os.system('cls')
                        print('Digite apenas letras!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                    else:
                        break
                while True:
                    try:
                        novo_cliente.append(int(input('CEP (Apenas números, sem formatação!): ')))
                        break
                    except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                        os.system('cls')
                        print('Digite apenas números inteiros!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                while True:
                    try:
                        novo_cliente.append(int(input('Telefone do cliente (Apenas números, sem formatação!): ')))
                        break
                    except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                        os.system('cls')
                        print('Digite apenas números inteiros!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')

                # Fase de registro das informações da lista no arquivo 'Clientes.csv'.
                Functions_P3.manipularCSV_ComLista(caminho_clientes, 'append', 'utf8', novo_cliente)

                # Voltando para o menu principal, após registrar o(a) cliente.
                os.system('cls')
                print('Cliente registrado com sucesso!')
                print('\nVoltando ao menu principal...')
                on_menu_clientes = False
                sleep(2) # Vai esperar dois segundos até prosseguir.

            elif menu_clientes_options == 2:
                print('b')
            
            elif menu_clientes_options == 3:
                print('c')
            
            elif menu_clientes_options == 4:
                with open(caminho_clientes, 'r', encoding='utf8') as file:
                    lista_clientes = []
                    for cliente in csv.reader(file):
                        if cliente:
                            informacoes_cliente = []
                            for informacao in cliente:
                                informacoes_cliente.append(informacao)
                            lista_clientes.append(informacoes_cliente)
                
                os.system('cls')
                print('\nLista de clientes:\n\n')
                for cliente in range(1, len(lista_clientes)):
                        print(f'ID: {lista_clientes[cliente][0]}\n')
                        print(f'Nome: {lista_clientes[cliente][1]}\n')
                        print(f'Endereço do cliente:\nRua: {lista_clientes[cliente][2]},'
                                f' Nº: {lista_clientes[cliente][3]},'
                                f' Estado: {lista_clientes[cliente][4]},'
                                f' Cidade: {lista_clientes[cliente][5]},'
                                f' Bairro: {lista_clientes[cliente][6]},'
                                f' CEP: {lista_clientes[cliente][7]}\n')
                        print(f'Telefone: {lista_clientes[cliente][8]}\n')
                        print('\n')
                
                print('Pressione a tecla "Espaço" no teclado, para prosseguir.')
                keyboard.wait('space')
            
            elif menu_clientes_options == 5:
                os.system('cls')
                print("\nVoltando ao Menu Principal!\n")
                on_menu_clientes = False
                sleep(2) # Vai esperar dois segundos até prosseguir.
            
            # Vai sair do programa, se a opção "6" for selecionada.
            elif menu_clientes_options == 6:
                os.system('cls')
                print("\nAté mais!\n")
                on_menu_clientes = False
                on_menu = False
                sleep(2) # Vai esperar dois segundos até prosseguir.
            
            # Vai entrar nessa condição, se uma opção inválida for digitada no menu.
            else:
                os.system('cls')
                print('\nEssa opção não existe!\n')
                sleep(2) # Vai esperar dois segundos até voltar ao menu.

    elif start_menu_options == 2:
        on_menu_manutencoes = True # Vai permitir a entrada no sub-menu das manutenções.
                                # "True" > Entrar | "False" > Sair
        while on_menu_manutencoes == True:
            os.system('cls')
            print("Operações com Manutenções\n"
            "\n1. Agendar manutenção.\n"
            "2. Editar manutenção.\n"
            "3. Excluir manutenção.\n"
            "4. Realizar manutenção.\n"
            "5. Ver a lista de manutenções.\n"
            "6. Imprimir lista de manutenções.\n"
            "7. Voltar ao menu principal.\n"
            )
            try:
                menu_manutencoes_options = int(input("Sua escolha: "))
            # Irá tratar os erros, caso o usuário digite uma letra ou nada neste sub-menu.
            except (TypeError, ValueError):
                os.system('cls')
                print(
                    "\nOpção Inválida!\n"
                )
                sleep(2)
                os.system('cls')

            if menu_manutencoes_options == 1:
                print('a')
            elif menu_manutencoes_options == 2:
                print('b')
            elif menu_manutencoes_options == 3:
                print('c')
            elif menu_manutencoes_options == 4:
                print('d')
            elif menu_manutencoes_options == 5:
                print('e')
            elif menu_manutencoes_options == 6:
                print('f')
            elif menu_manutencoes_options == 7:
                os.system('cls')
                print("\nVoltando ao Menu Principal!")
                sleep(2)
                on_menu_manutencoes = False
    
    elif start_menu_options == 3:
        print('c')
    
    # Vai sair do programa, se a opção "4" for selecionada.
    elif start_menu_options == 4:
        os.system('cls')
        print("\nAté mais!\n")
        on_menu = False
        sleep(2) # Vai esperar dois segundos até prosseguir.

    # Vai entrar nessa condição, se uma opção inválida for digitada no menu.
    else:
        os.system('cls')
        print('\nEssa opção não existe!\n')
        sleep(2) # Vai esperar dois segundos até voltar ao menu.