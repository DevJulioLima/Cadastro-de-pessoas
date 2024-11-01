nome1 =[]
cpf1 = []
idade1 = []

while True:
    print('digite uma opcao')
    opcao = input('digite 1 para cadastrar: \n'
                  'digite 2 para listar: \n'
                  'digite 3 para alterar: \n'
                  'digite 4 para deletar: \n')
    
    if opcao == '1':
        nome2 = input('digite seu nome completo: ')
        while len(nome2) <= 10:
            nome2 = input('digite seu nome completo: ')
            print('erro! digite um nome valido')
        nome1.append(nome2)

        cpf2 = input('digite seu cpf: ')
        while not cpf2.isdigit() or len(cpf2) != 11:
            print('erro! o cpf deve ter exatamente 11 dígitos.')
            cpf2 = input('digite seu cpf: ')
        cpf1.append(cpf2)

        idade2 = input('digite sua idade: ')
        while not idade2.isdigit() or not (1 <= int(idade2) <= 9 or 11 <= int(idade2) <= 99 or 100 <= int(idade2) <= 150):
            print('Erro: digite uma idade válida!')
            idade2 = input("Digite sua idade: ")
        idade1.append(idade2)

    elif opcao == '2':
        print(f'nome: {nome2}\n cpf: {cpf2}\n idade: {idade2}')





            



        