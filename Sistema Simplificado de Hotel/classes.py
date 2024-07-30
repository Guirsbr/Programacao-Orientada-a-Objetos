import os

class Pousada:
    def __init__(self, nome = None, contato = None, quarto = None, reserva = None, produto = None):
        self.__nome = nome
        self.__contato = contato
        if quarto == None:
            self.__quarto = []
        else:
            self.__quarto = quarto
        if reserva == None:
            self.__reserva = []
        else:
            self.__reserva = reserva
        if produto == None:
            self.__produto = []
        else:
            self.__produto = produto

    # GETTERS E SETTERS:
    
    def get_nome(self):
        return self.__nome
    
    def get_contato(self):
        return self.__contato
    
    def get_quarto(self):
        return self.__quarto
    
    def get_reserva(self):
        return self.__reserva
    
    def get_produto(self):
        return self.__produto

    def set_nome(self, nome):
        self.__nome = nome

    def set_contato(self, contato):
        self.__contato = contato

    def set_quarto(self, quarto):
        self.__quarto = quarto

    def set_reserva(self, reserva):
        self.__reserva = reserva

    def set_produto(self, produto):
        self.__produto = produto

    # ADDS E REMOVES:
    
    def add_quarto(self, quarto):
        self.__quarto.append(quarto)

    def add_reserva(self, reserva):
        self.__reserva.append(reserva)

    def add_produto(self, produto):
        self.__produto.append(produto)

    def remove_quarto(self, quarto):
        if quarto in self.__quarto:
            self.__quarto.remove()

    def remove_reserva(self, reserva):
        if reserva in self.__reserva:
            self.__reserva.remove()

    def remove_produto(self, produto):
        if produto in self.__produto:
            self.__produto.remove()

    # OUTROS:

    def carregar_dados(self):
        arquivo_pousada = open('pousada.txt', 'r')
        dados_pousada = arquivo_pousada.read().strip()
        dados_pousada = dados_pousada.split(';')
        self.__nome = dados_pousada[0]
        self.__contato = int(dados_pousada[1])
        arquivo_pousada.close()

        arquivo_produto = open('produto.txt', 'r')
        dados_produto = arquivo_produto.read().strip().split('\n')
        posicao = 0
        for produto in dados_produto:
            dados_produto[posicao] = produto.split(';')
            posicao += 1
        for produto in dados_produto:
            self.add_produto(Produto(produto[0], produto[1], produto[2]))
        arquivo_produto.close()

        arquivo_quarto = open('quarto.txt', 'r')
        dados_quarto = arquivo_quarto.read().strip().split('\n')
        posicao = 0
        for quarto in dados_quarto:
            dados_quarto[posicao] = quarto.split(';')
            posicao += 1
        for quarto in dados_quarto:
            self.add_quarto(Quarto(quarto[0], quarto[1], quarto[2]))
        arquivo_quarto.close()
        
        arquivo_reserva = open('reserva.txt', 'r')
        dados_reserva = arquivo_reserva.read().strip().split('\n')
        posicao = 0
        for reserva in dados_reserva:
            dados_reserva[posicao] = reserva.split(';')
            posicao += 1
        objetos_quarto = self.get_quarto()
        for reserva in dados_reserva:
            numero_quarto_reserva = int(reserva[3])
            for quarto in objetos_quarto:
                if numero_quarto_reserva == quarto.get_numero():
                    reserva[3] = quarto
        for reserva in dados_reserva:
            if len(reserva) == 5:
                self.add_reserva(Reserva(reserva[0], reserva[1], reserva[2], reserva[3], reserva[4]))
            else:
                reserva[5] = reserva[5].split(':')
                reserva[3].set_consumo(reserva[5])
                self.add_reserva(Reserva(reserva[0], reserva[1], reserva[2], reserva[3], reserva[4]))
        arquivo_reserva.close()

        return self
        

    def salvar_dados(self):
        arquivo_pousada = open('pousada.txt', 'a')
        arquivo_pousada.truncate(0)
        arquivo_pousada.write(f'{self.__nome};{self.__contato}')
        arquivo_pousada.close()

        arquivo_produto = open('produto.txt', 'a')
        arquivo_produto.truncate(0)
        for produto in self.get_produto():
            arquivo_produto.write(produto.serializar())
        arquivo_produto.close()

        arquivo_quarto = open('quarto.txt', 'a')
        arquivo_quarto.truncate(0)
        for quarto in self.get_quarto():
            arquivo_quarto.write(quarto.serializar())
        arquivo_quarto.close()

        arquivo_reserva = open('reserva.txt', 'a')
        arquivo_reserva.truncate(0)
        for reserva in self.get_reserva():
            quarto_reserva = reserva.get_quarto()
            if quarto_reserva.get_consumo() == []:
                arquivo_reserva.write(f'{reserva.serializar()}\n')
            else:
                arquivo_reserva.write(f'{reserva.serializar()};')
                primeira_vez = True
                for consumo in quarto_reserva.get_consumo():
                    if primeira_vez == False:
                        arquivo_reserva.write(':')
                    arquivo_reserva.write(f'{consumo}')
                    primeira_vez = False
                arquivo_reserva.write('\n')
        arquivo_reserva.close()


    def realizar_reserva(self, dia_inicial_selecionado, dia_final_selecionado, nome_cliente, numero_quarto_selecionado):
        quarto_disponivel = True
        try:
            dia_inicial_selecionado = int(dia_inicial_selecionado)
            dia_final_selecionado = int(dia_final_selecionado)
            numero_quarto_selecionado = int(numero_quarto_selecionado) 
            quarto_selecionado = None
            for quarto in self.__quarto:
                if quarto.get_numero() == numero_quarto_selecionado:
                    quarto_selecionado = quarto
            if quarto_selecionado == None or dia_inicial_selecionado < 0 or dia_final_selecionado > 31:
                raise Exception()
            for reserva in self.__reserva:
                dia_inicial_reserva = reserva.get_dia_inicio()
                dia_final_reserva = reserva.get_dia_fim()
                if numero_quarto_selecionado == reserva.get_quarto().get_numero() and not ((dia_inicial_selecionado < dia_inicial_reserva and dia_final_selecionado <= dia_inicial_reserva) or (dia_inicial_selecionado >= dia_final_reserva and dia_final_selecionado > dia_final_reserva)):
                    quarto_disponivel = False
            if quarto_disponivel == True:
                self.add_reserva(Reserva(dia_inicial_selecionado, dia_final_selecionado, nome_cliente, quarto_selecionado, 'A'))
                os.system('cls') or None
                print('\n..:: Realizar Reserva ::..\n')
                print(f'Reserva feita com sucesso no quarto {numero_quarto_selecionado}.')
                print(f'Hospedagem inicia dia {dia_inicial_selecionado} e termina dia {dia_final_selecionado}.')
                input('\nPressione Enter para voltar ao menu: ')
                return self
            else:
                os.system('cls') or None
                print('\n..:: Realizar Reserva ::..\n')
                print('Quarto não está disponível no período selecionado.')
                input('\nPressione Enter para voltar ao menu: ')
                return self  
        except:
            os.system('cls') or None
            print('\n..:: Realizar Reserva ::..\n')
            print('Dados digitados não correspondem ao que foi pedido.')
            input('\nPressione Enter para voltar ao menu: ')
            return self
        

    def realizar_check_in(self, nome_cliente):
        reservas_do_cliente = []
        cliente_possui_reserva = False
        for reserva in self.__reserva:
            if reserva.get_cliente() == nome_cliente and reserva.get_status() == 'A':
                reservas_do_cliente.append(reserva)
                cliente_possui_reserva = True
        if cliente_possui_reserva == True:
            opcao_invalida = False
            while True:
                os.system('cls') or None
                print('\n..:: Realizar Check-in ::..\n')
                print('Foram encontradas as seguintes reservas no nome do cliente:\n')
                contador = 1
                for reserva in reservas_do_cliente:
                    total_de_dias_reservados = reserva.get_dia_fim() - reserva.get_dia_inicio()
                    print(f'Reserva nº{contador}:')
                    print(f'Reserva começa dia {reserva.get_dia_inicio()} e termina dia {reserva.get_dia_fim()}.')
                    print(f'O valor total da reserva é de: R$ {total_de_dias_reservados * reserva.get_quarto().get_diaria():.2f}')
                    print(f'Reserva no quarto nº {reserva.get_quarto().get_numero()}.')
                    print(f'O quarto está na categoria {reserva.get_quarto().get_categoria()}.\n')
                    contador += 1
                if opcao_invalida == True:
                    print('Digite uma opção válida!')
                try:
                    numero_reserva_selecionada = int(input('Digite o nº da reserva a ser feita o check-in: ').strip())
                    if numero_reserva_selecionada >= 1 and numero_reserva_selecionada <= contador:
                        numero_reserva_selecionada -= 1
                        reserva_selecionada = reservas_do_cliente[numero_reserva_selecionada]
                        reserva_selecionada.set_status('I')
                        total_de_dias_reservados = reserva_selecionada.get_dia_fim() - reserva_selecionada.get_dia_inicio()
                        os.system('cls') or None
                        print('\n..:: Realizar Check-in ::..\n')
                        print(f'Check-in feito com sucesso.\n')
                        print(f'A hospedagem começa dia {reserva_selecionada.get_dia_inicio()} e termina dia {reserva_selecionada.get_dia_fim()}.')
                        print(f'A hospedagem durará no total {total_de_dias_reservados} dias.')
                        print(f'O valor total das diárias é de: R$ {total_de_dias_reservados * reserva_selecionada.get_quarto().get_diaria():.2f}')
                        print(f'A hospedagem é no quarto nº {reserva_selecionada.get_quarto().get_numero()}.')
                        print(f'O quarto está na categoria {reserva_selecionada.get_quarto().get_categoria()}.')
                        input('\nPressione Enter para voltar ao menu: ')
                        return self
                    else:
                        opcao_invalida = True
                except:
                    opcao_invalida = True
        else:
            os.system('cls') or None
            print('\n..:: Realizar Check-in ::..\n')
            print('Cliente digitado não possui nenhuma reserva no sistema.')
            input('\nPressione Enter para voltar ao menu: ')
            return self

    
    def realizar_check_out(self, nome_cliente):
        lista_de_check_in_do_cliente = []
        cliente_possui_check_in = False
        for reserva in self.__reserva:
            if reserva.get_cliente() == nome_cliente and reserva.get_status() == 'I':
                lista_de_check_in_do_cliente.append(reserva)
                cliente_possui_check_in = True
        if cliente_possui_check_in == True:
            opcao_invalida = False
            while True:
                os.system('cls') or None
                print('\n..:: Realizar Check-out ::..\n')
                print('Foram encontradas os seguintes check-in no nome do cliente:\n')
                contador = 1
                for check_in in lista_de_check_in_do_cliente:
                    total_de_dias_reservados = check_in.get_dia_fim() - check_in.get_dia_inicio()
                    valor_total_das_diarias = total_de_dias_reservados * check_in.get_quarto().get_diaria()
                    print(f'Check-in nº{contador}:')
                    print(f'Check-in começou dia {check_in.get_dia_inicio()} e termina dia {check_in.get_dia_fim()}.')
                    print(f'O check-in durará no total {total_de_dias_reservados} dias.')
                    print(f'O valor total das diárias é de: R$ {valor_total_das_diarias:.2f}')
                    print('Lista de consumos da copa:')
                    for consumo in check_in.get_quarto().lista_consumo(self):
                        print(f'1 {consumo.get_nome()} de R$ {consumo.get_preco():.2f}')
                    valor_total_consumo = check_in.get_quarto().valor_total_consumo(self)
                    print(f'O valor total dos consumo é de: R$ {valor_total_consumo:.2f}')
                    print(f'O valor total a ser pago é de: R$ {valor_total_consumo + valor_total_das_diarias:.2f}\n')
                    contador += 1
                if opcao_invalida == True:
                    print('Digite uma opção válida!')
                try:
                    numero_check_in_selecionado = int(input('Digite o nº do check-in a ser feita o check-out: ').strip())
                    if numero_check_in_selecionado >= 1 and numero_check_in_selecionado <= contador:
                        numero_check_in_selecionado -= 1
                        check_in_selecionado = lista_de_check_in_do_cliente[numero_check_in_selecionado]
                        check_in_selecionado.set_status('O')
                        check_in_selecionado.get_quarto().limpa_consumo()
                        os.system('cls') or None
                        print('\n..:: Realizar Check-out ::..\n')
                        print('Check-out feito com sucesso!')
                        input('\nPressione Enter para voltar ao menu: ')
                        return self
                    else:
                        opcao_invalida = True
                except:
                    opcao_invalida = True
        else:
            os.system('cls') or None
            print('\n..:: Realizar Check-out ::..\n')
            print('Cliente digitado não possui nenhum check-in no sistema.')
            input('\nPressione Enter para voltar ao menu: ')
            return self
        

    def registrar_consumo(self, nome_cliente):
        lista_de_check_in_do_cliente = []
        cliente_possui_check_in = False
        for reserva in self.__reserva:
            if reserva.get_cliente() == nome_cliente and reserva.get_status() == 'I':
                lista_de_check_in_do_cliente.append(reserva)
                cliente_possui_check_in = True
        if cliente_possui_check_in == True:
            opcao_invalida = False
            while True:
                os.system('cls') or None
                print('\n..:: Registrar Consumo ::..\n')
                print('Foram encontradas os seguintes check-in no nome do cliente:\n')
                contador = 1
                for check_in in lista_de_check_in_do_cliente:
                    print(f'Check_in nº{contador}:')
                    print(f'Check_in começou dia {check_in.get_dia_inicio()} e termina dia {check_in.get_dia_fim()}.')
                    print(f'Check_in no quarto nº {check_in.get_quarto().get_numero()}.')
                    print(f'O quarto está na categoria {check_in.get_quarto().get_categoria()}.\n')
                    contador += 1
                if opcao_invalida == True:
                    print('Digite uma opção válida!')
                try:
                    numero_check_in_selecionado = int(input('Digite o nº do check-in a ser feito o registro do consumo: ').strip())
                    if numero_check_in_selecionado >= 1 and numero_check_in_selecionado <= contador:
                        numero_check_in_selecionado -= 1
                        check_in_selecionado = lista_de_check_in_do_cliente[numero_check_in_selecionado]
                        opcao_invalida = False
                        while True:
                            os.system('cls') or None
                            print('\n..:: Registrar Consumo ::..\n')
                            print('Lista de produtos na copa:')
                            contador = 1
                            for consumo in self.__produto:
                                print(f'{contador} - {consumo.get_nome()} por R$ {consumo.get_preco():.2f}')
                                contador += 1
                            print('\n')
                            if opcao_invalida == True:
                                print('Digite uma opção válida!')
                            try:
                                numero_consumo_selecionado = int(input('Digite o nº do produto desejado: ').strip())
                                if numero_consumo_selecionado >= 1 and numero_consumo_selecionado <= contador:
                                    numero_consumo_selecionado -= 1
                                    consumo_selecionado = self.__produto[numero_consumo_selecionado].get_codigo()
                                    check_in_selecionado.get_quarto().add_consumo(consumo_selecionado)
                                    os.system('cls') or None
                                    print('\n..:: Registrar Consumo ::..\n')
                                    print('Consumo registrado com sucesso!')
                                    input('\nPressione Enter para voltar ao menu: ')
                                    return self
                                else:
                                    opcao_invalida = True
                            except:
                                opcao_invalida = True
                    else:
                        opcao_invalida = True
                except:
                    opcao_invalida = True
        else:
            os.system('cls') or None
            print('\n..:: Registrar Consumo ::..\n')
            print('Cliente digitado não possui nenhum check-in no sistema.')
            input('\nPressione Enter para voltar ao menu: ')
            return self

