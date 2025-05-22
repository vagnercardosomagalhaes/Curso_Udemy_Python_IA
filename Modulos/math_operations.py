#Módulo de operaciones matemáticas
def sum(a, b):
    """Suma dos números a e b"""
    return a + b

def subtract(a, b):
    """Resta dos números a e b"""
    return a - b    

def multiply(a, b):
    """Multiplicação dos números a e b"""
    return a * b    

def divide(a, b):   
    """Divisão dos números a e b"""
    if b != 0:
        return a / b
    else:   
        raise ValueError("Divisão por zero não é permitida.")
        


