# Módulo principal del programa
import math_operations
from math_operations import multiply, divide
import string_utils


print(math_operations.sum(5, 3))  # Exibe: 8
print(math_operations.subtract(5, 3))  # Exibe: 2

print(multiply(5, 3))  # Exibe: 15
print(divide(5, 3))  # Exibe: 1.6666666666666667
#print(divide(5, 0))  # Exibe: ValueError: Divisão por zero não é permitida.

print(string_utils.capitalize_string("olá mundo"))  # Exibe: Olá mundo
print(string_utils.reverse_string("flamengo"))  # Exibe: ognemalf
print(string_utils.count("Vagner Cardos de Magalhaes"))  # Exibe: 26







