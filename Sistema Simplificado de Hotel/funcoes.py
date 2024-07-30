import os


def menu():
    opcao_invalida = False
    while True:
        os.system('cls') or None
        print('\n..:: Menu ::..\n')
        print('1 - Consultar disponibilidade')
        print('2 - Consultar reserva')
        print('3 - Realizar reserva')
        print('4 - Cancelar reserva')
        print('5 - Realizar check-in')
        print('6 - Realizar check-out')
        print('7 - Registrar consumo')
        print('8 - Salvar')
        print('0 - Sair\n')
        if opcao_invalida == True:
            print('Digite uma opção válida!')
        opcao = input('Digite a opção desejada: ').strip()
        if opcao in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return opcao
        else:
            opcao_invalida = True


def realizar_reserva(pousada):
    os.system('cls') or None
    print('\n..:: Realizar Reserva ::..\n')
    print('Digite os dados da reserva:')
    dia_inicial = input('Digite o dia inicial: ').strip()
    dia_final = input('Digite o dia final: ').strip()
    nome_cliente = input('Digite o nome do cliente: ').strip()
    numero_quarto = input('Digite o número do quarto: ').strip()
    pousada.realizar_reserva(dia_inicial, dia_final, nome_cliente, numero_quarto)
    return pousada 

def realizar_check_in(pousada):
    os.system('cls') or None
    print('\n..:: Realizar Check-in ::..\n')
    nome_cliente = input('Digite o nome do cliente para procurar por reservas: ').strip()
    pousada.realizar_check_in(nome_cliente)
    return pousada  


def realizar_check_out(pousada):
    os.system('cls') or None
    print('\n..:: Realizar Check-out ::..\n')
    nome_cliente = input('Digite o nome do cliente para procurar por check-in: ').strip()
    pousada.realizar_check_out(nome_cliente)
    return pousada  


def registrar_consumo(pousada):
    os.system('cls') or None
    print('\n..:: Registrar Consumo ::..\n')
    nome_cliente = input('Digite o nome do cliente para procurar por check-in: ').strip()
    pousada.registrar_consumo(nome_cliente)
    return pousada  


def salvar(pousada):
    pousada.salvar_dados()
    os.system('cls') or None
    print('\n..:: Salvar ::..\n')
    print('Dados salvos com sucesso!')
    input('\nPressione Enter para voltar ao menu: ')


def sair():
    return