class Reserva:
    def __init__(self, dia_inicio, dia_fim, cliente, quarto, status):
        self.__dia_inicio = int(dia_inicio)
        self.__dia_fim = int(dia_fim)
        self.__cliente = cliente.strip()
        if isinstance(quarto, Quarto):
            self.__quarto = quarto
        else:
            raise ValueError
        status = status.upper()
        if status in ['A', 'C', 'I', 'O']:
            self.__status = status
        else:
            raise ValueError

    # GETTERS E SETTERS:

    def get_dia_inicio(self):
        return self.__dia_inicio

    def get_dia_fim(self):
        return self.__dia_fim

    def get_cliente(self):
        return self.__cliente

    def get_quarto(self):
        return self.__quarto

    def get_status(self):
        return self.__status

    def set_dia_inicio(self, dia_inicio):
        self.__dia_inicio = int(dia_inicio)

    def set_dia_fim(self, dia_fim):
        self.__dia_fim = int(dia_fim)

    def set_cliente(self, cliente):
        self.__cliente = cliente.strip()

    def set_quarto(self, quarto):
        if isinstance(quarto, Quarto):
            self.__quarto = quarto
        else:
            raise ValueError

    def set_status(self, status):
        if status in ['A', 'C', 'I', 'O']:
            self.__status = status
        else:
            raise ValueError
        
    def serializar(self):
        return f'{self.__dia_inicio};{self.__dia_fim};{self.__cliente};{self.__quarto.get_numero()};{self.__status}'




