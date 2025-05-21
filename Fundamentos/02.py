#Lista

nomes=["Vagner", "Lucas", "Gustavo", "Gabriel", "Felipe", "Matheus", "João"]
print (type(nomes))
print (nomes[0]) #busca o primeiro elemento da lista
print (nomes[1]) #busca o segundo elemento da lista
print (nomes[5]) #busca o quinto elemento da lista
print (nomes[0:3]) #busca os três primeiros elementos da lista
print (nomes[3:]) #busca os elementos a partir do quarto elemento da lista
print (nomes[-1]) #busca o ultimo elemento da lista
print(len(nomes)) #busca o tamanho da lista
print(nomes.index("Vagner")) #busca o índice do elemento "Vagner" na lista
nomes.append("Ana_Clara") #adiciona o elemento "Vagner" no final da lista
print(nomes) #imprime a lista
nomescopia = nomes.copy() #faz uma cópia da lista
nomescopia.remove("Gabriel") #remove o elemento "Ana_Clara" da lista
print(nomescopia) #imprime a lista
nomescopia.clear() #limpa a lista
print(nomescopia) #imprime a lista  