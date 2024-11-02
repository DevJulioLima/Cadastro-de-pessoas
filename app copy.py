# Listas para armazenar os dados
nome1 = []
cpf1 = []
idade1 = []

while True:
    print('\n')
    print('Digite uma opção:')
    opcao = input('Digite 1 para cadastrar \n'
                  'Digite 2 para listar \n'
                  'Digite 3 para alterar \n'
                  'Digite 4 para deletar todos os cadastros \n'
                  'Digite 5 para sair \n')

    # Cadastro
    if opcao == '1':
        nome2 = input('Digite seu nome completo: ')
        while len(nome2) <= 10:
            print('Erro! Digite um nome válido (mais de 10 caracteres).')
            nome2 = input('Digite seu nome completo: ')
        nome1.append(nome2)

        cpf2 = input('Digite seu CPF: ')
        while not cpf2.isdigit() or len(cpf2) != 11:
            print('Erro! O CPF deve ter exatamente 11 dígitos.')
            cpf2 = input('Digite seu CPF: ')
        cpf1.append(cpf2)

        idade2 = input('Digite sua idade: ')
        while not idade2.isdigit() or not (1 <= int(idade2) <= 150):
            print('Erro! Digite uma idade válida (1-150).')
            idade2 = input("Digite sua idade: ")
        idade1.append(idade2)
        print('\nCadastro realizado com sucesso!')

    # Listagem
    elif opcao == '2':
        if nome1:
            for i in range(len(nome1)):
                print(f'Cadastro {i + 1}: Nome: {nome1[i]}, CPF: {cpf1[i]}, Idade: {idade1[i]}')
        else:
            print("Nenhum cadastro encontrado.")

    # Alteração
    elif opcao == '3':
        if nome1:
            indice = int(input(f"Digite o número do cadastro para alterar (1 a {len(nome1)}): ")) - 1
            if 0 <= indice < len(nome1):
                idade_nova = input('Digite a nova idade: ')
                while not idade_nova.isdigit() or not (1 <= int(idade_nova) <= 150):
                    print('Erro: Digite uma idade válida (1-150).')
                    idade_nova = input("Digite sua nova idade: ")
                idade1[indice] = idade_nova
                print('Idade alterada com sucesso!')
            else:
                print("Índice inválido.")
        else:
            print("Nenhum cadastro para alterar.")

    # Deleção de todos os cadastros
    elif opcao == '4':
        nome1.clear()
        cpf1.clear()
        idade1.clear()
        print("Todos os cadastros foram deletados com sucesso!")

    # Sair
    elif opcao == '5':
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida. Tente novamente.")