class Quarto:
    def __init__(self, numero, categoria, diaria, consumo = None):
        self.__numero = int(numero)
        categoria = categoria.upper()
        if categoria in ['S', 'M', 'P']:
            self.__categoria = categoria
        else:
            raise ValueError
        self.__diaria = float(diaria)
        if consumo == None:
            self.__consumo = []
        else:    
            self.__consumo = consumo
            posicao = 0
            for con in self.__consumo:
                self.__consumo[posicao] = int(con)
                posicao += 1

    # GETTERS E SETTERS:
    
    def get_numero(self):
        return self.__numero
    
    def get_categoria(self):
        return self.__categoria
    
    def get_diaria(self):
        return self.__diaria
    
    def get_consumo(self):
        return self.__consumo
    
    def set_numero(self, numero):
        self.__numero = int(numero)

    def set_categoria(self, categoria):
        categoria = categoria.upper()
        if categoria in ['S', 'M', 'P']:
            self.__categoria = categoria
        else:
            raise ValueError

    def set_diaria(self, diaria):
        self.__diaria = float(diaria)

    def set_consumo(self, consumo):
        self.__consumo = consumo
        posicao = 0
        for con in self.__consumo:
            self.__consumo[posicao] = int(con)
            posicao += 1

    # ADDS E REMOVES:

    def add_consumo(self, consumo):
        self.__consumo.append(int(consumo))

    def remove_consumo(self, consumo):
        if consumo in self.__consumo:
            self.__consumo.remove()

    # OUTROS:
 
    def lista_consumo(self, pousada):
        lista_consumo = []
        for consumo in self.__consumo:
            for produto in pousada.get_produto():
                if produto.get_codigo() == consumo:
                    lista_consumo.append(produto)
        return lista_consumo    
    
    def valor_total_consumo(self, pousada):
        valor_total_consumo = 0.0
        for consumo in self.lista_consumo(pousada):
            valor_total_consumo += consumo.get_preco()
        return valor_total_consumo

    def limpa_consumo(self):
        self.__consumo = []

    def serializar(self):    
        return f'{self.__numero};{self.__categoria};{self.__diaria}\n'




class Produto:
    def __init__(self, codigo, nome, preco):
        self.__codigo = int(codigo)
        self.__nome = nome
        self.__preco = float(preco)

    # GETTERS E SETTERS:

    def get_codigo(self):
        return self.__codigo
    
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco
    
    def set_codigo(self, codigo):
        self.__codigo = int(codigo)

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = float(preco)

    def serializar(self):
        return f'{self.__codigo};{self.__nome};{self.__preco}\n'






        
    

