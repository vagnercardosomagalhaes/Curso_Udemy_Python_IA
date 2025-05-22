import math

print(math.pi) #Número pi
print(f"Número pi: {math.pi:.2f}") #Número pi com 2 casas decimais
print(math.e) #Número e
print(f"Número e: {math.e:.2f}") #Número e com 2 casas decimais

#arredondamento de numeros
print(math.ceil(5.4)) #Arredondar para cima
print(math.floor(5.4)) #Arredondar para baixo
print(math.trunc(5.4)) #Truncar o número


num2 = input("Digite um número: ")
print(math.factorial(num2)) #Fatorial de num2


print(math.sqrt(25)) #Raiz quadrada de 25
print(math.pow(2, 3)) #2 elevado a 3
print(math.log(100, 10)) #Logaritmo de 100 na base 10
print(math.log(100)) #Logaritmo natural de 100
print(math.log10(100)) #Logaritmo de 100 na base 10
print(math.sin(math.radians(90))) #Seno de 90 graus
print(math.cos(math.radians(90))) #Cosseno de 90 graus
print(math.tan(math.radians(90))) #Tangente de 90 graus
print(math.degrees(1)) #Converter radianos para graus
print(math.radians(180)) #Converter graus para radianos
print(math.hypot(3, 4)) #Hipotenusa de um triângulo retângulo
print(math.isclose(0.1 + 0.2, 0.3)) #Verifica se dois números são próximos
print(math.isfinite(1.0)) #Verifica se o número é finito
print(math.isinf(float('inf'))) #Verifica se o número é infinito
print(math.isnan(float('nan'))) #Verifica se o número é NaN
print(math.gcd(12, 15)) #Máximo divisor comum
print(math.lcm(12, 15)) #Mínimo múltiplo comum
print(math.dist((1, 2), (4, 6))) #Distância entre dois pontos
print(math.prod([1, 2, 3, 4, 5])) #Produto de uma lista
print(math.comb(5, 2)) #Combinação de 5 elementos tomados 2 a 2
print(math.perm(5, 2)) #Permutação de 5 elementos tomados 2 a 2
print(math.isqrt(25)) #Raiz quadrada inteira de 25
print(math.remainder(5, 2)) #Resto da divisão de 5 por 2
print(math.copysign(5, -1)) #Copia o sinal de -1 para 5

