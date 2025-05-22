import re

text = "Aprenda a Usar Pillow, OpenCV, MediaPipe, Hugging Face, NLTK, Spacy e muito mais para criar Aplicações Robustas em IA"

match = re.search(r"muito mais", text)
print(f"Indice inicial: {match.start()}")
print(f"Indice  final: {match.end()}")

#Buscando indice do .
site="https://www.google.com"
match = re.search(r"\.", site)
print(match)

#Buscando todas as letras entre g e m dentro de uma string
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)   

#verificando inicio da string
rule = "^A"
phrases = ["Aprenda a Usar Pillow", "Aprenda a Usar Pillow, OpenCV, MediaPipe, Hugging Face, NLTK, Spacy e muito mais para criar Aplicações Robustas em IA"]
for phrase in phrases:
    match = re.search(rule, phrase)
    if match:
        print(f"A frase '{phrase}' começa com 'A'.")    
result = re.findall(pattern, text)

#verificar final da string
rule = "IA$"
phrases = ["Aprenda a Usar Pillow", "Aprenda a Usar Pillow, OpenCV, MediaPipe, Hugging Face, NLTK, Spacy e muito mais para criar Aplicações Robustas em IA"]
for phrase in phrases:
    match = re.search(rule, phrase)
    if match:
        print(f"A frase '{phrase}' termina com 'IA'.")
        result = re.findall(pattern, text)
print(result)

#verificando se a string é composta apenas por letras
rule = "^[a-zA-Z]+$"
phrases = ["Aprenda a Usar Pillow", "Aprenda a Usar Pillow, OpenCV, MediaPipe, Hugging Face, NLTK, Spacy e muito mais para criar Aplicações Robustas em IA"]
for phrase in phrases:
    match = re.search(rule, phrase)
    if match:
        print(f"A frase '{phrase}' é composta apenas por letras.")
        result = re.findall(pattern, text)
print(result)

#verificando se a string é composta apenas por letras e espaços
rule = "^[a-zA-Z\s]+$"
phrases = ["Aprenda a Usar Pillow", "Aprenda a Usar Pillow, OpenCV, MediaPipe, Hugging Face, NLTK, Spacy e muito mais para criar Aplicações Robustas em IA"]
for phrase in phrases:
    match = re.search(rule, phrase)
    if match:
        print(f"A frase '{phrase}' é composta apenas por letras e espaços.")
        result = re.findall(pattern, text)
print(result)




