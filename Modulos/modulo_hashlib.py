#Para trabalhar com criptografia de textos, o Python possui a biblioteca hashlib, que fornece uma interface para algoritmos de hash criptográfico.
import hashlib

#verificar algoritmos de hash disponíveis
algoritmos = hashlib.algorithms_available
print("Algoritmos de hash disponíveis:")
for algoritmo in algoritmos:
    print(algoritmo)



#verificar algoritmos de hash disponíveis de acordo com o so
print(hashlib.algorithms_guaranteed)

#utilizando o sha256
texto = "Tr18365518!"
hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()
print(f"Texto encriptado - Hash SHA256: {hash_sha256}")

# utilizando o md5
hash_md5 = hashlib.md5(texto.encode()).hexdigest()
print(f"Texto encriptado - Hash MD5: {hash_md5}")

# utilizando o sha1
hash_sha1 = hashlib.sha1(texto.encode()).hexdigest()
print(f"Texto encriptado - Hash SHA1: {hash_sha1}")


