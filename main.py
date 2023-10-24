from lib import *

# Calcula o fatorial

# variáveis
# fat = 1

while True:
    # Apresentação
    print('\n\t\t\t -- Sistema Matemático -- \n\n')

    print('1. Fatorial')
    print('2. Tabuada')
    print('3. Sair')

    # Ler a opção do usuário
    op = int(input('Informe a opção desejada: '))

    if op == 1:
        print('\n\t\t\t -- Calcula Fatorial \n\n')

        #Entrada
        num = int(input('Informe um número: '))

        # Processamento
        fat = gera_fatorial(num)

       # for cont in range(1, num+1):
            # fat *= cont
            # fat = fat * cont

        # Saída
        print(f'{num}! = {fat}')
    elif op == 2:
        print('\n\t\t\t -- Tabuada -- ')

        # Entrada
        num = int(input('Informe o número: '))

        # Processamento e Saída
        gerar_tabuada(num)

    elif op == 3:
        # Sair do sistema
        print('\nAbraço!\n')
        break
    else:
        # Opção incorreta
        print(f'\nOpção {op} incorreta!\n')
