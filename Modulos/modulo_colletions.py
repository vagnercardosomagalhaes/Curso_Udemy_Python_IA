from collections import Counter, namedtuple, deque
from operator import itemgetter

# realizar uma contagem dentro de uma lista

frutas = ["banana", "maçã", "laranja", "banana", "maçã", "banana", "melancia", "banana", "maçã", "laranja"]
contagem_frutas = Counter(frutas)
print("Contagem de frutas:")
for fruta, contagem in contagem_frutas.items():
    print(f"{fruta}: {contagem}")
print()

#usando uma tupla nomeada
# Uma tupla nomeada é uma subclasse de tuple que permite acessar os elementos por nome em vez de índice.
# Isso pode tornar o código mais legível e auto-documentado.
# Criando uma tupla nomeada chamada "Ponto" com dois campos: "x" e "y"
Ponto = namedtuple("Ponto", ["x", "y"])
# Criando uma instância da tupla nomeada
ponto1 = Ponto(10, 20)
ponto2 = Ponto(30, 40)
print(f"Ponto 1: x={ponto1.x}, y={ponto1.y}")
print(f"Ponto 2: x={ponto2.x}, y={ponto2.y}")
print()
# Criando uma lista de tuplas nomeadas
pontos = [Ponto(1, 2), Ponto(3, 4), Ponto(5, 6)]
# Ordenando a lista de tuplas nomeadas com base no campo "x"
pontos_ordenados = sorted(pontos, key=itemgetter(0))
print("Pontos ordenados por x:")
for ponto in pontos_ordenados:
    print(f"x={ponto.x}, y={ponto.y}")
print()
# Criando uma lista de tuplas nomeadas
pontos = [Ponto(1, 2), Ponto(3, 4), Ponto(5, 6)]
# Ordenando a lista de tuplas nomeadas com base no campo "y"
pontos_ordenados = sorted(pontos, key=itemgetter(1))
print("Pontos ordenados por y:")
for ponto in pontos_ordenados:
    print(f"x={ponto.x}, y={ponto.y}")
print()

#oORDENANDO DICIONARIOS
# Criando um dicionário
dicionario = {
    "banana": 3,
    "maçã": 2,
    "laranja": 5,
    "melancia": 1
}
# Ordenando o dicionário com base nos valores
dicionario_ordenado = sorted(dicionario.items(), key=lambda item: item[1])
print("Dicionário ordenado por valores:")
for chave, valor in dicionario_ordenado:
    print(f"{chave}: {valor}")
print()
# Criando um dicionário
dicionario = {
    "banana": 3,
    "maçã": 2,
    "laranja": 5,
    "melancia": 1
}   
# Ordenando o dicionário com base nas chaves
dicionario_ordenado = sorted(dicionario.items(), key=lambda item: item[0])
print("Dicionário ordenado por chaves:")
for chave, valor in dicionario_ordenado:
    print(f"{chave}: {valor}")
print()



