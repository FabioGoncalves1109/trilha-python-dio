import textwrap
from modelos import Deposito, Saque
from operacoes import criar_usuario, criar_conta, listar_contas, exibir_extrato


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao in ["d", "s", "e"]:
            cpf = input("Informe o CPF: ")
            cliente = next((u for u in usuarios if u.cpf == cpf), None)

            if not cliente or not cliente.contas:
                print("\n@@@ Cliente não encontrado ou sem conta. @@@")
                continue

            conta = cliente.contas[0]  # Simples: só 1 conta por enquanto

            if opcao == "d":
                valor = float(input("Valor do depósito: "))
                cliente.realizar_transacao(conta, Deposito(valor))

            elif opcao == "s":
                valor = float(input("Valor do saque: "))
                cliente.realizar_transacao(conta, Saque(valor))

            elif opcao == "e":
                exibir_extrato(conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero = len(contas) + 1
            criar_conta(numero, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Opção inválida. @@@")

if __name__ == "__main__":
    main()