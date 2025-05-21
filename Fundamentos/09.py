# list comprehension

listnum = [i for i in range(10) if i < 4]
print(listnum)

nomes=["Vagner", "Lucas", "Gustavo", "Gabriel", "Felipe", "Matheus", "João"]
nomecomE = [nome for nome in nomes if "e" in nome.lower()]
