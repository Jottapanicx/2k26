import random 
import string 

caracteres = string.ascii_letters + string.digits 

tamanh = int(input("[+] Escreva o tamanho da sua key: "))

senha = ""

for _ in range(tamanh):
 senha += random.choice(caracteres)
 
print("[+] Senha gerada: ", senha)