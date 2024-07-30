
import os
import classes

class Sistema:
    def __init__(self, lista = None, proximo_pid = 0, opcao = 0):
        self.__opcao = opcao
        if lista == None:
            self.__lista = []
        else:
            self.__lista = lista
        self.__proximo_pid = int(proximo_pid)

    def get_opcao(self):
         return self.__opcao
    
    def get_lista(self):
         return self.__lista
    
    def get_proximo_pid(self):
         return self.__proximo_pid

    def set_opcao(self, opcao):
            self.__opcao = opcao

    def set_lista(self, lista):
            self.__lista = lista

    def set_proximo_pid(self, proximo_pid):
            self.__proximo_pid = proximo_pid

    
    def menu(self):
        opcao_invalida = False
        while True:
            os.system('cls') or None
            print('\n..:: Menu ::..\n')
            print('1 - Criar Processo')
            print('2 - Executar Próximo')
            print('3 - Executar Processo Específico')
            print('4 - Salvar a Fila de Processos')
            print('5 - Carregar do Arquivo a Fila de Processos')
            print('0 - Sair\n')
            if opcao_invalida == True:
                print('Digite uma opção válida!')
            self.__opcao = input('Digite a opção desejada: ').strip()
            if self.__opcao in ['0', '1', '2', '3', '4', '5']:
                return self.__opcao
            else:
                opcao_invalida = True

    
    def criar_processo(self):
        opcao_invalida = False
        while True:
            os.system('cls') or None
            print('\n..:: Criar Processo ::..\n')
            print('1 - Processo de Cálculo')
            print('2 - Processo de Gravação')
            print('3 - Processo de Leitura')
            print('4 - Processo de Impressão')
            print('0 - Voltar ao Menu')
            if opcao_invalida == True:
                print('Digite uma opção válida!')
            self.__opcao = input('\nDigite o processo desejado: ').strip()
            if self.__opcao in ['0', '1', '2', '3', '4']:    
                match self.__opcao:
                    case '0':
                        return
                    
                    case '1':
                        tem_operador = False
                        operacao_invalida = False
                        while True:
                            os.system('cls') or None
                            print('\n..:: Criar Processo ::..\n')
                            if operacao_invalida == True:
                                print('Digite uma operação válida!')
                            operacao = input('Digite uma expressão de dois números e um operador no meio: ')
                            operacao = operacao.replace(' ', '')
                            for x in operacao:
                                if x in ['+', '-', '*', '/']:
                                    operador = x
                                    tem_operador = True
                            if tem_operador == True:
                                operandos = operacao.split(operador)
                                try:
                                    operandos[0] = float(operandos[0])
                                    operandos[1] = float(operandos[1])
                                    self.__lista.append(classes.Calculo(self.__proximo_pid, 'Calculo', operandos, operador))
                                    os.system('cls') or None
                                    print('\n..:: Criar Processo ::..\n')
                                    print(f'Processo de cálculo com pid {self.__proximo_pid} criado com sucesso!')
                                    input('Pressione Enter para voltar ao Menu:')
                                    self.__proximo_pid += 1
                                    return
                                except:
                                    operacao_invalida = True
                                    continue
                            else:
                                operacao_invalida = True
                                continue

                    case '2':
                        tem_operador = False
                        operacao_invalida = False
                        while True:
                            os.system('cls') or None
                            print('\n..:: Criar Processo ::..\n')
                            if operacao_invalida == True:
                                print('Digite uma operação válida!')
                            operacao = input('Digite uma expressão de dois números e um operador no meio: ')
                            operacao = operacao.replace(' ', '')
                            for x in operacao:
                                if x in ['+', '-', '*', '/']:
                                    operador = x
                                    tem_operador = True
                            if tem_operador == True:
                                operandos = operacao.split(operador)
                                try:
                                    operandos[0] = float(operandos[0])
                                    operandos[1] = float(operandos[1])
                                    self.__lista.append(classes.Gravacao(self.__proximo_pid, 'Gravacao', operandos, operador))
                                    os.system('cls') or None
                                    print('\n..:: Criar Processo ::..\n')
                                    print(f'Processo de gravação com pid {self.__proximo_pid} criado com sucesso!')
                                    input('Pressione Enter para voltar ao Menu:')
                                    self.__proximo_pid += 1
                                    return
                                except:
                                    operacao_invalida = True
                                    continue
                            else:
                                operacao_invalida = True
                                continue
                        
                    case '3':
                        self.__lista.append(classes.Leitura(self.__proximo_pid, 'Leitura'))
                        os.system('cls') or None
                        print('\n..:: Criar Processo ::..\n')
                        print(f'Processo de leitura com pid {self.__proximo_pid} criado com sucesso!')
                        input('Pressione Enter para voltar ao Menu:')
                        self.__proximo_pid += 1
                        return

                    case '4':
                        self.__lista.append(classes.Impressao(self.__proximo_pid, 'Impressao', self.__lista))
                        os.system('cls') or None
                        print('\n..:: Criar Processo ::..\n')
                        print(f'Processo de impressão com pid {self.__proximo_pid} criado com sucesso!')
                        input('Pressione Enter para voltar ao Menu:')
                        self.__proximo_pid += 1
                        return
            else:
                opcao_invalida = True

    
    def executar_proximo(self):
        if self.__lista == []:
            os.system('cls') or None
            print('\n..:: Executar Próximo ::..\n')
            print('Não foi encontrado nenhum processo na lista! ')
            input('\nPressione Enter para voltar ao Menu:')
        else:
            execucao = self.__lista[0].execute()
            match execucao[1]:
                case 0:
                    if execucao[0] == '':
                        os.system('cls') or None
                        print('\n..:: Executar Próximo ::..\n')
                        print('Processo executado: Cálculo')
                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                        print(f'Resultado da operação: Divisão impossível\n')
                        input('Pressione Enter para voltar ao Menu:')
                    else:
                        os.system('cls') or None
                        print('\n..:: Executar Próximo ::..\n')
                        print('Processo executado: Cálculo')
                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                        print(f'Resultado da operação: {execucao[0]}\n')
                        input('Pressione Enter para voltar ao Menu:')
                case 1:
                    os.system('cls') or None
                    print('\n..:: Executar Próximo ::..\n')
                    print('Processo executado: Gravação')
                    print(f'Pid do processo: {self.__lista[0].get_pid()}')
                    print('Processo executado com sucesso!\n')
                    input('Pressione Enter para voltar ao Menu:')
                case 2:
                    if execucao[0] == [['']]:
                        os.system('cls') or None
                        print('\n..:: Executar Próximo ::..\n')
                        print('Processo executado: Leitura')
                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                        print('Nenhum processo foi encontrado!\n')
                        input('Pressione Enter para voltar ao Menu:')
                    else:
                        for calculo in execucao[0]:
                            self.__lista.append(classes.Calculo(self.__proximo_pid, 'Calculo', [calculo[0], calculo[2]], calculo[1]))
                            self.__proximo_pid += 1
                        os.system('cls') or None
                        print('\n..:: Executar Próximo ::..\n')
                        print('Processo executado: Leitura')
                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                        print('Processo executado com sucesso!\n')
                        input('Pressione Enter para voltar ao Menu:')
                case 3:
                    input('Pressione Enter para voltar ao Menu:')
            self.__lista.pop(0)
        return
    

    def executar_processo_especifico(self):
        if self.__lista == []:
            os.system('cls') or None
            print('\n..:: Executar Processo Específico ::..\n')
            print('Não foi encontrado nenhum processo na lista! ')
            input('\nPressione Enter para voltar ao Menu:')
        else:
            opcao_invalida = False
            while True:
                os.system('cls') or None
                print('\n..:: Executar Processo Específico ::..\n')
                if opcao_invalida == True:
                    print('Digite uma opção válida!')
                pid = input('Digite o número do pid do processo a ser executado: ').strip()
                try:
                    pid = int(pid)
                    localizacao_do_processo = 0
                    for processo in self.__lista:
                        if processo.get_pid() == pid:
                            execucao = processo.execute()
                            match execucao[1]:
                                case 0:
                                    if execucao[0] == '':
                                        os.system('cls') or None
                                        print('\n..:: Executar Processo Específico ::..\n')
                                        print('Processo executado: Cálculo')
                                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                                        print(f'Resultado da operação: Divisão impossível\n')
                                        input('Pressione Enter para voltar ao Menu:')
                                    else:
                                        os.system('cls') or None
                                        print('\n..:: Executar Processo Específico ::..\n')
                                        print('Processo executado: Cálculo')
                                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                                        print(f'Resultado da operação: {execucao[0]}\n')
                                        input('Pressione Enter para voltar ao Menu:')
                                case 1:
                                    os.system('cls') or None
                                    print('\n..:: Executar Processo Específico ::..\n')
                                    print('Processo executado: Gravação')
                                    print(f'Pid do processo: {self.__lista[0].get_pid()}')
                                    print('Processo executado com sucesso!\n')
                                    input('Pressione Enter para voltar ao Menu:')
                                case 2:
                                    if execucao[0] == [['']]:
                                        os.system('cls') or None
                                        print('\n..:: Executar Processo Específico ::..\n')
                                        print('Processo executado: Leitura')
                                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                                        print('Nenhum processo foi encontrado!\n')
                                        input('Pressione Enter para voltar ao Menu:')
                                    else:
                                        for calculo in execucao[0]:
                                            self.__lista.append(classes.Calculo(self.__proximo_pid, 'Calculo', [calculo[0], calculo[2]], calculo[1]))
                                            self.__proximo_pid += 1
                                        os.system('cls') or None
                                        print('\n..:: Executar Processo Específico ::..\n')
                                        print('Processo executado: Leitura')
                                        print(f'Pid do processo: {self.__lista[0].get_pid()}')
                                        print('Processo executado com sucesso!\n')
                                        input('Pressione Enter para voltar ao Menu:')
                                case 3:
                                    input('Pressione Enter para voltar ao Menu:')
                            self.__lista.pop(localizacao_do_processo)
                            return
                        localizacao_do_processo += 1
                    os.system('cls') or None
                    print('\n..:: Executar Processo Específico ::..\n')
                    print('Não foi encontrado nenhum processo com o pid informado! ')
                    input('\nPressione Enter para voltar ao Menu:')
                    return
                except:
                    opcao_invalida = False


    def salvar_a_fila_de_processos(self):
        arquivos_dados = open('dados.txt', 'a')
        arquivos_dados.truncate(0)
        arquivos_dados.write(f'{self.__proximo_pid}\n')
        for processo in self.__lista:
            match processo.get_tipo():
                case 'Calculo':
                    arquivos_dados.write(f'{processo.get_pid()};{processo.get_tipo()};{processo.get_operando_1()};{processo.get_operando_2()};{processo.get_operador()}\n')
                case 'Gravacao':
                    arquivos_dados.write(f'{processo.get_pid()};{processo.get_tipo()};{processo.get_operando_1()};{processo.get_operando_2()};{processo.get_operador()}\n')
                case 'Leitura':
                    arquivos_dados.write(f'{processo.get_pid()};{processo.get_tipo()}\n')
                case 'Impressao':
                    arquivos_dados.write(f'{processo.get_pid()};{processo.get_tipo()}\n')
        arquivos_dados.close
        os.system('cls') or None
        print('\n..:: Salvar a Fila de Processos ::..\n')
        print('Fila de processos salva com sucesso!\n')
        input('Pressione Enter para voltar ao Menu:')


    def carregar_do_arquivo_a_fila_de_processos(self):
        arquivo_dados = open('dados.txt', 'r')
        processos_dados = arquivo_dados.read().strip().split('\n')
        arquivo_dados.close()
        self.__proximo_pid = int(processos_dados.pop(0))
        posicao = 0
        for processo in processos_dados:
            processos_dados[posicao] = processo.split(';')
            posicao += 1
        self.__lista = []
        for processo in processos_dados:
            match processo[1]:
                case 'Calculo':
                    self.__lista.append(classes.Calculo(processo[0], processo[1], [processo[2], processo[3]], processo[4]))
                case 'Gravacao':
                    self.__lista.append(classes.Gravacao(processo[0], processo[1], [processo[2], processo[3]], processo[4]))
                case 'Leitura':
                    self.__lista.append(classes.Leitura(processo[0], processo[1]))
                case 'Impressao':
                    self.__lista.append(classes.Impressao(processo[0], processo[1], self.__lista))
        os.system('cls') or None
        print('\n..:: Carregar do Arquivo a Fila de Processos ::..\n')
        print('Fila de processos carregada com sucesso!\n')
        input('Pressione Enter para voltar ao Menu:')
        

