# função recursiva
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1) 
    
    
number = int(input("Digite um número: "))
print(f"O fatorial de {number} é {fatorial(number)}")   
