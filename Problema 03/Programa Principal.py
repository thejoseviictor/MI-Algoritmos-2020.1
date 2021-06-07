#/*******************************************************************************
# Autor: José Victor de Oliveira Correia
# Componente Curricular: Algoritmos I
# Concluido em: 06/06/2021
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

# Gerenciador de Manutenções da empresa do Seu Marcos.

import keyboard # Para pausar o programa até que o usuário pressione alguma tecla.
import datetime # Para agendar uma manutenção automática.
from time import sleep # Para dar um delay entre a execução das linhas de código.
import os # Para limpar o terminal.
import csv # Para criar e manipular arquivos .csv.
import platform # Vai verificar se o sistema é "Windows" ou "Linux" para criação dos diretórios.
from sys import exit # Para finalizar o programa.
import Functions_P3 # Onde estão as modularizações pessoais deste programa.

# Vai verificar qual o sistema operacional
# e criar os endereços para os diretórios dos arquivos
# de acordo com cada sistema.
sistema_operacional = platform.system()
if sistema_operacional == 'Windows':
    pasta_program_files = '.\Program Files'
    pasta_user_files = '.\Arquivos do Usuário'
    caminho_clientes = 'Program Files\Clientes.csv'
    caminho_manutencoes_agendadas = 'Program Files\Manutenções_Agendadas.csv'
    caminho_manutencoes_realizadas = 'Program Files\Manutenções_Realizadas.csv'
elif sistema_operacional == 'Linux':
    pasta_program_files = './Program Files'
    pasta_user_files = './Arquivos do Usuário'
    caminho_clientes = 'Files/Clientes.csv'
    caminho_manutencoes_agendadas = 'Program Files/Manutenções_Agendadas.csv'
    caminho_manutencoes_realizadas = 'Program Files/Manutenções_Realizadas.csv'

# Verificar se os arquivos já existem...
# Se não, eles serão criados e formatados!
if os.path.exists('Program Files') == False: # Vai verificar se a pasta "Program Files" já existe.
    os.makedirs(pasta_program_files) # Se não existir, será criada.
if os.path.exists('Arquivos do Usuário') == False: # Vai verificar se a pasta "Arquivos do Usuário" já existe.
    os.makedirs(pasta_user_files) # Se não existir, será criada.
# Vai verificar se os arquivos "Clientes.csv", "Manutenções_Agendadas.csv" e "Manutenções_Realizadas.csv"
# existem... se não existirem, serão criados e formatados!
TemArquivoClientes = Functions_P3.verificacoesCSV(caminho_clientes, 'existe') 
TemArquivoManutencoesAgendadas = Functions_P3.verificacoesCSV(caminho_manutencoes_agendadas, 'existe')
TemArquivoManutencoesRealizadas = Functions_P3.verificacoesCSV(caminho_manutencoes_realizadas, 'existe')
if TemArquivoClientes == True:
    pass
elif TemArquivoClientes == False:
    EstruturaCSV = ['Código do Cliente','Nome', 'Rua', 'Número da Casa',
                    'Estado', 'Cidade', 'Bairro', 'CEP', 'Nº de Telefone']
    Functions_P3.manipularCSV_ComLista(caminho_clientes, 'write', 'utf8', EstruturaCSV)
if TemArquivoManutencoesAgendadas == True:
    pass
elif TemArquivoManutencoesAgendadas == False:
    EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                    'Nome da Peça', 'Tipo de Validade', 'Validade da Peça', 'Data para a Manutenção - DD/MM/AAAA']
    Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
if TemArquivoManutencoesRealizadas == True:
    pass
elif TemArquivoManutencoesRealizadas == False:
    EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                    'Nome da Peça', 'Tipo de Validade', 'Validade da Peça', 'Data de Conclusão da Manutenção - DD/MM/AAAA']
    Functions_P3.manipularCSV_ComLista(caminho_manutencoes_realizadas, 'write', 'utf8', EstruturaCSV)

# Bloco do programa principal:
on_menu = True # Vai permitir a entrada no loop do menu principal.
               # "True" > Entrar | "False" > Sair
