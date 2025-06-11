from modelos import PessoaFisica, Deposito, Saque


def criar_usuario(usuarios):
    cpf = input("CPF (somente números): ")
    if any(u.cpf == cpf for u in usuarios):
        print("\n@@@ Usuário já existe. @@@")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço: ")

    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    usuarios.append(cliente)
    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(numero, usuarios, contas):
    cpf = input("CPF do usuário: ")
    cliente = next((u for u in usuarios if u.cpf == cpf), None)
    if not cliente:
        print("\n@@@ Usuário não encontrado. @@@")
        return

    conta = cliente.contas[0].__class__.nova_conta(cliente, numero)  # Usa mesma classe da primeira conta
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 50)
        print(f"Agência: {conta.agencia}")
        print(f"C/C: {conta.numero}")
        print(f"Titular: {conta.cliente.nome}")


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in conta.historico.transacoes:
            print(f"{t['tipo']}: R$ {t['valor']:.2f} em {t['data']}")
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("==========================================")