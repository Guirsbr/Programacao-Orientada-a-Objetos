import funcoes
import classes

def main():
    pousada_bons_sonhos = classes.Pousada()
    pousada_bons_sonhos.carregar_dados()
    opcao = ''
    while opcao != '0':
        opcao = funcoes.menu()
        match opcao:
            case '1':
                continue
            case '2':
                continue
            case '3':
                funcoes.realizar_reserva(pousada_bons_sonhos)
            case '4':
                continue
            case '5':
                funcoes.realizar_check_in(pousada_bons_sonhos)
            case '6':
                funcoes.realizar_check_out(pousada_bons_sonhos)
            case '7':
                funcoes.registrar_consumo(pousada_bons_sonhos)
            case '8':
                funcoes.salvar(pousada_bons_sonhos)
            case '0':
                funcoes.sair()


if __name__ == '__main__':
    main()


