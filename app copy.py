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
                  'Digite 4 para deletar os cadastros \n'
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
        
        # Adicionando a lógica p/ confirmar que as informações estão corretas (S/N)
        confirmar = input('Confirma que as informações estão corretas? (S/N): ').strip().upper()
        while confirmar not in ('S', 'N'):
            print('Erro! Digite "S" para sim ou "N" para não')
            confirmar = input('Confirma as informações? (S/N): ').strip().upper()

        if confirmar == 'S':
            print('\nCadastro realizado com sucesso!')
        else:
            print('\nCadastro cancelado. Por favor, revise e modique os seus dados!')

            # Revisando e modificando os dados
            nome2 = input(f'Nome atual: {nome1[-1]}. Digite o novo nome ou pressione Enter para manter: ')
            if len(nome2) > 10:
                nome1[-1] = nome2  # Atualiza o nome se um novo nome válido for inserido

            # Revisar e modificar CPF
            cpf2 = input(f'CPF atual: {cpf1[-1]}. Digite o novo CPF ou pressione Enter para manter: ')
            if cpf2.isdigit() and len(cpf2) == 11:
                cpf1[-1] = cpf2  # Atualiza o CPF se um novo CPF válido for inserido

            # Revisar e modificar idade
            idade2 = input(f'Idade atual: {idade1[-1]}. Digite a nova idade ou pressione Enter para manter: ')
            if idade2.isdigit() and (1 <= int(idade2) <= 150):
                idade1[-1] = idade2  # Atualiza a idade se uma nova idade válida for inserida

            print('Dados atualizados com sucesso!')

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