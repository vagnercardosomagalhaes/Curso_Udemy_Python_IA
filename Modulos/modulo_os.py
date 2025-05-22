#Módulo OS
import os

#Retornar pasta atual
#print(os.getcwd())

#Criar pasta no diretorio atual
#os.mkdir('pasta')

#Criar pasta com nome e caminho
if not os.path.exists('C:\\temp\\python\\pasta3'):
    os.mkdir('C:\\temp\\python\\pasta3')

                      
if not os.path.exists('C:\\temp\\python\\pasta3\\pasta4'):
    os.mkdir('C:\\temp\\python\\pasta3\\pasta4')


#Para criar a pasta com todo o caminho, caso o caminho não exista 
# os.makedirs('C:\\temp\\python\\pasta5\\pasta6')
# 
##Renomear pasta
#os.rename('pasta', 'pasta_renomeada')
#Remover pasta
#os.rmdir('pasta_renomeada')
#Remover pasta com caminho
#os.rmdir('C:/temp/python/pasta3')
#Remover pasta com caminho e nome
#os.rmdir('C:/temp/python/pasta3/pasta4')    



#Listar arquivos e pastas
print(os.listdir())

os.system('systeminfo') #Informações do sistema

os.system('cls')

os.system('shutdown /s /t 10') #Desligar o computador em 10 segundos







