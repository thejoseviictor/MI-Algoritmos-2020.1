#/*******************************************************************************
#Autor: José Victor de Oliveira Correia
#Componente Curricular: Algoritmos I
#Concluido em: 03/03/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

#Sistema de controle das aplicações de vacinas contra a COVID-19
#e produção de suas estatísticas em Feira de Santana.

#Essas variáveis serão usadas para armazenar os dados das pessoas vacinadas
#e também serão usadas na exibição as estatísticas e seus cálculos.
masculino = 0
feminino = 0
doses = 0
dose_1 = 0
dose_2 = 0
vacinados_coronavac = 0
vacinados_oxford = 0
idosos_vacinados = 0
manha = 0
tarde = 0

#O usuário vai escolher o que deseja fazer no sistema. Caso escolha uma opção errada entrará no loop!
print('Bem-vindo ao Sistema de Controle das Aplicações de Vacinas\ncontra a COVID-19 em Feira de Santana - BA')
print('\nEntre as opções abaixo, escolha a que corresponde ao você deseja fazer no sistema:')
print('1. Registrar vacinação de um nova pessoa ao sistema\n2. Ver estatísticas de vacinação em Feira de Santana')
opcao_entrada = int(input('\nDigite o número da opção desejada:\n'))

#Entrando no loop da opção incorreta
while opcao_entrada == 0 or opcao_entrada > 3:
    print('\nDigite um número válido!\n')
    print('Entre as opções abaixo, escolha a que corresponde ao você deseja fazer no sistema:')
    print('1. Registrar vacinação de um nova pessoa ao sistema\n2. Ver estatísticas de vacinação em Feira de Santana')
    opcao_entrada = int(input('\nDigite o número da opção desejada:\n'))

