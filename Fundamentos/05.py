# Dicionarios
nomes = {
    "nome": "Vagner",
    "idade": 30,
    "altura": 1.80,
    "peso": 80,
    "cidade": "São Paulo",
    "estado": "SP",
    "pais": "Brasil",
    "profissao": "Desenvolvedor",
    "hobbies": ["programar", "jogar", "ler", "viajar"],
    "carro": {
        "marca": "Ford",
        "modelo": "Fusca",
        "ano": 1970,
        "cor": "azul"
    }    
}    
print(nomes["altura"])
print(nomes.get("cidade"))
print(nomes.get("carro").get("marca"))
print(nomes.get("carro").get("modelo"))
print(nomes.get("carro").get("ano"))
print(nomes.get("carro").get("cor"))
print(nomes.keys()) #busca as chaves do dicionario
print(nomes.values()) #busca os valores do dicionario
print(nomes.items()) #busca as chaves e os valores do dicionario
nomes["sexo"] = "masculino" #adiciona o elemento "sexo" no dicionario
print(nomes) #imprime o dicionario
nomes.update({"estado": "Rio de janeiro"}) #atualiza o elemento "estado" no dicionario
print(nomes) #imprime o dicionario