#print("Olá Mundo!")
#print("Aprendendo Python")
# Linha de comentario para uma linha
"""
Linha de comentario para mais de uma linha
"""

#num = 1
#Texto = "Texto string"
#dtnascto = "01/01/2000"
#valor = 7.5
#verdadeurooufalse = True

#print(num)
#print(type(num))
#print(Texto)
#print(type(Texto))
#print(dtnascto)
#print(type(dtnascto))
#print(valor)
#print(type(valor))
#print(verdadeurooufalse)
#print(type(verdadeurooufalse))

#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))
#print("Olá " + nome + ", você tem " + str(idade) + " anos.")

nome = input("Digite seu nome: ")
nome2 = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
nomecompleto = nome + " " + nome2
print("Olá " + nomecompleto + ", você tem " + str(idade) + " anos.")

print(nome[0:]) #busca toda a string a prtir da posiçao 0 - primeira posição
print(nome[:6]) #busca a string da posição 0 até a 6
print(nome[2:6]) #busca a string da posição 2 até a 6   
print(nome[::2]) #busca a string de 
print(nome[1::2]) #busca a string somente as posições impares
print(nome[-1]) #busca a string da última posição   
print(nome[-2]) #busca a string da penúltima posição
print(nome[-3]) #busca a string da antepenúltima posição
nome3 = print(nome[::-1]) #busca a string de trás para frente
if(nome == nome3):
    print("O nome é igual, essa string é um palíndromo")
else:
    print("O nome não é igual, essa string não é um palíndromo")