#Entrando no loop da opção correta
while opcao_entrada > 0 and opcao_entrada < 4:
    #Nesta seção serão registrados dados de vacinação.
    if opcao_entrada == 1: 
        print('\nEscolha o local de vacinação, dentre as opções abaixo:')
        print('1. Hospital Geral Clériston Andrade')
        local = int(input('\nSua escolha:\n'))
    
        if local == 1:

            #O usuário vai escolher qual foi o fabricante da vacina aplicada.
            print('\nQual a fabricante da vacina?\nCoronavac\nAstrazeneca')
            fabricante = str(input('\nSua escolha:\n'))

            #A partir daqui, serão cadastradas as pessoas que receberam a vacina "Coronavac".
            if fabricante == 'Coronavac' or fabricante == 'coronavac' or fabricante == 1:

                #Vai perguntar ao usuário em qual dose ele quer adicionar dados de vacinação.
                print('\nQual a dose?\n1ª Dose\n2ª Dose')
                coronavac_dose = int(input('\nDigite 1 ou 2:\n'))

                #Adicionar cidadão que recebeu a 1ª dose da Coronavac.
                if coronavac_dose == 1:

                    #Vai definir o lote da vacina que foi usado.
                    print('\nQual o lote da vacina?\n1')
                    coronavac_dose1_lote = int(input('\nDigite o número do lote:\n'))
                    if coronavac_dose1_lote == 1:
                        print('\nA pessoa pertence a algum grupo prioritário?')
                        prioritario = str(input())

                        #vai adicionar dados de vacinação de uma pessoa que pertence a algum grupo prioritário.
                        if prioritario == 'Sim' or prioritario == 'sim' or prioritario == 's':
                            print('\nA qual grupo prioritário a pessoa pertence?\nProfissionais de Saúde.\nIdosos\nComorbidades')
                            print('Professores.\nForças de Segurança e Salvamento, Policia Rodoviária Federal\nFuncionários do Sistema Priosional')
                            print('Transporte Coletivo.\nPessoa com Deficiência\nTransportes e Rodoviários de Carga')
                            print('Privados de Liberdade, Adolescentes e Jovens sob medida socioeducativa\n')
                            qual_grupo_prioritario = input('Escolha uma opção:\n')

                            #vai adicionar dados de vacinação de uma pessoa idosa
                            if qual_grupo_prioritario == 'idosos' or qual_grupo_prioritario == 'Idosos':
                                print('\nQual o sexo da pessoa?')
                                sexo = str(input())
                                #adicionar cidadão idoso do sexo masculino que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose1_lote_nomes_idosos_masculino = open('coronavac_dose1_lote_nomes_idosos_masculino.txt', 'a')
                                    coronavac_dose1_lote_nomes_idosos_masculino.write(input() + '\n')
                                    coronavac_dose1_lote_nomes_idosos_masculino.close()
                                    masculino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_coronavac += 1
                                    idosos_vacinados += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã idosa do sexo feminino que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose1_lote_nomes_idosas_feminino = open('coronavac_dose1_lote_nomes_idosas_feminino.txt', 'a')
                                    coronavac_dose1_lote_nomes_idosas_feminino.write(input() + '\n')
                                    coronavac_dose1_lote_nomes_idosas_feminino.close()
                                    feminino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_coronavac += 1
                                    idosos_vacinados += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')

                            #vai adicionar dados de vacinação de uma pessoa de qualquer outro grupo prioritário
                            else:
                                print('\nQual o sexo da pessoa?')
                                sexo = str(input())
                                #adicionar cidadão do sexo masculino, com prioridade, que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose1_lote_nomes_prioridade_masculino = open('coronavac_dose1_lote_nomes_prioridade_masculino.txt', 'a')
                                    coronavac_dose1_lote_nomes_prioridade_masculino.write(input() + '\n')
                                    coronavac_dose1_lote_nomes_prioridade_masculino.close()
                                    masculino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_coronavac += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã do sexo feminino, com prioridade, que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose1_lote_nomes_prioridade_feminino = open('coronavac_dose1_lote_nomes_prioridade_feminino.txt', 'a')
                                    coronavac_dose1_lote_nomes_prioridade_feminino.write(input() + '\n')
                                    coronavac_dose1_lote_nomes_prioridade_feminino.close()
                                    feminino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_coronavac += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')

                        #vai adicionar dados de vacinação de uma pessoa que NÃO pertence a nenhum grupo prioritário.
                        elif prioritario == 'Não' or prioritario == 'não' or prioritario == 'Nao' or prioritario == 'nao' or prioritario == 'n':
                            print('\nQual o sexo da pessoa?')
                            sexo = str(input())

                            #adicionar cidadão do sexo masculino, sem prioridade, que foi vacinado.
                            if sexo == 'Masculino' or sexo == 'masculino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                coronavac_dose1_lote_nomes_np_masculino = open('coronavac_dose1_lote_nomes_np_masculino.txt', 'a')
                                coronavac_dose1_lote_nomes_np_masculino.write(input() + '\n')
                                coronavac_dose1_lote_nomes_np_masculino.close()
                                masculino += 1
                                doses += 1
                                dose_1 += 1
                                vacinados_coronavac += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                
                            #adicionar cidadã do sexo feminino, sem prioridade, que foi vacinada.
                            elif sexo == 'Feminino' or  sexo == 'feminino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                coronavac_dose1_lote_nomes_np_feminino = open('coronavac_dose1_lote_nomes_np_feminino.txt', 'a')
                                coronavac_dose1_lote_nomes_np_feminino.write(input() + '\n')
                                coronavac_dose1_lote_nomes_np_feminino.close()
                                feminino += 1
                                doses += 1
                                dose_1 += 1
                                vacinados_coronavac += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                    
                #Adicionar cidadão que recebeu a 2ª dose da Coronavac.
                elif coronavac_dose == 2:

                    #Vai definir o lote da vacina que foi usado.
                    print('\nQual o lote da vacina?\n1')
                    coronavac_dose2_lote = int(input('\nDigite o número do lote:\n'))
                    if coronavac_dose2_lote == 1:
                        print('\nA pessoa pertence a algum grupo prioritário?')
                        prioritario = str(input())

                        #vai adicionar dados de vacinação de uma pessoa que pertence a algum grupo prioritário.
                        if prioritario == 'Sim' or prioritario == 'sim' or prioritario == 's':
                            print('\nA qual grupo prioritário a pessoa pertence?\nProfissionais de Saúde.\nIdosos\nComorbidades')
                            print('Professores.\nForças de Segurança e Salvamento, Policia Rodoviária Federal\nFuncionários do Sistema Priosional')
                            print('Transporte Coletivo.\nPessoa com Deficiência\nTransportes e Rodoviários de Carga')
                            print('Privados de Liberdade, Adolescentes e Jovens sob medida socioeducativa\n')
                            qual_grupo_prioritario = input('Escolha uma opção:\n')

                            #vai adicionar dados de vacinação de uma pessoa idosa
                            if qual_grupo_prioritario == 'idosos' or qual_grupo_prioritario == 'Idosos':
                                print('\nQual o sexo doa pessoa?')
                                sexo = str(input())
                                #adicionar cidadão idoso do sexo masculino que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose2_lote_nomes_idosos_masculino = open('coronavac_dose2_lote_nomes_idosos_masculino.txt', 'a')
                                    coronavac_dose2_lote_nomes_idosos_masculino.write(input() + '\n')
                                    coronavac_dose2_lote_nomes_idosos_masculino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã idosa do sexo feminino que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose2_lote_nomes_idosas_feminino = open('coronavac_dose2_lote_nomes_idosas_feminino.txt', 'a')
                                    coronavac_dose2_lote_nomes_idosas_feminino.write(input() + '\n')
                                    coronavac_dose2_lote_nomes_idosas_feminino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')


                            #vai adicionar dados de vacinação de uma pessoa de qualquer outro grupo prioritário
                            else:
                                print('\nQual o sexo da pessoa?')
                                sexo = str(input())
                                #adicionar cidadão do sexo masculino, com prioridade, que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose2_lote_nomes_prioridade_masculino = open('coronavac_dose2_lote_nomes_prioridade_masculino.txt', 'a')
                                    coronavac_dose2_lote_nomes_prioridade_masculino.write(input() + '\n')
                                    coronavac_dose2_lote_nomes_prioridade_masculino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã do sexo feminino, com prioridade, que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    coronavac_dose2_lote_nomes_prioridade_feminino = open('coronavac_dose2_lote_nomes_prioridade_feminino.txt', 'a')
                                    coronavac_dose2_lote_nomes_prioridade_feminino.write(input() + '\n')
                                    coronavac_dose2_lote_nomes_prioridade_feminino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')

                        #vai adicionar dados de vacinação de uma pessoa que NÃO pertence a nenhum grupo prioritário.
                        elif prioritario == 'Não' or prioritario == 'não' or prioritario == 'Nao' or prioritario == 'nao' or prioritario == 'n':
                            print('\nQual o sexo da pessoa?')
                            sexo = str(input())

                            #adicionar cidadão do sexo masculino, sem prioridade, que foi vacinado.
                            if sexo == 'Masculino' or sexo == 'masculino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                coronavac_dose2_lote_nomes_np_masculino = open('coronavac_dose2_lote_nomes_np_masculino.txt', 'a')
                                coronavac_dose2_lote_nomes_np_masculino.write(input() + '\n')
                                coronavac_dose2_lote_nomes_np_masculino.close()
                                doses += 1
                                dose_2 += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                
                            #adicionar cidadã do sexo feminino, sem prioridade, que foi vacinada.
                            elif sexo == 'Feminino' or  sexo == 'feminino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                coronavac_dose2_lote_nomes_np_feminino = open('coronavac_dose2_lote_nomes_np_feminino.txt', 'a')
                                coronavac_dose2_lote_nomes_np_feminino.write(input() + '\n')
                                coronavac_dose2_lote_nomes_np_feminino.close()
                                doses += 1
                                dose_2 += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                
            #A partir daqui, serão cadastradas as pessoas que receberam a vacina "Astrazeneca (OXFORD)".
            elif fabricante == 'Astrazeneca' or fabricante == 'astrazeneca' or fabricante == 2:

                #Vai perguntar ao usuário em qual dose ele quer adicionar dados de vacinação.
                print('\nQual a dose?\n1ª Dose\n2ª Dose')
                oxford_dose = int(input('\nDigite 1 ou 2:\n'))

                #Adicionar cidadão que recebeu a 1ª dose da Astrazeneca.
                if oxford_dose == 1:

                    #Vai definir o lote da vacina que foi usado.
                    print('\nQual o lote da vacina?\n1')
                    oxford_dose1_lote = int(input('\nDigite o número do lote:\n'))
                    if oxford_dose1_lote == 1:
                        print('\nA pessoa pertence a algum grupo prioritário?')
                        prioritario = str(input())

                        #vai adicionar dados de vacinação de uma pessoa que pertence a algum grupo prioritário.
                        if prioritario == 'Sim' or prioritario == 'sim' or prioritario == 's':
                            print('\nA qual grupo prioritário a pessoa pertence?\nProfissionais de Saúde.\nIdosos\nComorbidades')
                            print('Professores.\nForças de Segurança e Salvamento, Policia Rodoviária Federal\nFuncionários do Sistema Priosional')
                            print('Transporte Coletivo.\nPessoa com Deficiência\nTransportes e Rodoviários de Carga')
                            print('Privados de Liberdade, Adolescentes e Jovens sob medida socioeducativa\n')
                            qual_grupo_prioritario = input('Escolha uma opção:\n')

                            #vai adicionar dados de vacinação de uma pessoa idosa
                            if qual_grupo_prioritario == 2 or qual_grupo_prioritario == 'idosos' or qual_grupo_prioritario == 'Idosos':
                                print('\nQual o sexo da pessoa?')
                                sexo = str(input())
                                #adicionar cidadão idoso do sexo masculino que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose1_lote_nomes_idosos_masculino = open('oxford_dose1_lote_nomes_idosos_masculino.txt', 'a')
                                    oxford_dose1_lote_nomes_idosos_masculino.write(input() + '\n')
                                    oxford_dose1_lote_nomes_idosos_masculino.close()
                                    masculino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_oxford += 1
                                    idosos_vacinados += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã idosa do sexo feminino que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose1_lote_nomes_idosas_feminino = open('oxford_dose1_lote_nomes_idosas_feminino.txt', 'a')
                                    oxford_dose1_lote_nomes_idosas_feminino.write(input() + '\n')
                                    oxford_dose1_lote_nomes_idosas_feminino.close()
                                    feminino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_oxford += 1
                                    idosos_vacinados += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')


                            #vai adicionar dados de vacinação de uma pessoa de qualquer outro grupo prioritário
                            else:
                                print('\nQual o sexo da pessoa?')
                                sexo = str(input())
                                #adicionar cidadão do sexo masculino, com prioridade, que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose1_lote_nomes_prioridade_masculino = open('oxford_dose1_lote_nomes_prioridade_masculino.txt', 'a')
                                    oxford_dose1_lote_nomes_prioridade_masculino.write(input() + '\n')
                                    oxford_dose1_lote_nomes_prioridade_masculino.close()
                                    masculino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_oxford += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã do sexo feminino, com prioridade, que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose1_lote_nomes_prioridade_feminino = open('oxford_dose1_lote_nomes_prioridade_feminino.txt', 'a')
                                    oxford_dose1_lote_nomes_prioridade_feminino.write(input() + '\n')
                                    oxford_dose1_lote_nomes_prioridade_feminino.close()
                                    feminino += 1
                                    doses += 1
                                    dose_1 += 1
                                    vacinados_oxford += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')

                        #vai adicionar dados de vacinação de uma pessoa que NÃO pertence a nenhum grupo prioritário.
                        elif prioritario == 'Não' or prioritario == 'não' or prioritario == 'Nao' or prioritario == 'nao' or prioritario == 'n':
                            print('\nQual o sexo da pessoa?')
                            sexo = str(input())

                            #adicionar cidadão do sexo masculino, sem prioridade, que foi vacinado.
                            if sexo == 'Masculino' or sexo == 'masculino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                oxford_dose1_lote_nomes_np_masculino = open('oxford_dose1_lote_nomes_np_masculino.txt', 'a')
                                oxford_dose1_lote_nomes_np_masculino.write(input() + '\n')
                                oxford_dose1_lote_nomes_np_masculino.close()
                                masculino += 1
                                doses += 1
                                dose_1 += 1
                                vacinados_oxford += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                
                            #adicionar cidadã do sexo feminino, sem prioridade, que foi vacinada.
                            elif sexo == 'Feminino' or  sexo == 'feminino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                oxford_dose1_lote_nomes_np_feminino = open('oxford_dose1_lote_nomes_np_feminino.txt', 'a')
                                oxford_dose1_lote_nomes_np_feminino.write(input() + '\n')
                                oxford_dose1_lote_nomes_np_feminino.close()
                                feminino += 1
                                doses += 1
                                dose_1 += 1
                                vacinados_oxford += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                    
                #Adicionar cidadão que recebeu a 2ª dose da Astrazeneca.
                elif oxford_dose == 2:

                    #Vai definir o lote da vacina que foi usado.
                    print('\nQual o lote da vacina?\n1')
                    oxford_dose2_lote = int(input('\nDigite o número do lote:\n'))
                    if oxford_dose2_lote == 1:
                        print('\nA pessoa pertence a algum grupo prioritário?')
                        prioritario = str(input())

                        #vai adicionar dados de vacinação de uma pessoa que pertence a algum grupo prioritário.
                        if prioritario == 'Sim' or prioritario == 'sim' or prioritario == 's':
                            print('\nA qual grupo prioritário a pessoa pertence?\nProfissionais de Saúde.\nIdosos\nComorbidades')
                            print('Professores.\nForças de Segurança e Salvamento, Policia Rodoviária Federal\nFuncionários do Sistema Priosional')
                            print('Transporte Coletivo.\nPessoa com Deficiência\nTransportes e Rodoviários de Carga')
                            print('Privados de Liberdade, Adolescentes e Jovens sob medida socioeducativa\n')
                            qual_grupo_prioritario = input('Escolha uma opção:\n')

                            #vai adicionar dados de vacinação de uma pessoa idosa
                            if qual_grupo_prioritario == 2 or qual_grupo_prioritario == 'idosos' or qual_grupo_prioritario == 'Idosos':
                                print('\nQual o sexo doa pessoa?')
                                sexo = str(input())
                                #adicionar cidadão idoso do sexo masculino que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose2_lote_nomes_idosos_masculino = open('oxford_dose2_lote_nomes_idosos_masculino.txt', 'a')
                                    oxford_dose2_lote_nomes_idosos_masculino.write(input() + '\n')
                                    oxford_dose2_lote_nomes_idosos_masculino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã idosa do sexo feminino que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose2_lote_nomes_idosas_feminino = open('oxford_dose2_lote_nomes_idosas_feminino.txt', 'a')
                                    oxford_dose2_lote_nomes_idosas_feminino.write(input() + '\n')
                                    oxford_dose2_lote_nomes_idosas_feminino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')


                            #vai adicionar dados de vacinação de uma pessoa de qualquer outro grupo prioritário
                            else:
                                print('\nQual o sexo da pessoa?')
                                sexo = str(input())
                                #adicionar cidadão do sexo masculino, com prioridade, que foi vacinado.
                                if sexo == 'Masculino' or sexo == 'masculino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose2_lote_nomes_prioridade_masculino = open('oxford_dose2_lote_nomes_prioridade_masculino.txt', 'a')
                                    oxford_dose2_lote_nomes_prioridade_masculino.write(input() + '\n')
                                    oxford_dose2_lote_nomes_prioridade_masculino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                
                                #adicionar cidadã do sexo feminino, com prioridade, que foi vacinada.
                                elif sexo == 'Feminino' or  sexo == 'feminino':
                                    print('\nDigite o nome completo e o CPF (nome, cpf):')
                                    oxford_dose2_lote_nomes_prioridade_feminino = open('oxford_dose2_lote_nomes_prioridade_feminino.txt', 'a')
                                    oxford_dose2_lote_nomes_prioridade_feminino.write(input() + '\n')
                                    oxford_dose2_lote_nomes_prioridade_feminino.close()
                                    doses += 1
                                    dose_2 += 1

                                    #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                    print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                    dia = str(input())
                                    print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                    horario = float(input())
                                    if horario > 7 and horario < 12:
                                        manha += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')
                                    elif horario > 11 and horario < 19:
                                        tarde += 1
                                        print('\nVacinação registrada com sucesso!\n')
                                        print('Voltando para o menu principal...\n')

                        #vai adicionar dados de vacinação de uma pessoa que NÃO pertence a nenhum grupo prioritário.
                        elif prioritario == 'Não' or prioritario == 'não' or prioritario == 'Nao' or prioritario == 'nao' or prioritario == 'n':
                            print('\nQual o sexo da pessoa?')
                            sexo = str(input())

                            #adicionar cidadão do sexo masculino, sem prioridade, que foi vacinado.
                            if sexo == 'Masculino' or sexo == 'masculino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                oxford_dose2_lote_nomes_np_masculino = open('oxford_dose2_lote_nomes_np_masculino.txt', 'a')
                                oxford_dose2_lote_nomes_np_masculino.write(input() + '\n')
                                oxford_dose2_lote_nomes_np_masculino.close()
                                doses += 1
                                dose_2 += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (dd.mm.aaaa) em que o cidadão foi vacinado?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que o paciente foi vacinado?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                
                            #adicionar cidadã do sexo feminino, sem prioridade, que foi vacinada.
                            elif sexo == 'Feminino' or  sexo == 'feminino':
                                print('\nDigite o nome completo e o CPF (nome, cpf):')
                                oxford_dose2_lote_nomes_np_feminino = open('oxford_dose2_lote_nomes_np_feminino.txt', 'a')
                                oxford_dose2_lote_nomes_np_feminino.write(input() + '\n')
                                oxford_dose2_lote_nomes_np_feminino.close()
                                doses += 1
                                dose_2 += 1

                                #vai perguntar qual o dia e horário em que o cidadão foi vacinado.
                                print('\nQual o dia (DD MM AAAA) em que a cidadã foi vacinada?')
                                dia = str(input())
                                print('\nQual o horário (apenas as horas, ex: 15) em que a paciente foi vacinada?')
                                horario = float(input())
                                if horario > 7 and horario < 12:
                                    manha += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')
                                elif horario > 11 and horario < 19:
                                    tarde += 1
                                    print('\nVacinação registrada com sucesso!\n')
                                    print('Voltando para o menu principal...\n')

    #Essa parte vai mostrar os dados de todas as vacinações que foram registradas no sistema
    #1 – Quantas pessoas foram vacinadas e quantas doses foram aplicadas;
    #2 – Quantas pessoas receberam a 1ª dose e quantas a 2ª dose;
    #3 – O percentual de pessoas que recebeu cada tipo vacina (segundo o fabricante da vacina);
    #4 – O percentual de idosos vacinados em relação ao total de vacinados;
    #5 – O percentual de vacinas aplicada pela manhã e pela tarde;
    #6 – O percentual de vacinados do sexo masculino e do sexo feminino.
    elif opcao_entrada == 2:
        if doses != 0 and masculino > 0 and feminino > 0: #Para entrar aqui, deve ter sido vacinado(a) ao menos uma pessoa.
            #Serão calculados o percentuais das estatísticas 3, 4, 5 e 6.
            total_pessoas = masculino + feminino
            porcentagem_idosos = int(idosos_vacinados*100/total_pessoas)
            porcentagem_masculinos = int(masculino*100/total_pessoas)
            porcentagem_femininos = int(feminino*100/total_pessoas)
            porcentagem_manha = int(manha*100/doses)
            porcentagem_tarde = int(tarde*100/doses)
            porcentagem_coronavac = int(vacinados_coronavac*100/total_pessoas)
            porcentagem_oxford = int(vacinados_oxford*100/total_pessoas)

            #Vai imprimir as estatísticas na tela.
            print('\nEssas são as estatísticas de vacinação contra a COVID-19 em Feira de Santana:\n')
            print('%d pessoas já foram vacinadas e %d doses foram aplicadas.' % (total_pessoas, doses))
            print('%d pessoas receberam a 1ª dose e %d reberam a 2ª dose da vacina.' % (dose_1, dose_2))
            print(porcentagem_coronavac, '% das pessoas receberam a Coronavac e', porcentagem_oxford, '% reberam a Astrazeneca.')
            print(porcentagem_idosos, '% dos que foram vacinados eram idosos.')
            print(porcentagem_manha, '% de vacinas foram aplicadas pela manhã e', porcentagem_tarde, '% foram aplicadas no período da tarde.')
            print(porcentagem_masculinos, '% dos que foram vacinados eram do sexo masculino e', porcentagem_femininos, '% eram do feminino.')
            print('\nVoltando para o menu principal...\n')
        else: #Caso nenhuma vacinação tenha sido registrada.
            print('\nAinda não há dados de pessoas vacinadas!')   
            print('\nVoltando para o menu principal...\n')
    
    #Logo após cadastrar uma pessoa, o algoritmo vai voltar ao menu principal.
    print('Bem-vindo ao Sistema de Controle das Aplicações de Vacinas\ncontra a COVID-19 em Feira de Santana - BA')
    print('\nEntre as opções abaixo, escolha a que corresponde ao você deseja fazer no sistema:')
    print('1. Registrar vacinação de um nova pessoa ao sistema\n2. Ver estatísticas de vacinação em Feira de Santana')
    opcao_entrada = int(input('\nDigite o número da opção desejada:\n'))

    #Loop caso a pessoa digite uma opção errada na volta ao menu principal.
    while opcao_entrada == 0 or opcao_entrada > 3:
        print('\nDigite um número válido!\n')
        print('Entre as opções abaixo, escolha a que corresponde ao você deseja fazer no sistema:')
        print('1. Registrar vacinação de um nova pessoa ao sistema\n2. Ver estatísticas de vacinação em Feira de Santana')
        opcao_entrada = int(input('\nDigite o número da opção desejada:\n'))