while on_menu == True:
    # Vai copiar todos dados dos arquivos "Clientes.csv", "Manutenções_Agendadas.csv" e "Manutenções_Realizadas.csv"
    # para listas, fazendo com que eles possam ser manipulados.
    # E, também, atualizá-los sempre que voltar ao topo deste loop.
    lista_clientes = Functions_P3.manipularCSV_ComLista(caminho_clientes, 'copy_to_list', 'utf8', '')
    lista_manutencoes_agendadas = Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'copy_to_list', 'utf8', '')
    lista_manutencoes_realizadas = Functions_P3.manipularCSV_ComLista(caminho_manutencoes_realizadas, 'copy_to_list', 'utf8', '')

    os.system('cls') # Vai limpar o terminal.
    try:
        start_menu_options = int(input("\nGerenciador de Manutenções\n"
                                       "\n1. Operações com clientes.\n"
                                       "2. Operações com manutenções.\n"
                                       "3. Balanço do mês.\n"
                                       "4. Sair.\n"
                                       "\nSua escolha: "))
    # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
    except ValueError:
        start_menu_options = 7 # O programa vai cair na condição de opção inválida!
    
    # Sub-menu onde serão efetuadas operações que estão relacionadas especificamente
    # aos clientes e ao arquivo "Clientes.csv".
    if start_menu_options == 1:
        on_menu_clientes = True # Vai permitir a entrada no loop do sub-menu dos clientes.
                                # "True" > Entrar | "False" > Sair
        while on_menu_clientes == True:
            os.system('cls') # Vai limpar o terminal.
            try:
                menu_clientes_options = int(input("\nOperações com Clientes\n"
                                                  "\n1. Incluir novo cliente.\n"
                                                  "2. Editar dados de um cliente.\n"
                                                  "3. Excluir cliente.\n"
                                                  "4. Ver a lista de clientes.\n"
                                                  "5. Voltar ao menu principal.\n"
                                                  "6. Sair do programa.\n"
                                                  "\nSua escolha: "))
            # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
            except ValueError:
                menu_clientes_options = 6  # O programa vai cair na condição de opção inválida!
            
            # Vai entrar no sub-menu de cadastrar um novo cliente.
            if menu_clientes_options == 1:
                # Vai copiar o código do último cliente.
                # Se não existirem clientes, o código do último será '0'.
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
                # Algumas dessas informações estão em loop, para impedir que números sejam
                # inseridos em uma string ou letras em uma variável de inteiros.
                os.system('cls') # Vai limpar o terminal.
                on_nome = True
                while on_nome == True:
                    novo_cliente.append(str(input('\nDigite o nome do cliente: ')))
                    texto = novo_cliente[1]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto) # Vai verificar se têm números na string.
                    if tem_numeros == True:
                        novo_cliente.pop(1) # Se tiver números, ela será removida da lista.
                        os.system('cls')
                        print('\nDigite apenas letras!\n')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                    else:
                        on_nome = False
                novo_cliente.append(str(input('Rua: '))) # Não está com tratamento de erros,
                                                         # pois devem existir ruas com números
                                                         # em seus respectivos nomes.
                on_numero_casa = True
                while on_numero_casa == True:
                    try:
                        novo_cliente.append(int(input('Número da Casa: ')))
                        on_numero_casa = False
                    except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                        os.system('cls')
                        print('Digite apenas números inteiros!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                        print('\n')
                on_estado = True
                while on_estado == True:
                    novo_cliente.append(str(input('Estado: ')))
                    texto = novo_cliente[4]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto) # Vai verificar se têm números na string.
                    if tem_numeros == True:
                        novo_cliente.pop(4) # Se tiver números, ela será removida da lista.
                        os.system('cls')
                        print('Digite apenas letras!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                        print('\n')
                    else:
                        on_estado = False
                on_cidade = True
                while on_cidade == True:
                    novo_cliente.append(str(input('Cidade: ')))
                    texto = novo_cliente[5]
                    tem_numeros = Functions_P3.verificarNumerosNaString(texto) # Vai verificar se têm números na string.
                    if tem_numeros == True:
                        novo_cliente.pop(5) # Se tiver números, ela será removida da lista.
                        os.system('cls')
                        print('Digite apenas letras!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                        print('\n')
                    else:
                        on_cidade = False             
                novo_cliente.append(str(input('Bairro: '))) # Não está com tratamento de erros,
                                                            # pois devem existir bairros com números
                                                            # em seus respectivos nomes.
                on_cep = True
                while on_cep == True:
                    try:
                        novo_cliente.append(int(input('CEP (Apenas números, sem formatação!): ')))
                        on_cep = False
                    except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                        os.system('cls')
                        print('Digite apenas números inteiros!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                        print('\n')
                on_telefone = True
                while on_telefone == True:
                    try:
                        novo_cliente.append(int(input('Telefone do cliente (Apenas números, sem formatação!): ')))
                        on_telefone = False
                    except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                        os.system('cls')
                        print('Digite apenas números inteiros!')
                        sleep(2) # Vai esperar dois segundos até prosseguir.
                        os.system('cls')
                        print('\n')

                # Fase de registro das informações da lista no arquivo "Clientes.csv".
                Functions_P3.manipularCSV_ComLista(caminho_clientes, 'append', 'utf8', novo_cliente)

                # Atualizando os dados da variável em memória.
                lista_clientes = Functions_P3.manipularCSV_ComLista(caminho_clientes, 'copy_to_list', 'utf8', '')

                # Voltando para o menu principal, após registrar o cliente.
                os.system('cls')
                print('\nCliente registrado com sucesso!\n')
                print(f'O código de usuário do cliente "{novo_cliente[1]}" é: {novo_cliente[0]}')
                print('\n\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.')
                keyboard.wait('space')
                on_menu_clientes = False

            # Vai entrar no sub-menu de editar dados de um determinado cliente através do seu ID.
            elif menu_clientes_options == 2:
                # Vai verificar se existem clientes cadastrados.
                try:
                    tem_clientes = int(lista_clientes[1][0])
                    tem_clientes = True
                except (IndexError, ValueError):
                    tem_clientes = False
                    os.system('cls')
                    print('\nAinda não há clientes cadastrados!\n')
                    sleep(2)

                # Vai continuar se já existir pelo menos um cliente cadastrado.
                if tem_clientes == True:
                    # Vai pedir o código do cliente.
                    # E tratar os erros, se forem digitadas letras, números decimais ou caracteres especiais.
                    on_id_cliente = True
                    while on_id_cliente == True:
                        try:
                            os.system('cls')
                            id_listagem = int(input('\nDigite o ID do cliente: '))
                            on_id_cliente = False
                        except ValueError:
                            os.system('cls')
                            print('\nDigite apenas números!\n')
                            sleep(2)
                    
                    # Vai verificar se o cliente existe,
                    # comparando o ID dele com os IDs disponíveis na lista.
                    cliente_existe = True
                    for linha_do_cliente in range(1, len(lista_clientes)):
                        if int(lista_clientes[linha_do_cliente][0]) == id_listagem:
                            cliente_existe = True
                            break
                        else:
                            cliente_existe = False
                    
                    # Se o cliente existir, o usuário irá prosseguir para o sub-menu
                    # de edição dos dados do cliente.
                    if cliente_existe == True:
                        on_menu_alterar_info = True
                        while on_menu_alterar_info == True:
                            os.system('cls') # Vai limpar o terminal.
                            try:
                                menu_alterar_options = int(input(f'\nQual informação do cliente "{lista_clientes[linha_do_cliente][1]}" você deseja alterar?\n'
                                                                '1. Nome.\n'
                                                                '2. Endereço.\n'
                                                                '3. Número de Telefone.\n'
                                                                '\n4. Voltar ao menu anterior.\n'
                                                                '\nSua escolha: '))
                                assert menu_alterar_options > 0 and menu_alterar_options < 5 # Vai verificar se a opção digitada existe.
                                on_menu_alterar_info = False
                            except (ValueError,AssertionError):
                                os.system('cls')
                                print('\nOpção inválida!\n')
                                sleep(2)

                        # Vai permitir a edição do nome do cliente na lista.
                        if menu_alterar_options == 1:
                            os.system('cls')
                            on_nome = True
                            while on_nome == True:
                                lista_clientes[linha_do_cliente][1] = str(input('\nDigite o novo nome do cliente: '))
                                texto = lista_clientes[linha_do_cliente][1]
                                tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                                if tem_numeros == True:
                                    os.system('cls')
                                    print('\nDigite apenas letras!\n')
                                    sleep(2) # Vai esperar dois segundos até prosseguir.
                                    os.system('cls')
                                else:
                                    on_nome = False
                            # Recriação e formatação do arquivo "Clientes.csv" com os dados alterados.
                            EstruturaCSV = ['Código do Cliente','Nome', 'Rua', 'Número da Casa',
                                            'Estado', 'Cidade', 'Bairro', 'CEP', 'Nº de Telefone']
                            Functions_P3.manipularCSV_ComLista(caminho_clientes, 'write', 'utf8', EstruturaCSV)
                            for clientes in range(1, len(lista_clientes)):
                                todas_informacoes_cliente = []
                                for informacoes_cliente in range(9):
                                    todas_informacoes_cliente.append(lista_clientes[clientes][informacoes_cliente])
                                Functions_P3.manipularCSV_ComLista(caminho_clientes, 'append', 'utf8', todas_informacoes_cliente)
                            
                            # Imprimindo mensagem de sucesso na edição e voltando ao menu anterior.
                            os.system('cls')
                            print(f'\nNome do cliente "{lista_clientes[linha_do_cliente][1]}" editado com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.')
                            on_menu_alterar_info = False
                            keyboard.wait('space') # Vai esperar o usuário pressionar a tecla "Espaço" para prosseguir.

                        # Vai permitir a edição do endereço do cliente.
                        elif menu_alterar_options == 2:
                            os.system('cls')
                            print(f'\nCadastrando novo endereço do cliente "{lista_clientes[linha_do_cliente][1]}"...\n')
                            lista_clientes[linha_do_cliente][2] = str(input('Rua: '))
                            on_numero_casa = True
                            while on_numero_casa == True:
                                try:
                                    lista_clientes[linha_do_cliente][3] = int(input('Número da Casa: '))
                                    on_numero_casa = False
                                except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                                    os.system('cls')
                                    print('Digite apenas números inteiros!')
                                    sleep(2) # Vai esperar dois segundos até prosseguir.
                                    os.system('cls')
                                    print('\n')
                            on_estado = True
                            while on_estado == True:
                                lista_clientes[linha_do_cliente][4] = str(input('Estado: '))
                                texto = lista_clientes[linha_do_cliente][4]
                                tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                                if tem_numeros == True:
                                    os.system('cls')
                                    print('Digite apenas letras!')
                                    sleep(2) # Vai esperar dois segundos até prosseguir.
                                    os.system('cls')
                                    print('\n')
                                else:
                                    on_estado = False
                            on_cidade = True
                            while on_cidade == True:
                                lista_clientes[linha_do_cliente][5] = str(input('Cidade: '))
                                texto = lista_clientes[linha_do_cliente][5]
                                tem_numeros = Functions_P3.verificarNumerosNaString(texto)
                                if tem_numeros == True:
                                    os.system('cls')
                                    print('Digite apenas letras!')
                                    sleep(2) # Vai esperar dois segundos até prosseguir.
                                    os.system('cls')
                                    print('\n')
                                else:
                                    on_cidade = False
                            lista_clientes[linha_do_cliente][6] = str(input('Bairro: '))
                            on_cep = True
                            while on_cep == True:
                                try:
                                    lista_clientes[linha_do_cliente][7] = int(input('CEP (Apenas números, sem formatação!): '))
                                    on_cep = False
                                except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                                    os.system('cls')
                                    print('Digite apenas números inteiros!')
                                    sleep(2) # Vai esperar dois segundos até prosseguir.
                                    os.system('cls')
                                    print('\n')
                            
                            # Recriação e formatação do arquivo "Clientes.csv" com os dados alterados.
                            EstruturaCSV = ['Código do Cliente','Nome', 'Rua', 'Número da Casa',
                                            'Estado', 'Cidade', 'Bairro', 'CEP', 'Nº de Telefone']
                            Functions_P3.manipularCSV_ComLista(caminho_clientes, 'write', 'utf8', EstruturaCSV)
                            for clientes in range(1, len(lista_clientes)):
                                todas_informacoes_cliente = []
                                for informacoes_cliente in range(9):
                                    todas_informacoes_cliente.append(lista_clientes[clientes][informacoes_cliente])
                                Functions_P3.manipularCSV_ComLista(caminho_clientes, 'append', 'utf8', todas_informacoes_cliente)
                            
                            # Imprimindo mensagem de sucesso na edição e voltando ao menu anterior.
                            os.system('cls')
                            print(f'\nEndereço do cliente "{lista_clientes[linha_do_cliente][1]}" editado com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.')
                            on_menu_alterar_info = False
                            keyboard.wait('space') # Vai esperar o usuário pressionar a tecla "Espaço" para prosseguir.
                        
                        # Vai permitir a edição do Nº de telefone do cliente.    
                        elif menu_alterar_options == 3:
                            os.system('cls')
                            on_telefone = True
                            while on_telefone == True:
                                try:
                                    lista_clientes[linha_do_cliente][8] = int(input('\nTelefone do cliente (Apenas números, sem formatação!): '))
                                    on_telefone = False
                                except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                                    os.system('cls')
                                    print('Digite apenas números inteiros!')
                                    sleep(2) # Vai esperar dois segundos até prosseguir.
                                    os.system('cls')
                            
                            # Recriação e formatação do arquivo "Clientes.csv" com os dados alterados.
                            EstruturaCSV = ['Código do Cliente','Nome', 'Rua', 'Número da Casa',
                                            'Estado', 'Cidade', 'Bairro', 'CEP', 'Nº de Telefone']
                            Functions_P3.manipularCSV_ComLista(caminho_clientes, 'write', 'utf8', EstruturaCSV)
                            for clientes in range(1, len(lista_clientes)):
                                todas_informacoes_cliente = []
                                for informacoes_cliente in range(9):
                                    todas_informacoes_cliente.append(lista_clientes[clientes][informacoes_cliente])
                                Functions_P3.manipularCSV_ComLista(caminho_clientes, 'append', 'utf8', todas_informacoes_cliente)
                            
                            # Imprimindo mensagem de sucesso na edição e voltando ao menu anterior.
                            os.system('cls')
                            print(f'\nTelefone do cliente "{lista_clientes[linha_do_cliente][1]}" editado com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.')
                            on_menu_alterar_info = False
                            keyboard.wait('space') # Vai esperar o usuário pressionar a tecla "Espaço" para prosseguir.

                        # Vai voltar ao menu anterior, se a opção "4" for selecionada neste sub-menu.
                        elif menu_alterar_options == 4:
                            os.system('cls')
                            print("\nVoltando ao menu anterior!\n")
                            sleep(2) # Vai esperar dois segundos até prosseguir.

                    # Se o cliente não existir, uma mensagem de erro será apresentada.    
                    else:
                        os.system('cls')
                        print('\nNão constam dados desse cliente no sistema!\n')
                        sleep(3)

            # Vai entrar no sub-menu de excluir um determinado cliente através do seu ID.
            elif menu_clientes_options == 3:
                # Vai verificar se existem clientes cadastrados no "Clientes.csv".
                try:
                    tem_clientes = int(lista_clientes[1][0])
                    tem_clientes = True
                except (IndexError, ValueError):
                    tem_clientes = False
                    os.system('cls')
                    print('\nAinda não há clientes cadastrados!\n')
                    sleep(2)

                # Vai continuar se pelo menos um cliente já estiver sido cadastrado.
                if tem_clientes == True:
                    # Vai pedir o código do cliente.
                    # E tratar os erros, se forem digitadas letras, números decimais ou caracteres especiais.
                    on_id_cliente = True
                    while on_id_cliente == True:
                        try:
                            os.system('cls')
                            id_listagem = int(input('\nDigite o ID do cliente: '))
                            on_id_cliente = False
                        except ValueError:
                            os.system('cls')
                            print('\nDigite apenas números!\n')
                            sleep(2)
                    
                    # Vai verificar se o cliente existe,
                    # comparando o ID dele com os IDs disponíveis na lista.
                    cliente_existe = True
                    for linha_do_cliente in range(1, len(lista_clientes)):
                        if int(lista_clientes[linha_do_cliente][0]) == id_listagem:
                            cliente_existe = True
                            break
                        else:
                            cliente_existe = False
                    
                    # Se o cliente existir, o programa irá prosseguir e removê-lo da matriz 'lista_clientes'.
                    if cliente_existe == True:
                        # Vai verificar se o cliente está cadastrado em alguma manutenção.
                        # Pois ele só pode ser excluido se não estiver cadastrado em nenhuma.
                        cliente_em_manutencao = False
                        for linha_da_manutencao in range(1, len(lista_manutencoes_agendadas)):
                            if int(lista_manutencoes_agendadas[linha_da_manutencao][1]) == id_listagem:
                                cliente_em_manutencao = True
                                break
                            else:
                                cliente_em_manutencao = False
                        
                        # Vai remover o cliente, se não estiver cadastrado em nenhuma manutenção.
                        if cliente_em_manutencao == False:
                            os.system('cls')
                            # Vai pedir confirmação de exclusão.
                            confirmar_exclusao = str(input('\nTem certeza que deseja excluir o cliente'
                                                          f' "{lista_clientes[linha_do_cliente][1]}"?\n'
                                                           '\nSua escolha (S = SIM; N = NÃO.): ').upper())
                            # Vai continuar com a exclusão, se o usuário confirmar.
                            if confirmar_exclusao == 'S':
                                lista_clientes.pop(linha_do_cliente)
                                # Recriação do arquivo "Clientes.csv" com o cliente removido.
                                # Vai estruturar o arquivo .csv.
                                EstruturaCSV = ['Código do Cliente','Nome', 'Rua', 'Número da Casa',
                                                'Estado', 'Cidade', 'Bairro', 'CEP', 'Nº de Telefone']
                                Functions_P3.manipularCSV_ComLista(caminho_clientes, 'write', 'utf8', EstruturaCSV)
                                # Vai copiar cada linha da matriz 'lista_clientes' para o arquivo "Clientes.csv".
                                for clientes in range(1, len(lista_clientes)):
                                    todas_informacoes_cliente = []
                                    for informacoes_cliente in range(9):
                                        todas_informacoes_cliente.append(lista_clientes[clientes][informacoes_cliente])
                                    Functions_P3.manipularCSV_ComLista(caminho_clientes, 'append', 'utf8', todas_informacoes_cliente)
                                os.system('cls')
                                print(f'\nCliente removido com sucesso!\n')
                                print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                                keyboard.wait('space')
                            # Vai sair dessa seção, se o usuário negar a permissão de exclusão.
                            else:
                                os.system('cls')
                                print(f'\nPermissão de exclusão do cliente "{lista_clientes[linha_do_cliente][1]}" negada!\n')
                                print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                                keyboard.wait('space')
                        
                        # Vai apresentar um erro, se o usuário estiver cadastrado em uma manutenção.
                        else:
                            os.system('cls')
                            print(f'\nO cliente "{lista_clientes[linha_do_cliente][1]}" não pode ser excluido, '
                                    f'pois está cadastrado na manutenção "{lista_manutencoes_agendadas[linha_da_manutencao][0]}"!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                            keyboard.wait('space')
                    
                    # Vai apresentar um erro se o cliente não existir.
                    else:
                        os.system('cls')
                        print('\nNão constam dados desse cliente no sistema!\n')
                        sleep(3)

            # Vai entrar no sub-menu de listar todos os clientes cadastrados
            # ou apenas um, através do seu ID.
            elif menu_clientes_options == 4:
                # Vai verificar se existem clientes cadastrados.
                try:
                    tem_clientes = int(lista_clientes[1][0])
                    tem_clientes = True
                except (IndexError, ValueError):
                    tem_clientes = False
                    os.system('cls')
                    print('\nAinda não há clientes cadastrados!\n')
                    sleep(2)
                
                # Vai continuar se pelo menos um cliente já estiver sido cadastrado.
                if tem_clientes == True:
                    on_menu_listagem = True # Vai permitir a entrada no sub-menu de listar os clientes.
                    while on_menu_listagem == True:
                        os.system('cls')
                        try:
                            menu_listagem_options = int(input('\nSelecione uma opção:\n\n'
                                '1. Listar dados de todos os clientes.\n'
                                '2. Listar dados de um cliente específico.\n'
                                '3. Voltar ao menu anterior.\n'
                                '4. Sair.\n\n'
                                'Sua escolha: '))
                        except ValueError: # Tratamento de erro se forem digitadas letras, números decimais ou caracteres especiais.
                            menu_listagem_options = 5 # O programa vai cair na condição de opção inválida!
                        
                        try:
                            # Vai imprimir em tela as informações de todos os clientes.
                            if menu_listagem_options == 1:
                                # Esse bloco vai ordenar os clientes em ordem alfabetica.
                                # Primeiramente vai enviar o nome de cada cliente para uma lista.
                                # Essa lista vai ser usada como referência (índice) para ordenar
                                # a matriz 'lista_clientes_ordenada'.
                                nomes_ordenados = []
                                for cliente in range(1, len(lista_clientes)):
                                    nomes_ordenados.append(lista_clientes[cliente][1])
                                # Depois vai ordenar os nomes que vão estar contidos nessa lista.
                                # Referência do método de ordenação (Insertion Sort):
                                # Máteria: Algoritmos e Programação I, Professora: Claudia P. Pereira
                                # Link: https://drive.google.com/file/d/1Hu6HUsfCNfRhaMRwm-Ysh_lw_B_1m22t/view
                                # Acesso em: 06 de Junho de 2021
                                t = len(nomes_ordenados)
                                for i in range(1, t):
                                    aux = nomes_ordenados[i]
                                    j = i - 1
                                    while j >= 0 and aux < nomes_ordenados[j]:
                                        nomes_ordenados[j+1] = nomes_ordenados [j]
                                        j -= 1
                                    nomes_ordenados[j+1] = aux
                                # Uma matriz ordenada será criada, a partir dos elementos da matriz
                                # 'lista_clientes', tendo como base a ordem da lista 'nomes_ordenados'
                                lista_clientes_ordenada = [] # Essa será a matriz ordenada.
                                for linha in range(1, len(lista_clientes)):
                                    lista_clientes_ordenada.append(['']) # Criando cada linha da matriz, em branco.
                                # Inserindo as informações dos clientes, usandos a ordem da lista 'nomes_ordenados'.
                                for cliente in range(1, len(lista_clientes)):
                                    for informacao in range(len(nomes_ordenados)):
                                        if lista_clientes[cliente][1] == nomes_ordenados[informacao]:
                                            lista_clientes_ordenada[informacao] = lista_clientes[cliente]

                                # Esse bloco é responsável por mostrar as informações da lista ordenada na tela.
                                os.system('cls')
                                print('\nDados de todos clientes:\n\n')
                                for cliente in range(len(lista_clientes_ordenada)):
                                        print(f'ID: {lista_clientes_ordenada[cliente][0]}\n')
                                        print(f'Nome: {lista_clientes_ordenada[cliente][1]}\n')
                                        print(f'Endereço do cliente:\nRua: {lista_clientes_ordenada[cliente][2]},'
                                                f' Nº: {lista_clientes_ordenada[cliente][3]},'
                                                f' Estado: {lista_clientes_ordenada[cliente][4]},'
                                                f' Cidade: {lista_clientes_ordenada[cliente][5]},'
                                                f' Bairro: {lista_clientes_ordenada[cliente][6]},'
                                                f' CEP: {lista_clientes_ordenada[cliente][7]}\n')
                                        print(f'Telefone: {lista_clientes_ordenada[cliente][8]}\n')
                                        print('\n')    
                                print('Pressione a tecla "Espaço" no teclado, para prosseguir.\n')
                                keyboard.wait('space')
                            
                            # Vai imprimir em tela as informações de um clientes específico.
                            elif menu_listagem_options == 2:
                                # Vai perguntar qual o ID do cliente.
                                on_id_cliente = True
                                while on_id_cliente == True:
                                    try:
                                        os.system('cls')
                                        id_listagem = int(input('\nDigite o ID do cliente: '))
                                        on_id_cliente = False
                                    except ValueError:
                                        os.system('cls')
                                        print('\nDigite apenas números!\n')
                                        sleep(2)
                                
                                # Vai verificar se o cliente existe.
                                cliente_existe = True
                                for linha_do_cliente in range(1, len(lista_clientes)):
                                    if int(lista_clientes[linha_do_cliente][0]) == id_listagem:
                                        cliente_existe = True
                                        break
                                    else:
                                        cliente_existe = False
                                
                                # Vai mostrar as informações do cliente, se ele existir.
                                if cliente_existe == True:
                                    os.system('cls')
                                    print(f'\nDados do cliente: {lista_clientes[linha_do_cliente][1]}\n\n')
                                    print(f'ID: {lista_clientes[linha_do_cliente][0]}\n')
                                    print(f'Endereço do cliente:\nRua: {lista_clientes[linha_do_cliente][2]},'
                                            f' Nº: {lista_clientes[linha_do_cliente][3]},'
                                            f' Estado: {lista_clientes[linha_do_cliente][4]},'
                                            f' Cidade: {lista_clientes[linha_do_cliente][5]},'
                                            f' Bairro: {lista_clientes[linha_do_cliente][6]},'
                                            f' CEP: {lista_clientes[linha_do_cliente][7]}\n')
                                    print(f'Telefone: {lista_clientes[linha_do_cliente][8]}\n')
                                    print('\n')
                                    print('Pressione a tecla "Espaço" no teclado, para prosseguir.\n')
                                    keyboard.wait('space')
                                
                                # Vai apresentar uma mensagem de erro se ele não existir.
                                else:
                                    os.system('cls')
                                    print('\nNão constam dados desse cliente no sistema!\n')
                                    sleep(3)
                                
                            # Vai voltar ao menu anterior, se a opção "3" for selecionada.
                            elif menu_listagem_options == 3:
                                os.system('cls')
                                print('\nVoltando ao menu anterior!\n')
                                on_menu_listagem = False
                                sleep(2) # Vai esperar dois segundos até prosseguir.
                    
                            # Vai sair do programa, se a opção "6" for selecionada.
                            elif menu_listagem_options == 4:
                                os.system('cls')
                                print("\nAté mais!\n")
                                exit()
                                
                            # Vai entrar nessa condição, se uma opção inválida for digitada no menu.
                            else:
                                os.system('cls')
                                print('\nEssa opção não existe!\n')
                                sleep(2) # Vai esperar dois segundos até voltar ao menu.
                        
                        # Vai apresentar um erro se os dados de algum cliente, no arquivo
                        # "Clientes.csv", estiverem incompletos.
                        except IndexError:
                            os.system('cls')
                            print('\nOs dados de alguns clientes estão incompletos!\n')
                            print('Verifique o arquivo "Clientes.csv"!\n')
                            sleep(3)
        
            # Vai voltar ao menu principal, se a opção "5" for selecionada.
            elif menu_clientes_options == 5:
                os.system('cls')
                print("\nVoltando ao Menu Principal...\n")
                on_menu_clientes = False
                sleep(2) # Vai esperar dois segundos até prosseguir.
            
            # Vai sair do programa, se a opção "6" for selecionada.
            elif menu_clientes_options == 6:
                os.system('cls')
                print("\nAté mais!\n")
                exit()
            
            # Vai entrar apresentar uma mensagem de erro, se uma opção inválida for digitada no sub-menu.
            else:
                os.system('cls')
                print('\nEssa opção não existe!\n')
                sleep(2) # Vai esperar dois segundos até voltar ao menu.

    # Sub-menu onde serão efetuadas operações que estão relacionadas especificamente
    # as manutenções e aos arquivos "Manutenções_Agendadas.csv", "Manutenções_Realizadas.csv" e "Manutenções_Agendadas (Ordenadas).csv".
    elif start_menu_options == 2:
        on_menu_manutencoes = True # Vai permitir a entrada no sub-menu das manutenções.
                                # "True" > Entrar | "False" > Sair
        while on_menu_manutencoes == True:
            os.system('cls')
            print("\nOperações com Manutenções\n"
            "\n1. Agendar uma manutenção manualmente.\n"
            "2. Editar manutenção.\n"
            "3. Excluir manutenção.\n"
            "4. Realizar manutenção.\n"
            "5. Ver a lista de manutenções.\n"
            "6. Imprimir lista de manutenções.\n"
            "7. Voltar ao menu principal.\n"
            )
            try:
                menu_manutencoes_options = int(input("Sua escolha: "))
                assert menu_manutencoes_options > 0 and menu_manutencoes_options < 8
            # Irá tratar os erros, caso o usuário digite uma letra ou opção inválida.
            except (ValueError, AssertionError):
                menu_manutencoes_options = 8 # Vai entrar na condição de opção inválida.

            # Vai permitir o agendamento manual de uma nova manutenção.
            if menu_manutencoes_options == 1:
                # Vai verificar se existem clientes cadastrados no "Clientes.csv".
                try:
                    tem_clientes = int(lista_clientes[1][0])
                    tem_clientes = True
                except (IndexError, ValueError):
                    tem_clientes = False
                    os.system('cls')
                    print('\nAinda não há clientes cadastrados!\n')
                    sleep(2)

                # Vai continuar se pelo menos um cliente já estiver sido cadastrado.
                if tem_clientes == True:
                    # Vai pedir o código do cliente.
                    # E tratar os erros, se forem digitadas letras, números decimais ou caracteres especiais.
                    on_id_cliente = True
                    while on_id_cliente == True:
                        try:
                            os.system('cls')
                            print('\nInformações para cadastrar uma nova manutenção:\n')
                            id_listagem = int(input('\nDigite o ID do cliente: '))
                            on_id_cliente = False
                        except ValueError:
                            os.system('cls')
                            print('\nDigite apenas números!\n')
                            sleep(2)
                    
                    # Vai verificar se o cliente existe,
                    # comparando o ID dele com os IDs disponíveis na lista.
                    cliente_existe = True
                    for linha_do_cliente in range(1, len(lista_clientes)):
                        if int(lista_clientes[linha_do_cliente][0]) == id_listagem:
                            cliente_existe = True
                            break
                        else:
                            cliente_existe = False
                    
                    # Vai continuar se o cliente for encontrado.
                    if cliente_existe == True:
                        # Vai copiar o código da última manutenção agendada para uma variável.
                        # Se não existirem manutenções agendadas, o código da última será '0'. 
                        try:
                            ultima_manutencao = int(lista_manutencoes_agendadas[len(lista_manutencoes_agendadas)-1][0])
                        # Vai dar erro se não houver alguma manutenção agendada, pois a lista irá retornar a string 'Código da Manutenção',
                        # e não o número inteiro do código dela.
                        except ValueError: 
                            ultima_manutencao = 0

                        nova_manutencao = []
                        nova_manutencao.append(ultima_manutencao + 1) # Código da manutenção.
                        nova_manutencao.append(lista_clientes[linha_do_cliente][0]) # ID do cliente.

                        # Nesse bloco serão inseridos os dados da nova manutenção.
                        # Preço da manutenção.
                        os.system('cls')
                        print(f'\nCliente: "{lista_clientes[linha_do_cliente][1]}"\n')
                        on_preco = True
                        while on_preco == True:
                            try:
                                nova_manutencao.append(float(input('\nPreço da manutenção (R$): ')))
                                on_preco = False
                            except ValueError:
                                os.system('cls')
                                print('\nDigite apenas números!\n')
                                sleep(2)
                                os.system('cls')
                        # Nome da peça do cliente que passará por manutenção.
                        nova_manutencao.append(str(input('\nNome da Peça:  ')))
                        # Prazo de validade da peça.
                        # Vai perguntar como a data de validade será expressa
                        # e entrar na condição desejada.
                        expressar_validade = True
                        while expressar_validade == True:
                            os.system('cls')
                            tipo_validade = int(input('\nComo é expresso o prazo de validade da peça?\n'
                                                    '1. Dias\n'
                                                    '2. Meses\n'
                                                    '3. Anos\n'
                                                    '\nSua escolha: '))
                            try:
                                assert tipo_validade > 0 and tipo_validade < 4
                                expressar_validade = False
                            except AssertionError:
                                os.system('cls')
                                print('\nOpção inválida!\n')
                                sleep(2)
                        # Data de validade em dias.
                        if tipo_validade == 1:
                            nova_manutencao.append('Dias')
                            on_dias = True
                            while on_dias == True:
                                os.system('cls')
                                try:
                                    nova_manutencao.append(int(input('\nDigite a quantidade de dias: ')))
                                    on_dias = False
                                except ValueError:
                                    os.system('cls')
                                    print('\nDigite apenas números!\n')
                                    sleep(2)
                        # Data de validade em meses.
                        elif tipo_validade == 2:
                            nova_manutencao.append('Meses')
                            on_meses = True
                            while on_meses == True:
                                os.system('cls')
                                try:
                                    nova_manutencao.append(int(input('\nDigite a quantidade de meses: ')))
                                    on_meses = False
                                except ValueError:
                                    os.system('cls')
                                    print('\nDigite apenas números!\n')
                                    sleep(2) 
                        # Data de validade em anos.
                        elif tipo_validade == 3:
                            nova_manutencao.append('Anos')
                            on_anos = True
                            while on_anos == True:
                                os.system('cls')
                                try:
                                    nova_manutencao.append(int(input('\nDigite a quantidade de anos: ')))
                                    on_anos = False
                                except ValueError:
                                    os.system('cls')
                                    print('\nDigite apenas números!\n')
                                    sleep(2)
                        # Vai perguntar em qual data a manutenção será agendada.
                        os.system('cls')
                        print('\nData de Agendamento da Manutenção: ')
                        # Dia da manutenção.
                        on_dia_agendamento = True
                        while on_dia_agendamento == True:
                            try:
                                dia_agendamento = int(input('\nDia: '))
                                on_dia_agendamento = False
                            except ValueError:
                                os.system('cls')
                                print('\nDigite apenas números!\n')
                                sleep(2)
                                os.system('cls')
                        # Mês da manutenção.
                        on_mes_agendamento = True
                        while on_mes_agendamento == True:
                            try:
                                mes_agendamento = int(input('\nMês (apenas números): '))
                                assert mes_agendamento > 0 and mes_agendamento < 13
                                on_mes_agendamento = False
                            except (ValueError, AssertionError):
                                os.system('cls')
                                print('\nDigite um mês válido!\n')
                                sleep(2)
                                os.system('cls')
                        # Ano da manutenção.
                        on_ano_agendamento = True
                        while on_ano_agendamento == True:
                            try:
                                ano_agendamento = int(input('\nAno: '))
                                on_ano_agendamento = False
                            except ValueError:
                                os.system('cls')
                                print('\nDigite apenas números!\n')
                                sleep(2)
                                os.system('cls')
                        # Vai formatar a data e inseri-la na lista.
                        nova_manutencao.append(f'{dia_agendamento}/{mes_agendamento}/{ano_agendamento}')

                        # Fase de registro das informações da lista no arquivo "Manutenções_Agendadas.csv".
                        Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', nova_manutencao)

                        # Atualizando os dados da variável em memória.
                        lista_manutencoes_agendadas = Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'copy_to_list', 'utf8', '')

                        # Voltando para o menu principal, após agendar a manutenção.
                        os.system('cls')
                        print('\nNova manutenção agendada com sucesso!\n')
                        print(f'O código da nova manutenção, do cliente "{lista_clientes[linha_do_cliente][1]}", é: {nova_manutencao[0]}')
                        print(f'\nA manutenção foi agendada para a data: {nova_manutencao[6]}\n')
                        print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.')
                        keyboard.wait('space')
                        on_menu_manutencoes = False

                    # Vai apresentar um erro se o cliente não existir.
                    else:
                        os.system('cls')
                        print('\nNão constam dados desse cliente no sistema!\n')
                        sleep(3)

            # Vai permitir a edição dos dados de uma manutenção.
            elif menu_manutencoes_options == 2:
                # Vai verificar se existem manutenções agendadas no "Manutenções_Agendadas.csv".
                try:
                    tem_manutencoes = int(lista_manutencoes_agendadas[1][0])
                    tem_manutencoes = True
                except (IndexError, ValueError):
                    tem_manutencoes = False
                    os.system('cls')
                    print('\nAinda não existem manutenções agendadas!\n')
                    sleep(2)

                # Vai continuar se pelo menos uma manutenção já estiver sido agendada.
                if tem_manutencoes == True:
                    # Vai pedir o código da manutenção.
                    # E tratar os erros, se forem digitadas letras, números decimais ou caracteres especiais.
                    on_codigo_manutencao = True
                    while on_codigo_manutencao == True:
                        try:
                            os.system('cls')
                            codigo_listagem = int(input('\nDigite o código da manutenção: '))
                            on_codigo_manutencao = False
                        except ValueError:
                            os.system('cls')
                            print('\nDigite apenas números!\n')
                            sleep(2)
                    
                    # Vai verificar se a manutenção digitada existe,
                    # comparando o código dela com os códigos disponíveis na lista.
                    manutencao_existe = True
                    for linha_da_manutencao in range(1, len(lista_manutencoes_agendadas)):
                        if int(lista_manutencoes_agendadas[linha_da_manutencao][0]) == codigo_listagem:
                            manutencao_existe = True
                            break
                        else:
                            manutencao_existe = False
                    
                    # Se a manutenção existir, o programa irá prosseguir e 
                    # permitir a edição dos dados dela na matriz "lista_manutencoes_agendadas".
                    if manutencao_existe == True:
                        # Vai perguntar qual informação que o usuário que modificar na manutenção.
                        on_menu_alterar_info = True
                        while on_menu_alterar_info == True:
                            os.system('cls') # Vai limpar o terminal.
                            try:
                                menu_alterar_options = int(input(f'\nQual informação da manutenção "{lista_manutencoes_agendadas[linha_da_manutencao][0]}" você deseja alterar?\n'
                                                                '1. Código do cliente vinculado.\n'
                                                                '2. Preço da manutenção.\n'
                                                                '3. Nome da peça.\n'
                                                                '4. Tipo e Prazo de Validade da peça.\n'
                                                                '5. Data para a manutenção.'
                                                                '\n6. Voltar ao menu anterior.\n'
                                                                '\nSua escolha: '))
                                assert menu_alterar_options > 0 and menu_alterar_options < 7 # Vai verificar se a opção digitada existe.
                                on_menu_alterar_info = False
                            except (ValueError,AssertionError):
                                os.system('cls')
                                print('\nOpção inválida!\n')
                                sleep(2)
                        
                        # Nessa seção poderá ser editado o ID do cliente vinculado a manutenção.
                        if menu_alterar_options == 1:
                            # Vai perguntar qual o código do cliente.
                            on_cliente_manutencao = True
                            while on_cliente_manutencao == True:
                                try:
                                    os.system('cls')
                                    novo_cliente_vinculado = int(input('\nDigite o código do novo cliente que será vinculado'
                                                                        f'a manutenção: "{lista_manutencoes_agendadas[linha_da_manutencao][0]}": '))
                                except ValueError:
                                    os.system('cls')
                                    print('\nDigite apenas números!\n')
                                    sleep(2)
                            
                                # Vai verificar se o cliente existe,
                                # comparando o ID dele com os IDs disponíveis na lista de clientes.
                                cliente_existe = True
                                for linha_do_cliente in range(1, len(lista_clientes)):
                                    if int(lista_clientes[linha_do_cliente][0]) == novo_cliente_vinculado:
                                        cliente_existe = True
                                        break
                                    else:
                                        cliente_existe = False
                                
                                # Se o cliente exister, o programa irá prosseguir e substituir o ID vinculado a manutenção.
                                if cliente_existe == True:
                                    lista_manutencoes_agendadas[linha_da_manutencao][1] = novo_cliente_vinculado
                                    # Recriação do arquivo "Manutenções_Agendadas.csv" com o cliente alterado.
                                    # Vai estruturar o arquivo .csv.
                                    EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                                    'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                                    'Data para a Manutenção - DD/MM/AAAA']
                                    Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
                                    # Vai copiar cada linha da matriz "lista_manutencoes_agendadas" para o arquivo "Manutenções_Agendadas.csv".
                                    for manutencoes in range(1, len(lista_manutencoes_agendadas)):
                                        todos_dados_manutencao = []
                                        for dados_manutencao in range(7):
                                            todos_dados_manutencao.append(lista_manutencoes_agendadas[manutencoes][dados_manutencao])
                                        Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', todos_dados_manutencao)
                                    os.system('cls')
                                    print(f'\nO cliente vinculado a manutenção foi editado com sucesso!\n')
                                    print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                                    on_cliente_manutencao = False
                                    keyboard.wait('space')
                                
                                # Se o cliente não existir, o programa irá apresentar uma mensagem de erro
                                # e perguntar se o usuário quer tentar novamente.
                                else:
                                    os.system('cls')
                                    print(f'\nO cliente "{novo_cliente_vinculado}" não foi encontrado!\n')
                                    continuar = int(input('\nDeseja tentar novamente?'
                                                            '\n1. Sim.'
                                                            '\n2. Não.\n'
                                                            '\nSua escolha: '))
                                    if continuar == 1:
                                        os.system('cls')
                                        print('\nVoltando a edição do cliente na manutenção!\n')
                                        sleep(2)
                                    else:
                                        os.system('cls')
                                        print('\nVoltando ao menu anterior!\n')
                                        on_cliente_manutencao = False
                                        sleep(2)

                        # Nessa seção poderá ser editado o preço da manutenção.
                        elif menu_alterar_options == 2:
                            # Vai perguntar qual o novo preço da manutenção.
                            on_preco = True
                            while on_preco == True:
                                try:
                                    os.system('cls')
                                    lista_manutencoes_agendadas[linha_da_manutencao][2] = float(input('\nDigite o novo preço da '
                                                                                                     f'manutenção "{lista_manutencoes_agendadas[linha_da_manutencao][0]}": '))
                                    on_preco = False
                                except ValueError:
                                    os.system('cls')
                                    print('\nDigite apenas números!\n')
                                    sleep(2)
                            # Recriação do arquivo "Manutenções_Agendadas.csv" com o preço alterado.
                            # Vai estruturar o arquivo .csv.
                            EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                            'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                            'Data para a Manutenção - DD/MM/AAAA']
                            Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
                            # Vai copiar cada linha da matriz "lista_manutencoes_agendadas" para o arquivo "Manutenções_Agendadas.csv".
                            for manutencoes in range(1, len(lista_manutencoes_agendadas)):
                                todos_dados_manutencao = []
                                for dados_manutencao in range(7):
                                    todos_dados_manutencao.append(lista_manutencoes_agendadas[manutencoes][dados_manutencao])
                                Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', todos_dados_manutencao)
                            os.system('cls')
                            print(f'\nO preço da manutenção foi modificado com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                            on_cliente_manutencao = False
                            keyboard.wait('space')

                        # Nessa seção poderá ser editado o nome da peça vinculada a manutenção.
                        elif menu_alterar_options == 3:
                            # Vai perguntar qual o novo nome da peça.
                            os.system('cls')
                            lista_manutencoes_agendadas[linha_da_manutencao][3] = str(input('\nDigite o novo nome da peça vinculada a '
                                                                                            f'manutenção "{lista_manutencoes_agendadas[linha_da_manutencao][0]}": '))
                            # Recriação do arquivo "Manutenções_Agendadas.csv" com o nome da peça alterado.
                            # Vai estruturar o arquivo .csv.
                            EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                            'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                            'Data para a Manutenção - DD/MM/AAAA']
                            Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
                            # Vai copiar cada linha da matriz "lista_manutencoes_agendadas" para o arquivo "Manutenções_Agendadas.csv".
                            for manutencoes in range(1, len(lista_manutencoes_agendadas)):
                                todos_dados_manutencao = []
                                for dados_manutencao in range(7):
                                    todos_dados_manutencao.append(lista_manutencoes_agendadas[manutencoes][dados_manutencao])
                                Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', todos_dados_manutencao)
                            os.system('cls')
                            print(f'\nO nome da peça vinculada a manutenção foi modificado com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                            on_cliente_manutencao = False
                            keyboard.wait('space')
                        
                        # Nessa seção poderá ser editado o tipo e prazo de validade da peça vinculada a manutenção.
                        elif menu_alterar_options == 4:
                            # Vai perguntar como a validade será expressa.
                            expressar_validade = True
                            while expressar_validade == True:
                                os.system('cls')
                                tipo_validade = int(input('\nComo será expresso o novo prazo de validade da peça?\n'
                                                        '1. Dias\n'
                                                        '2. Meses\n'
                                                        '3. Anos\n'
                                                        '\nSua escolha: '))
                                try:
                                    assert tipo_validade > 0 and tipo_validade < 4
                                    expressar_validade = False
                                except AssertionError:
                                    os.system('cls')
                                    print('\nOpção inválida!\n')
                                    sleep(2)
                            # Data de validade em dias.
                            if tipo_validade == 1:
                                lista_manutencoes_agendadas[linha_da_manutencao][4] = 'Dias' # Vai vincular o tipo de validade ao arquivo.
                                on_dias = True
                                while on_dias == True:
                                    os.system('cls')
                                    try:
                                        lista_manutencoes_agendadas[linha_da_manutencao][5] = int(input('\nDigite a quantidade de dias: '))
                                        on_dias = False
                                    except ValueError:
                                        os.system('cls')
                                        print('\nDigite apenas números!\n')
                                        sleep(2)
                            # Data de validade em meses.
                            elif tipo_validade == 2:
                                lista_manutencoes_agendadas[linha_da_manutencao][4] = 'Meses' # Vai vincular o tipo de validade ao arquivo.
                                on_meses = True
                                while on_meses == True:
                                    os.system('cls')
                                    try:
                                        lista_manutencoes_agendadas[linha_da_manutencao][5] = int(input('\nDigite a quantidade de meses: '))
                                        on_meses = False
                                    except ValueError:
                                        os.system('cls')
                                        print('\nDigite apenas números!\n')
                                        sleep(2) 
                            # Data de validade em anos.
                            elif tipo_validade == 3:
                                lista_manutencoes_agendadas[linha_da_manutencao][4] = 'Anos' # Vai vincular o tipo de validade ao arquivo.
                                on_anos = True
                                while on_anos == True:
                                    os.system('cls')
                                    try:
                                        lista_manutencoes_agendadas[linha_da_manutencao][5] = int(input('\nDigite a quantidade de anos: '))
                                        on_anos = False
                                    except ValueError:
                                        os.system('cls')
                                        print('\nDigite apenas números!\n')
                                        sleep(2)
                            
                            # Recriação do arquivo "Manutenções_Agendadas.csv" com o prazo de validade da peça alterado.
                            # Vai estruturar o arquivo .csv.
                            EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                            'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                            'Data para a Manutenção - DD/MM/AAAA']
                            Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
                            # Vai copiar cada linha da matriz "lista_manutencoes_agendadas" para o arquivo "Manutenções_Agendadas.csv".
                            for manutencoes in range(1, len(lista_manutencoes_agendadas)):
                                todos_dados_manutencao = []
                                for dados_manutencao in range(7):
                                    todos_dados_manutencao.append(lista_manutencoes_agendadas[manutencoes][dados_manutencao])
                                Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', todos_dados_manutencao)
                            os.system('cls')
                            print(f'\nO tipo e prazo de validade da peça, vinculada a manutenção, foi editado com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                            on_cliente_manutencao = False
                            keyboard.wait('space')
                        
                        # Nessa seção poderá ser editada a data para a manutenção.
                        elif menu_alterar_options == 5:
                            # Vai perguntar qual a nova data em que a manutenção será agendada.
                            os.system('cls')
                            print('\nNova data de agendamento da manutenção: ')
                            # Dia da manutenção.
                            on_dia_agendamento = True
                            while on_dia_agendamento == True:
                                try:
                                    dia_agendamento = int(input('\nDia: '))
                                    on_dia_agendamento = False
                                except ValueError:
                                    os.system('cls')
                                    print('\nDigite apenas números!\n')
                                    sleep(2)
                                    os.system('cls')
                            # Mês da manutenção.
                            on_mes_agendamento = True
                            while on_mes_agendamento == True:
                                try:
                                    mes_agendamento = int(input('\nMês (apenas números): '))
                                    assert mes_agendamento > 0 and mes_agendamento < 13
                                    on_mes_agendamento = False
                                except (ValueError, AssertionError):
                                    os.system('cls')
                                    print('\nDigite um mês válido!\n')
                                    sleep(2)
                                    os.system('cls')
                            # Ano da manutenção.
                            on_ano_agendamento = True
                            while on_ano_agendamento == True:
                                try:
                                    ano_agendamento = int(input('\nAno: '))
                                    on_ano_agendamento = False
                                except ValueError:
                                    os.system('cls')
                                    print('\nDigite apenas números!\n')
                                    sleep(2)
                                    os.system('cls')
                            # Vai formatar a data e inseri-la na matriz.
                            lista_manutencoes_agendadas[linha_da_manutencao][6] = f'{dia_agendamento}/{mes_agendamento}/{ano_agendamento}'
                            
                            # Recriação do arquivo "Manutenções_Agendadas.csv" com a data de realização da manutenção alterada.
                            # Vai estruturar o arquivo .csv.
                            EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                            'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                            'Data para a Manutenção - DD/MM/AAAA']
                            Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
                            # Vai copiar cada linha da matriz "lista_manutencoes_agendadas" para o arquivo "Manutenções_Agendadas.csv".
                            for manutencoes in range(1, len(lista_manutencoes_agendadas)):
                                todos_dados_manutencao = []
                                for dados_manutencao in range(7):
                                    todos_dados_manutencao.append(lista_manutencoes_agendadas[manutencoes][dados_manutencao])
                                Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', todos_dados_manutencao)
                            os.system('cls')
                            print(f'\nA data para a manutenção foi editada com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                            on_cliente_manutencao = False
                            keyboard.wait('space')

                        # Vai voltar ao menu anterior, se a opção "6" for selecionada.
                        else:
                            os.system('cls')
                            print('\nVoltando ao menu anterior...\n')
                            sleep(2)
                
                    # Vai apresentar um erro se a manutenção não existir.
                    else:
                        os.system('cls')
                        print('\nNão constam dados dessa manutenção na lista de manutenções agendadas!\n')
                        sleep(3)

            # Vai permitir a exclusão de uma determinada manutenção,
            # da lista de manutenções agendadas.
            elif menu_manutencoes_options == 3:
                # Vai verificar se existem manutenções agendadas no "Manutenções_Agendadas.csv".
                try:
                    tem_manutencoes = int(lista_manutencoes_agendadas[1][0])
                    tem_manutencoes = True
                except (IndexError, ValueError):
                    tem_manutencoes = False
                    os.system('cls')
                    print('\nAinda não existem manutenções agendadas!\n')
                    sleep(2)

                # Vai continuar se pelo menos uma manutenção já estiver sido agendada.
                if tem_manutencoes == True:
                    # Vai pedir o código da manutenção.
                    # E tratar os erros, se forem digitadas letras, números decimais ou caracteres especiais.
                    on_codigo_manutencao = True
                    while on_codigo_manutencao == True:
                        try:
                            os.system('cls')
                            codigo_listagem = int(input('\nDigite o código da manutenção: '))
                            on_codigo_manutencao = False
                        except ValueError:
                            os.system('cls')
                            print('\nDigite apenas números!\n')
                            sleep(2)
                    
                    # Vai verificar se a manutenção digitada existe,
                    # comparando o código dela com os códigos disponíveis na lista.
                    manutencao_existe = True
                    for linha_da_manutencao in range(1, len(lista_manutencoes_agendadas)):
                        if int(lista_manutencoes_agendadas[linha_da_manutencao][0]) == codigo_listagem:
                            manutencao_existe = True
                            break
                        else:
                            manutencao_existe = False
                    
                    # Se a manutenção existir, o programa irá prosseguir e removê-la da matriz "lista_manutencoes_agendadas".
                    if manutencao_existe == True:                  
                        os.system('cls')
                        # Vai pedir confirmação de exclusão.
                        confirmar_exclusao = str(input('\nTem certeza que deseja excluir a manutenção'
                                                        f' "{lista_manutencoes_agendadas[linha_da_manutencao][0]}"?\n'
                                                        '\nSua escolha (S = SIM; N = NÃO.): ').upper())
                        # Vai continuar com a exclusão, se o usuário confirmar.
                        if confirmar_exclusao == 'S':
                            lista_manutencoes_agendadas.pop(linha_da_manutencao)
                            # Recriação do arquivo "Manutenções_Agendadas.csv" com o cliente removido.
                            # Vai estruturar o arquivo .csv.
                            EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                            'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                            'Data para a Manutenção - DD/MM/AAAA']
                            Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
                            # Vai copiar cada linha da matriz "lista_manutencoes_agendadas" para o arquivo "Manutenções_Agendadas.csv".
                            for manutencoes in range(1, len(lista_manutencoes_agendadas)):
                                todos_dados_manutencao = []
                                for dados_manutencao in range(7):
                                    todos_dados_manutencao.append(lista_manutencoes_agendadas[manutencoes][dados_manutencao])
                                Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', todos_dados_manutencao)
                            os.system('cls')
                            print(f'\nManutenção removida com sucesso!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                            keyboard.wait('space')
                        
                        # Vai sair dessa seção, se o usuário negar a permissão de exclusão.
                        else:
                            os.system('cls')
                            print(f'\nPermissão de exclusão da manutenção "{lista_manutencoes_agendadas[linha_da_manutencao][0]}" negada!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                            keyboard.wait('space')
                    
                    # Vai apresentar um erro se a manutenção não existir.
                    else:
                        os.system('cls')
                        print('\nNão constam dados dessa manutenção na lista de manutenções agendadas!\n')
                        sleep(3)
            
            # Vai permitir que uma manutenção agendada seja realizada.
            # Removendo ela da lista de agendadas e colocando na lista de realizadas.
            # Em seguida, vai criar uma nova manutenção automática.
            elif menu_manutencoes_options == 4:
                # Vai verificar se existem manutenções agendadas no "Manutenções_Agendadas.csv".
                try:
                    tem_manutencoes = int(lista_manutencoes_agendadas[1][0])
                    tem_manutencoes = True
                except (IndexError, ValueError):
                    tem_manutencoes = False
                    os.system('cls')
                    print('\nAinda não existem manutenções agendadas!\n')
                    sleep(2)

                # Vai continuar se pelo menos uma manutenção já estiver sido agendada.
                if tem_manutencoes == True:
                    # Vai pedir o código da manutenção.
                    # E tratar os erros, se forem digitadas letras, números decimais ou caracteres especiais.
                    on_codigo_manutencao = True
                    while on_codigo_manutencao == True:
                        try:
                            os.system('cls')
                            codigo_listagem = int(input('\nDigite o código da manutenção: '))
                            on_codigo_manutencao = False
                        except ValueError:
                            os.system('cls')
                            print('\nDigite apenas números!\n')
                            sleep(2)
                    
                    # Vai verificar se a manutenção digitada existe,
                    # comparando o código dela com os códigos disponíveis na lista.
                    manutencao_existe = True
                    for linha_da_manutencao in range(1, len(lista_manutencoes_agendadas)):
                        if int(lista_manutencoes_agendadas[linha_da_manutencao][0]) == codigo_listagem:
                            manutencao_existe = True
                            break
                        else:
                            manutencao_existe = False
                    
                    # Se a manutenção existir, o programa irá prosseguir e removê-la das manutenções agendadas,
                    # adicioná-la nas manutenções realizadas e criar uma nova manutenção automática.
                    # A data da nova manutenção automática tem como base a data de realização da manutenção
                    # com o incremento do prazo de validade da peça.
                    if manutencao_existe == True:
                        # Vai salvar a manutenção em uma lista, para que ela
                        # seja escrita nas manutenções realizadas.
                        manutencao_para_realizar = lista_manutencoes_agendadas[linha_da_manutencao]
                        Functions_P3.manipularCSV_ComLista(caminho_manutencoes_realizadas, 'append', 'utf8', manutencao_para_realizar)  
                        
                        # Vai calcular a data da nova manutenção.
                        # Primeiramente, vai formatar a data antiga em uma variável.
                        data_manutencao_antiga = manutencao_para_realizar[6]
                        # Vai separar o dia, mês e ano.
                        if data_manutencao_antiga[-8] == '/': # Vai verificar se a data tem zeros.
                            dia_antiga = int(data_manutencao_antiga[-10:len(data_manutencao_antiga)-8])
                            mes_antiga = int(data_manutencao_antiga[-7:len(data_manutencao_antiga)-5])
                        else:
                            dia_antiga = int(data_manutencao_antiga[-9:len(data_manutencao_antiga)-7])
                            mes_antiga = int(data_manutencao_antiga[-6:len(data_manutencao_antiga)-5])
                        ano_antiga = int(data_manutencao_antiga[-4:len(data_manutencao_antiga)])
                        # Vai colocar a data antiga no formato do "datetime".
                        data_manutencao_antiga = datetime.date(ano_antiga, mes_antiga, dia_antiga)
                        # Vai verificar o tipo do prazo de validade da peça.
                        if manutencao_para_realizar[4] == 'Dias':
                            incremento_dias = int(manutencao_para_realizar[5])
                        elif manutencao_para_realizar[4] == 'Meses':
                            incremento_dias = int(manutencao_para_realizar[5]) * 30
                        elif manutencao_para_realizar[4] == 'Anos':
                            incremento_dias = int(manutencao_para_realizar[5]) * 375
                        # Vai incrementar a validade e criar a data da nova manutenção.
                        nova_data = data_manutencao_antiga + datetime.timedelta(days=incremento_dias)
                        manutencao_para_realizar[6] = f'{nova_data.day}/{nova_data.month}/{nova_data.year}'
                        
                        # Vai remover a manutenção do arquivo de manutenções agendadas
                        # e criar uma nova manutenção automática.
                        lista_manutencoes_agendadas.pop(linha_da_manutencao) # Vai remover a manutenção antiga.
                        lista_manutencoes_agendadas.append(manutencao_para_realizar) # Vai adicionar a manutenção nova.
                        # Vai estruturar o arquivo .csv.
                        EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                        'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                        'Data para a Manutenção - DD/MM/AAAA']
                        Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'write', 'utf8', EstruturaCSV)
                        # Vai copiar cada linha da matriz "lista_manutencoes_agendadas" para o arquivo "Manutenções_Agendadas.csv".
                        for manutencoes in range(1, len(lista_manutencoes_agendadas)):
                            todos_dados_manutencao = []
                            for dados_manutencao in range(7):
                                todos_dados_manutencao.append(lista_manutencoes_agendadas[manutencoes][dados_manutencao])
                            Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas, 'append', 'utf8', todos_dados_manutencao)
                        # Vai retornar ao menu.
                        os.system('cls')
                        print(f'\nManutenção realizada com sucesso!\n')
                        print(f'Nova manutenção da peça "{manutencao_para_realizar[2]}", do cliente "{manutencao_para_realizar[1]}", '
                              f'marcada para a seguinte data: {manutencao_para_realizar[6]}')
                        print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                        keyboard.wait('space')
                    
                    # Vai apresentar um erro se a manutenção agendada não existir.
                    else:
                        os.system('cls')
                        print('\nNão constam dados dessa manutenção na lista de manutenções agendadas!\n')
                        sleep(3)
            
            # Vai exibir a lista de manutenções agendadas e realizadas.
            elif menu_manutencoes_options == 5:
                # Vai verificar se existem manutenções agendadas.
                try:
                    tem_agendadas = int(lista_manutencoes_agendadas[1][0])
                    tem_agendadas = True
                except (IndexError, ValueError):
                    tem_agendadas = False
                
                # Vai verificar se existem manutenções realizadas.
                try:
                    tem_realizadas = int(lista_manutencoes_realizadas[1][0])
                    tem_realizadas = True
                except (IndexError, ValueError):
                    tem_realizadas = False

                # Vai perguntar quais dados o usuário deseja listar no terminal.
                on_menu_listagem = True
                while on_menu_listagem == True:
                    os.system('cls')
                    try:
                        tipo_manutencao = int(input('\nEscolha o que deseja listar:'
                                                    '\n1. Manutenções Agendadas.'
                                                    '\n2. Manutenções Realizadas.'
                                                    '\n3. Manutenções Agendadas e Realizadas.\n'
                                                    '\n4. Voltar ao menu anterior.\n'
                                                    '\nSua escolha: '))
                        assert tipo_manutencao > 0 and tipo_manutencao < 5
                        on_menu_listagem = False
                    except (ValueError, AssertionError):
                        os.system('cls')
                        print('\nOpção inválida!\n')
                        sleep(2)
                
                # Vai listar as manutenções agendadas, se a opção "1" for selecionada.
                if tipo_manutencao == 1:
                    # Vai prosseguir se existirem manutenções agendadas.
                    if tem_agendadas == True:
                        try:
                            os.system('cls')
                            print('\nManutenções Agendadas:\n')
                            for manutencao in range(1, len(lista_manutencoes_agendadas)):
                                    print(f'\nCódigo da Manutenção: {lista_manutencoes_agendadas[manutencao][0]}'
                                        f'\nID do Cliente: {lista_manutencoes_agendadas[manutencao][1]}'
                                        f'\nPreço: {lista_manutencoes_agendadas[manutencao][2]}'
                                        f'\nNome da Peça: {lista_manutencoes_agendadas[manutencao][3]}'
                                        f'\nTipo de Validade: {lista_manutencoes_agendadas[manutencao][4]}, '
                                        f'Validade: {lista_manutencoes_agendadas[manutencao][5]}'
                                        f'\nData para a Manutenção (DD/MM/AAAA): {lista_manutencoes_agendadas[manutencao][6]}')
                                    print('\n')
                            print('Pressione a tecla "Espaço" no teclado, para prosseguir.\n')
                            keyboard.wait('space')
                        # Vai apresentar um erro se os dados de alguma manutenção, no arquivo
                        # "Manutenções_Agendadas.csv", estiverem incompletos.
                        except IndexError:
                            os.system('cls')
                            print(f'\nOs dados da manutenção "{lista_manutencoes_agendadas[manutencao][0]}" estão incompletos '
                                    'e prejudicaram a listagem das manutenções agendadas!\n')
                            print('Verifique e corrija o arquivo "Manutenções_Agendadas.csv"!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para prosseguir.\n')
                            keyboard.wait('space')
                    # Vai apresentar um erro se não existir nenhuma manutenção agendada.
                    else:
                        os.system('cls')
                        print('\nAinda não existem manutenções agendadas!\n')
                        sleep(2)

                # Vai listar as manutenções realizadas, se a opção "2" for selecionada.
                elif tipo_manutencao == 2:
                    # Vai prosseguir se existirem manutenções realizadas.
                    if tem_realizadas == True:
                        try:
                            os.system('cls')
                            print('\nManutenções Realizadas:\n')
                            for manutencao in range(1, len(lista_manutencoes_realizadas)):
                                    print(f'\nCódigo da Manutenção: {lista_manutencoes_realizadas[manutencao][0]}'
                                        f'\nID do Cliente: {lista_manutencoes_realizadas[manutencao][1]}'
                                        f'\nPreço: {lista_manutencoes_realizadas[manutencao][2]}'
                                        f'\nNome da Peça: {lista_manutencoes_realizadas[manutencao][3]}'
                                        f'\nTipo de Validade: {lista_manutencoes_realizadas[manutencao][4]}, '
                                        f'Validade: {lista_manutencoes_realizadas[manutencao][5]}'
                                        f'\nData de Conclusão da Manutenção (DD/MM/AAAA): {lista_manutencoes_realizadas[manutencao][6]}')
                                    print('\n')
                            print('Pressione a tecla "Espaço" no teclado, para prosseguir.\n')
                            keyboard.wait('space')
                        # Vai apresentar um erro se os dados de alguma manutenção, no arquivo
                        # "Manutenções_Realizadas.csv", estiverem incompletos.
                        except IndexError:
                            os.system('cls')
                            print(f'\nOs dados da manutenção "{lista_manutencoes_realizadas[manutencao][0]}" estão incompletos '
                                    'e prejudicaram a listagem das manutenções realizadas!\n')
                            print('Verifique e corrija o arquivo "Manutenções_Realizadas.csv"!\n')
                            print('\nPressione a tecla "Espaço" no teclado, para prosseguir.\n')
                            keyboard.wait('space')  
                    # Vai apresentar um erro se não existir nenhuma manutenção realizada.
                    else:
                        os.system('cls')
                        print('\nAinda não existem manutenções realizadas!\n')
                        sleep(2)

                # Vai listar as manutenções agendadas e realizadas, se a opção "3" for selecionada.
                elif tipo_manutencao == 3:
                    # Vai prosseguir se existirem manutenções agendadas.
                    if tem_agendadas == True:
                        # Vai prosseguir se existirem manutenções realizadas.
                        if tem_realizadas == True:
                            try:
                                os.system('cls')
                                print('\nManutenções Agendadas:\n')
                                for manutencao in range(1, len(lista_manutencoes_agendadas)):
                                        print(f'\nCódigo da Manutenção: {lista_manutencoes_agendadas[manutencao][0]}'
                                            f'\nID do Cliente: {lista_manutencoes_agendadas[manutencao][1]}'
                                            f'\nPreço: {lista_manutencoes_agendadas[manutencao][2]}'
                                            f'\nNome da Peça: {lista_manutencoes_agendadas[manutencao][3]}'
                                            f'\nTipo de Validade: {lista_manutencoes_agendadas[manutencao][4]}, '
                                            f'Validade: {lista_manutencoes_agendadas[manutencao][5]}'
                                            f'\nData para a Manutenção (DD/MM/AAAA): {lista_manutencoes_agendadas[manutencao][6]}')
                                        print('\n')
                            # Vai apresentar um erro se os dados de alguma manutenção, no arquivo
                            # "Manutenções_Agendadas.csv", estiverem incompletos.
                            except IndexError:
                                os.system('cls')
                                print(f'\nOs dados da manutenção "{lista_manutencoes_agendadas[manutencao][0]}" estão incompletos '
                                        'e prejudicaram a listagem das manutenções agendadas e realizadas!\n')
                                print('Verifique e corrija o arquivo "Manutenções_Agendadas.csv"!\n')
                                print('\nPressione a tecla "Espaço" no teclado, para prosseguir.\n')
                                keyboard.wait('space')
                            
                            try:
                                print('\nManutenções Realizadas:\n')
                                for manutencao in range(1, len(lista_manutencoes_realizadas)):
                                        print(f'\nCódigo da Manutenção: {lista_manutencoes_realizadas[manutencao][0]}'
                                            f'\nID do Cliente: {lista_manutencoes_realizadas[manutencao][1]}'
                                            f'\nPreço: {lista_manutencoes_realizadas[manutencao][2]}'
                                            f'\nNome da Peça: {lista_manutencoes_realizadas[manutencao][3]}'
                                            f'\nTipo de Validade: {lista_manutencoes_realizadas[manutencao][4]}, '
                                            f'Validade: {lista_manutencoes_realizadas[manutencao][5]}'
                                            f'\nData de Conclusão da Manutenção (DD/MM/AAAA): {lista_manutencoes_realizadas[manutencao][6]}')
                                        print('\n')
                                print('Pressione a tecla "Espaço" no teclado, para prosseguir.\n')
                                keyboard.wait('space')
                            # Vai apresentar um erro se os dados de alguma manutenção, no arquivo
                            # "Manutenções_Realizadas.csv", estiverem incompletos.
                            except IndexError:
                                os.system('cls')
                                print(f'\nOs dados da manutenção "{lista_manutencoes_realizadas[manutencao][0]}" estão incompletos '
                                        'e prejudicaram a listagem das manutenções agendadas e realizadas!\n')
                                print('Verifique e corrija o arquivo "Manutenções_Realizadas.csv"!\n')
                                print('\nPressione a tecla "Espaço" no teclado, para prosseguir.\n')
                                keyboard.wait('space') 
                        # Vai apresentar um erro se não existir nenhuma manutenção realizada.
                        else:
                            os.system('cls')
                            print('\nAinda não existem manutenções realizadas!\n')
                            sleep(2)
                    # Vai apresentar um erro se não existir nenhuma manutenção agendada.
                    else:
                        os.system('cls')
                        print('\nAinda não existem manutenções agendadas!\n')
                        sleep(2)

                # Vai voltar ao menu anterior, se a opção "4" for selecionada no sub-menu
                # de listagem das manutenções.
                elif tipo_manutencao == 4:
                    os.system('cls')
                    print("\nVoltando ao menu anterior...\n")
                    sleep(2)
            
            # Vai salvar a lista de manutenções agendadas, ordenadas por data mais próxima, em um arquivo.
            elif menu_manutencoes_options == 6:
                # Esse bloco vai ordenar as manutenções por data mais próxima.
                # Primeiramente vai enviar as datas de cada manutenção para uma lista.
                # Essa lista vai ser usada como referência (índice) para ordenar
                # a matriz 'lista_manutencoes_agendadas_ordenadas'.
                datas_ordenadas = [] # As datas ficarão salvas nessa lista.
                for manutencao in range(1, len(lista_manutencoes_agendadas)):
                    datas_ordenadas.append(lista_manutencoes_agendadas[manutencao][6]) # Vai inserir as datas na lista.
                # Depois vai ordenar as datas que vão estar contidos na lista.
                # Referência do método de ordenação (Insertion Sort):
                # Máteria: Algoritmos e Programação I, Professora: Claudia P. Pereira
                # Link: https://drive.google.com/file/d/1Hu6HUsfCNfRhaMRwm-Ysh_lw_B_1m22t/view
                # Acesso em: 06 de Junho de 2021
                # Com um incremento da biblioteca "datetime", para comparar datas.
                continuar_ordenacao = True # Vai ser usada para avisar ao programa se as datas estão corretas.
                try:
                    t = len(datas_ordenadas)
                    for i in range(1, t):
                        # Vai salvar o dia, mês e ano, da variável "aux", em variáveis.
                        data_aux = datas_ordenadas[i]
                        if data_aux[-8] == '/': # Vai verificar se a data tem zeros.
                            dia_aux = int(data_aux[-10:len(data_aux)-8])
                            mes_aux = int(data_aux[-7:len(data_aux)-5])
                        else:
                            dia_aux = int(data_aux[-9:len(data_aux)-7])
                            mes_aux = int(data_aux[-6:len(data_aux)-5])
                        ano_aux = int(data_aux[-4:len(data_aux)])
                        # Vai salvar o dia, mês e ano, da variável "j", em variáveis.
                        data_j = datas_ordenadas[i-1]
                        if data_j[-8] == '/': # Vai verificar se a data tem zeros.
                            dia_j = int(data_j[-10:len(data_j)-8])
                            mes_j = int(data_j[-7:len(data_j)-5])
                        else:
                            dia_j = int(data_j[-9:len(data_j)-7])
                            mes_j = int(data_j[-6:len(data_j)-5])
                        ano_j = int(data_j[-4:len(data_j)])
                        # Vai seguir com o "Insertion Sort".
                        aux = datas_ordenadas[i]
                        j = i - 1
                        # Referência do incremento do datetime: https://www.delftstack.com/pt/howto/python/python-compare-dates/
                        # Acesso em: 06 de junho de 2021.
                        while j >= 0 and datetime.date(ano_aux, mes_aux, dia_aux) < datetime.date(ano_j, mes_j, dia_j):
                            datas_ordenadas[j+1] = datas_ordenadas [j]
                            j -= 1
                        datas_ordenadas[j+1] = aux
                # Vai dizer ao programa que alguma data está incorreta,
                # e ele vai interromper o salvamento em arquivo.
                except ValueError:
                    continuar_ordenacao = False
                
                # Vai continuar, se todas as datas forem válidas.
                if continuar_ordenacao == True:
                    # Uma matriz ordenada será criada, a partir dos elementos da matriz
                    # 'lista_manutencoes_agendadas', tendo como base a ordem da lista 'datas_ordenadas'
                    lista_manutencoes_agendadas_ordenadas = [] # Essa será a matriz ordenada.
                    for linha in range(1, len(lista_manutencoes_agendadas)):
                        lista_manutencoes_agendadas_ordenadas.append(['']) # Criando cada linha da matriz, em branco.
                    # Inserindo as informações das manutenções, usando a ordem da lista 'datas_ordenadas'.
                    for manutencao in range(1, len(lista_manutencoes_agendadas)):
                        for informacao in range(len(datas_ordenadas)):
                            if lista_manutencoes_agendadas[manutencao][6] == datas_ordenadas[informacao]:
                                lista_manutencoes_agendadas_ordenadas[informacao] = lista_manutencoes_agendadas[manutencao]
                    # Vai verificar qual o sistema operacional e criar o endereço para o diretório do arquivo,
                    # de acordo com cada sistema e data de criação do arquivo.
                    if sistema_operacional == 'Windows':
                        data_hoje = datetime.date.today()
                        caminho_manutencoes_agendadas_ordenadas = f'Arquivos do Usuário\Manutenções Agendadas Ordenadas (Criado em {data_hoje.day}-{data_hoje.month}-{data_hoje.year}).csv'
                    elif sistema_operacional == 'Linux':
                        caminho_manutencoes_agendadas_ordenadas = f'Arquivos do Usuário/Manutenções Agendadas Ordenadas (Criado em {data_hoje.day}-{data_hoje.month}-{data_hoje.year}).csv'
                    EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço', 'Nome da Peça',
                                    'Tipo de Validade', 'Validade da Peça', 'Data para a Manutenção - DD/MM/AAAA']
                    Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas_ordenadas, 'write', 'utf8', EstruturaCSV)
                    # Vai copiar cada linha da matriz "lista_manutencoes_agendadas_ordenadas" para o arquivo.
                    for manutencoes in range(len(lista_manutencoes_agendadas_ordenadas)):
                        todos_dados_manutencao = []
                        for dados_manutencao in range(7):
                            todos_dados_manutencao.append(lista_manutencoes_agendadas_ordenadas[manutencoes][dados_manutencao])
                        Functions_P3.manipularCSV_ComLista(caminho_manutencoes_agendadas_ordenadas, 'append', 'utf8', todos_dados_manutencao)
                    os.system('cls')
                    print(f'\nArquivo de manutenções agendadas, ordenadas por datas, criado com sucesso!\n')
                    print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                    keyboard.wait('space')
                
                # Vai apresentar um erro, se alguma data for inválida.
                else:
                    os.system('cls')
                    print('\nExistem datas inválidas e elas prejudicaram a ordenação!\n')
                    print('Verifique o arquivo "Manutenções_Agendadas.csv"!\n')
                    sleep(4)

            # Vai sair do sub-menu de manutenções.
            elif menu_manutencoes_options == 7:
                os.system('cls') # Vai limpar o terminal.
                print("\nVoltando ao Menu Principal...\n")
                on_menu_manutencoes = False
                sleep(2) # Vai esperar dois segundos até prosseguir.
            
            # Condição de opção inválida digitada no sub-menu de manutenções.
            else:
                os.system('cls') # Vai limpar o terminal.
                print("\nOpção Inválida!\n")
                sleep(2) # Vai esperar dois segundos até prosseguir.
    
    # Sub-menu onde será possivel exibir o balanço de manutenções realizadas em um determinado mês.
    elif start_menu_options == 3:
        # Vai verificar se existem manutenções realizadas.
        try:
            tem_realizadas = int(lista_manutencoes_realizadas[1][0])
            tem_realizadas = True
        except (IndexError, ValueError):
            tem_realizadas = False
        
        # Vai continuar se ao menos uma manutenção já tiver sido realizada.
        if tem_realizadas == True:
            # Definindo algumas variáveis e pedindo algumas informações ao usuário.
            balanco_manutencoes_realizadas = [] # Essa lista será usada para criar o arquivo do balanço do mês.
            balanco_preco_total = 0 # Vai somar o valor total de todas as manutenções do mês.
            # Vai perguntar o mês que o cliente quer listar.
            on_balanco_mes = True
            while on_balanco_mes == True:
                os.system('cls')
                try:
                    balanco_mes = int(input('\nDigite o mês: '))
                    assert balanco_mes > 0 and balanco_mes < 12
                    on_balanco_mes = False
                except (ValueError, AssertionError):
                    os.system('cls')
                    print('\nDigite um mês válido!\n')
                    sleep(2)
            # Vai perguntar o ano que o cliente quer listar.
            on_balanco_ano = True
            while on_balanco_ano == True:
                try:
                    balanco_ano = int(input('\nDigite o ano: '))
                    on_balanco_ano = False
                except ValueError:
                    os.system('cls')
                    print('\nDigite apenas números!\n')
                    sleep(2)
                    os.system('cls')
            
            # Irá exibir em tela os dados do balanço do mês.
            os.system('cls')
            print(f'\nBalanço das Manutenções Realizadas em {balanco_mes}/{balanco_ano}:')  
            for manutencao in range(1, len(lista_manutencoes_realizadas)):
                # Vai copiar a data da manutenção realizada, dentro da matriz.
                data_manutencao = lista_manutencoes_realizadas[manutencao][6]
                # Vai verificar se o mês que consta no arquivo tem um digito ou dois
                # e depois vai copiá-lo para uma variável.
                if data_manutencao[-8] == '/':
                    mes_manutencao = int(data_manutencao[-7:len(data_manutencao)-5])
                else:
                    mes_manutencao = int(data_manutencao[-6:len(data_manutencao)-5])
                # Vai copiar o ano para uma variável.
                ano_manutencao = int(data_manutencao[-4:len(data_manutencao)])

                # Vai exibir as informações da manutenção, se a data de realização dela
                # atender a data informada pelo usuário.
                if mes_manutencao == balanco_mes and ano_manutencao == balanco_ano:
                    # Vai copiar os dados da manutenção para a lista que será usada
                    # para criar o arquivo do balanço do mês.
                    balanco_manutencoes_realizadas.append(lista_manutencoes_realizadas[manutencao])
                    # Vai somar o valor da manutenção ao valor total do balanço do mês.
                    balanco_preco_total += float(lista_manutencoes_realizadas[manutencao][2])
                    try:
                        print(f'\nCódigo da Manutenção: {lista_manutencoes_realizadas[manutencao][0]}'
                            f'\nID do Cliente: {lista_manutencoes_realizadas[manutencao][1]}'
                            f'\nPreço: {lista_manutencoes_realizadas[manutencao][2]}'
                            f'\nNome da Peça: {lista_manutencoes_realizadas[manutencao][3]}'
                            f'\nTipo de Validade: {lista_manutencoes_realizadas[manutencao][4]}, '
                            f'Validade: {lista_manutencoes_realizadas[manutencao][5]}'
                            f'\nData de Conclusão da Manutenção (DD/MM/AAAA): {lista_manutencoes_realizadas[manutencao][6]}')
                    # Vai apresentar um erro se os dados de alguma manutenção, no arquivo
                    # "Manutenções_Realizadas.csv", estiverem incompletos.
                    except IndexError:
                        os.system('cls')
                        print(f'\nOs dados da manutenção "{lista_manutencoes_realizadas[manutencao][0]}" estão incompletos '
                                'e prejudicaram a listagem do balanço do mês!\n')
                        print('Verifique e corrija o arquivo "Manutenções_Realizadas.csv"!\n')
                        print('\nPressione a tecla "Espaço" no teclado, para prosseguir.\n')
                        keyboard.wait('space')
                        break # Vai quebrar o "if", para voltar ao menu.
            print(f'\nValor total das manutenções realizadas: {balanco_preco_total}\n')
            print('\nPressione a tecla "Espaço" no teclado, para prosseguir.\n')
            keyboard.wait('space')

            # Bloco de salvamento do balanço do mês em um arquivo de texto.
            os.system('cls')
            # Vai pedir permissão para salvar o balanço do mês em um arquivo.
            on_menu_salvar_balanco = True
            while on_menu_salvar_balanco == True:
                try:
                    salvar_arquivo = int(input(f'\nDeseja salvar o balanço das manutenções de {balanco_mes}/{balanco_ano} em um arquivo?'
                                                '\n1. SIM.'
                                                '\n2. NÃO.\n'
                                                '\nSua escolha: '))
                    assert salvar_arquivo > 0 and salvar_arquivo < 3
                    on_menu_salvar_balanco = False
                except (ValueError, AssertionError):
                    os.system('cls')
                    print('\nOpção Inválida!\n')
                    sleep(2)
                    os.system('cls')
            
            # Vai salvar os dados em um arquivo, se a permissão for concedida.
            if salvar_arquivo == 1:
                # Vai definir o caminho e nome do arquivo, de acordo com o sistema operacional.
                if sistema_operacional == 'Windows':
                    caminho_arquivo_balanco = f'Arquivos do Usuário\Balanço do Mês ({balanco_mes}-{balanco_ano}).csv'
                elif sistema_operacional == 'Linux':
                    caminho_arquivo_balanco = f'Arquivos do Usuário/Balanço do Mês ({balanco_mes}-{balanco_ano}).csv'
                # Vai criar o layout do arquivo .csv.
                EstruturaCSV = ['Código da Manutenção','Código do Cliente','Preço',
                                'Nome da Peça', 'Tipo de Validade', 'Validade da Peça',
                                'Data de Conclusão da Manutenção - DD/MM/AAAA']
                Functions_P3.manipularCSV_ComLista(caminho_arquivo_balanco, 'write', 'utf8', EstruturaCSV)
                # Vai copiar cada linha da matriz "balanco_manutencoes_realizadas" para o arquivo.
                for manutencoes in range(len(balanco_manutencoes_realizadas)):
                    todos_dados_manutencao = []
                    for dados_manutencao in range(7):
                        todos_dados_manutencao.append(balanco_manutencoes_realizadas[manutencoes][dados_manutencao])
                    Functions_P3.manipularCSV_ComLista(caminho_arquivo_balanco, 'append', 'utf8', todos_dados_manutencao)
                os.system('cls')
                print(f'\nOs dados foram salvos com sucesso!\n')
                print('\nPressione a tecla "Espaço" no teclado, para continuar e voltar ao menu anterior.\n')
                keyboard.wait('space')
            
            # Vai apresentar um erro se a permissão de gravação em arquivo for negada.
            else:
                os.system('cls')
                print('\nPermissão negada!\n'
                        'O balanço do mês não será salvo em um arquivo!\n')
                sleep(2)

        # Vai apresentar um erro, se nenhuma manutenção tiver sido
        # realizada ainda. 
        else:
            os.system('cls')
            print(f'\nNenhuma manutenção foi realizada ainda!\n')
            sleep(2)
    
    # Vai sair do programa, se a opção "4" for selecionada.
    elif start_menu_options == 4:
        os.system('cls')
        print("\nAté mais!\n")
        exit()

    # Vai entrar nessa condição, se uma opção inválida for digitada no menu.
    else:
        os.system('cls')
        print('\nEssa opção não existe!\n')
        sleep(2) # Vai esperar dois segundos até voltar ao menu.