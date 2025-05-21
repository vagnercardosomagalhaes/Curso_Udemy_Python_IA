#Função lambda
power = lambda x: x ** 2

is_even = lambda x: x % 2 == 0

mdiv_num = lambda x, y: x / y if y != 0 else "Divisão por zero não é permitida"

reverse_string = lambda s: s[::-1]

nomes=["Vagner", "Lucas", "Gustavo", "Gabriel", "Felipe", "Matheus", "João"]
notas={
    "Vagner": [10,8,7], 
    "Lucas" : [9, 8, 7],     
    "Gustavo": [8, 7, 6], 
    "Gabriel": [7,  6, 5], 
    "Felipe": [6,8, 7],
    "Matheus": [5, 6, 7],        
    "João": [4,9, 8]    
    }

avarage_notas = lambda nomes: sum(notas[nomes]) / len(notas[nomes])
print(f"Media do Vagner: {avarage_notas('Vagner')}")
print(f"Media do Lucas: {avarage_notas('Lucas')}")
print(f"Media do Gustavo: {avarage_notas('Gustavo')}")
print(f"Media do Gabriel: {avarage_notas('Gabriel')}")
print(f"Media do Felipe: {avarage_notas('Felipe')}")    
print(f"Media do Matheus: {avarage_notas('Matheus')}")
print(f"Media do João: {avarage_notas('João')}")    


print(power(2))
print(power(3))

print(is_even(30))
print(is_even(27))

print(mdiv_num(10, 2))
print(mdiv_num(10, 0))

print(reverse_string("Python"))
print(reverse_string("Fundamentos"))