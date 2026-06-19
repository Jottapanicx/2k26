# pequeno sistema de loja
import os

nome = input("Qual seu nome: ")

produtovalor = float(input(f"\nQual o valor do produto que voce comprou senhor(a) {nome}: "))

quantidade = int(input(f"\nQuantos produtos voce comprou senhor(a) {nome}: "))

total = quantidade * produtovalor


print("LOJA NORTE")
print(f"\nCliente : {nome}")
print(f"Produtos: {quantidade}")
print(f"\nValor do produto: {produtovalor}")
print(f"\nSubtotal: {total}")
print(f"\nTOTAL A PAGAR: {total}")

input("\nAperte ENTER para resetar o painel: ")
os.system("clear")
  
