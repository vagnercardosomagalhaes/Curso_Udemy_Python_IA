# funções
def bemvindo():
    print('Bem-vindo ao meu programa!')


bemvindo() 

#def calcule():
#    num1 = int(input('Digite o primeiro número: '))
#    num2 = int(input('Digite o segundo número: '))
#    soma = num1 + num2
#    print(f'A soma de {num1} e {num2} é {soma}')


#calcule()

#def calcule2():
#    num3 = int(input('Digite o primeiro número: '))
#    num4 = int(input('Digite o segundo número: '))
#    soma2 = num3 + num4
#    #print(f'A soma de {num1} e {num2} é {soma}')
#    return soma2


#print(f"A soma dos dois numeros é: {calcule2():.2f}")


def cadnome():
    nome = input('Digite seu nome: ')
    return nome

nome_cadastrado = cadnome()
print(f"O nome cadastrado é: {nome_cadastrado}")

