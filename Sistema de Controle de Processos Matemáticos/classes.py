
import os

class Processo:
    def __init__(self, pid = None, tipo = None):
        self.__pid = int(pid)
        self.__tipo = tipo


    def get_pid(self):
        return self.__pid
    
    def get_tipo(self):
        return self.__tipo

    def set_pid(self, pid):
        self.__pid = pid

    def set_tipo(self, tipo):
        self.__tipo = tipo


    def execute():
        return


class Calculo(Processo):
    def __init__(self, pid = None, tipo = None, operandos = None, operador = None):
        super().__init__(pid, tipo)
        self.__operando_1 = float(operandos[0])
        self.__operando_2 = float(operandos[1])
        self.__operador = operador
        

    def get_operando_1(self):
        return self.__operando_1
    
    def get_operando_2(self):
        return self.__operando_2
    
    def get_operador(self):
        return self.__operador

    def set_operando_1(self, operando_1):
        self.__operando_1 = operando_1

    def set_operando_2(self, operando_2):
        self.__operando_2 = operando_2

    def set_operador(self, operador):
        self.__operador = operador


    def execute(self):
        match self.__operador:
            case '+':
                return self.__operando_1 + self.__operando_2, 0
            case '-':
                return self.__operando_1 - self.__operando_2, 0
            case '*':
                return self.__operando_1 * self.__operando_2, 0
            case '/':
                if self.__operando_2 == 0.0:
                    return '', 0
                else:
                    return self.__operando_1 / self.__operando_2, 0
        


class Gravacao(Processo):
    def __init__(self, pid = None, tipo = None, operandos = None, operador = None):
        super().__init__(pid, tipo)
        self.__operando_1 = float(operandos[0])
        self.__operando_2 = float(operandos[1])
        self.__operador = operador


    def get_operando_1(self):
        return self.__operando_1
    
    def get_operando_2(self):
        return self.__operando_2
    
    def get_operador(self):
        return self.__operador

    def set_operando_1(self, operando_1):
        self.__operando_1 = operando_1

    def set_operando_2(self, operando_2):
        self.__operando_2 = operando_2

    def set_operador(self, operador):
        self.__operador = operador


    def execute(self):
        arquivo_computation = open('computation.txt', 'a')
        arquivo_computation.write(f'{self.__operando_1};{self.__operador};{self.__operando_2}\n')
        arquivo_computation.close()
        return '', 1

    
class Leitura(Processo):
    def __init__(self, pid = None, tipo = None, ):
        super().__init__(pid, tipo)


    def execute(self):
        arquivo_computation = open('computation.txt', 'r')
        dados_computation = arquivo_computation.read().strip().split('\n')
        arquivo_computation.close()
        arquivo_computation = open('computation.txt', 'a')
        arquivo_computation.truncate(0)
        arquivo_computation.close()
        contador = 0
        for calculo in dados_computation:
            dados_computation[contador] = calculo.split(';')
            contador += 1
        return dados_computation, 2


class Impressao(Processo):
    def __init__(self, pid = None, tipo = None, lista = None):
        super().__init__(pid, tipo)
        if lista == None:
            self.__lista = []
        else:
            self.__lista = lista
        
    def get_lista(self):
        return self.__lista

    def set_lista(self, lista):
        self.__lista = lista

    
    def execute(self):
        os.system('cls') or None
        print('\n..:: Executar Próximo ::..\n')
        print('Lista de Processos:\n')
        for processo in self.__lista:
            print(f'Pid do processo: {processo.get_pid()}')
            print(f'Tipo de processo: {processo.get_tipo()}')
            match processo.get_tipo():
                case 'Calculo':
                    print(f'Operando 1: {processo.get_operando_1()}')
                    print(f'Operador: {processo.get_operador()}')
                    print(f'Operando 2: {processo.get_operando_2()}\n')
                case 'Gravacao':
                    print(f'Operando 1: {processo.get_operando_1()}')
                    print(f'Operador: {processo.get_operador()}')
                    print(f'Operando 2: {processo.get_operando_2()}\n')
                case _:
                    print('')
        return '', 3

