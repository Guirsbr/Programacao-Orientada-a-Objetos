import sistema

if __name__ == '__main__':
    sistema = sistema.Sistema()
    opcao = ''
    while opcao != '0':
        opcao = sistema.menu()
        match opcao:
            case '1':
                sistema.criar_processo()
            case '2':
                sistema.executar_proximo()
            case '3':
                sistema.executar_processo_especifico()
            case '4':
                sistema.salvar_a_fila_de_processos()
            case '5':
                sistema.carregar_do_arquivo_a_fila_de_processos()
            case '0':
                continue