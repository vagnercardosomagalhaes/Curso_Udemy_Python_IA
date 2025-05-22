import statistics

listnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listnum2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(statistics.mean(listnum)) #Média
print(statistics.median(listnum)) #Mediana
print(statistics.mode(listnum)) #Moda

print(statistics.stdev(listnum)) #Desvio padrão

print(statistics.variance(listnum)) #Variância
print(statistics.pstdev(listnum)) #Desvio padrão populacional
print(statistics.pvariance(listnum)) #Variância populacional

print(statistics.median_low(listnum)) #Mediana baixa
print(statistics.median_high(listnum)) #Mediana alta
print(statistics.median_grouped(listnum)) #Mediana agrupada

print(statistics.quantiles(listnum)) #Quantis

print(statistics.mode(listnum2)) #Moda
print(statistics.multimode(listnum2)) #Multimodal
print(statistics.median_grouped(listnum2)) #Mediana agrupada
print(statistics.median_low(listnum2)) #Mediana baixa
print(statistics.median_high(listnum2)) #Mediana alta

print(statistics.quantiles(listnum2)) #Quantis



