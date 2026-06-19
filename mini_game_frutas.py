#mini game de acertar frutas 
import random
import os

acertos = 0
erros = 0

frutas = [
    "Maçã",
    "Banana",
    "Laranja",
    "Uva",
    "Manga",
    "Abacaxi",
    "Morango",
    "Melancia",
    "Pera",
    "Kiwi"
]

while True:
  fruits = random.choice(frutas)
  
  print("\nAcerte a fruta do cesto :3")
  print(f"voce mete a mão no cesto, agora descubra qual fruta voce irá puxar")
  print(f"\nAcertos: {acertos}")
  print(f"\nErros: {erros}")
  print("\nas frutas são:")

  for i in frutas:
    print(i)

  escolha = input("\n{~} Qual fruta voc acha que voce pegou?: ")

  if escolha == fruits:
    print(f"Voce acertouu, a fruta que voce puxou é a(o) {fruits}")

    acertos = acertos + 1
    print("\n +1 acertos")

    input("Aperte ENTER para resetar: ")
    os.system("clear")

  else:
    print(f"Erroou, a fruta era {fruits}")

    erros = erros + 1

    print("\n +1 erro")
    
    input("Aperte ENTER para resetar: ")
    os.system("clear")
  
