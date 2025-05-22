import random

#selecionar valor aleatorio de uma lista
lista = [1, 2, 3, 4, 5]
valor_aleatorio = random.choice(lista)
print(f"Valor aleatório selecionado da lista: {valor_aleatorio}")
#selecionar valor aleatorio de um range
valor_aleatorio = random.randint(1, 10)
print(f"Valor aleatório selecionado do range: {valor_aleatorio}")
#selecionar valor aleatorio de um range com passo
valor_aleatorio = random.randrange(1, 10, 2)

print(f"Valor aleatório selecionado do range com passo: {valor_aleatorio}")
#selecionar valor aleatorio de uma string
string = "Python"
valor_aleatorio = random.choice(string)
print(f"Valor aleatório selecionado da string: {valor_aleatorio}")
#selecionar valor aleatorio de um dicionario
dicionario = {"a": 1, "b": 2, "c": 3}
valor_aleatorio = random.choice(list(dicionario.keys()))
print(f"Valor aleatório selecionado do dicionário: {valor_aleatorio}")
#selecionar valor aleatorio de um dicionario
dicionario = {"a": 1, "b": 2, "c": 3}
valor_aleatorio = random.choice(list(dicionario.values()))
print(f"Valor aleatório selecionado do dicionário: {valor_aleatorio}")


