#Parametros args e kwargs
def soma(*args):
    total = 0
    for i in args:
        total += i
    print(f"A soma dos números é: {total}")

soma(9,7,8,5,4,3,2,1)

def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print("Lista de cusrsos:")
presentation(nome = "Python", curso = "Fundamentos", ano = 2023, semestre = 1)
presentation(nome = "C#", curso = "Fundamentos", ano = 2023, semestre = 2)
presentation(nome = "Java", curso = "Fundamentos", ano = 2023, semestre = 3)
        
