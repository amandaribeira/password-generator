import string
import random

caracteres = string.ascii_letters + string.digits
tamanho = int(input("Quantos caracteres?"))
senha = ""
for i in range(tamanho):
    senha += random.choice(caracteres)
print("Sua Senha:", senha)
