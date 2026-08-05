import os 

# trabalhando com arquivos txt em py

def menu():
  print(f"\n1 > ler arquivo")
  print("2 > escrever no arquivo")
  print("3 > criar arquivo")
  print("4 > sair")

def ler_arquivo():
  with open("outlooks.txt") as arquivo:
    print(arquivo.read())

def escrever_arquivo():
  with open("outlooks.txt", "a") as arquivo:
    escrever = input("Escreva no arquivo: ")

    arquivo.write("\n" + escrever)
    print("Texto escrito com sucesso !!")

def criar_arquivo():
  nome = input("Digite o nome do arquivo para criar: ")

  with open(f"{nome}.txt", "x") as newfile:
    print("arquivo criado com sucesso !")

while True:
  menu()
  try:
    escolha = int(input("> "))

    if escolha == 1:
      ler_arquivo()
    elif escolha == 2:
      escrever_arquivo()
    elif escolha == 3:
      criar_arquivo()
    elif escolha == 4:
      print("saindo...")
      break
    else:
      print("\nValor nao encontrado")
      
  except ValueError:
    print("\nDigite apenas numeros ! ")
  
