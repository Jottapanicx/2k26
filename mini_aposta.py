# mini casa de apostaa
import random 

saldo = 0 

def menu():
  print("CASA DE APOSTA ")
  print("€ saldo :", saldo)
  print("\n1 - apostar ")
  print("2 - depositar  ")
  print("3 - sacar ")
  print("4 - sair ")
  
def aposta():
  global saldo
  
  print("ADVINHE O NUMERO ")
  
  c = random.randint(1, 10)
  
  print("\nA maquina rodou o numero , tente adivinhar !")
  
  v = int(input("\nQual valor voce deseja apostar? : "))
  
  if v > saldo:
    print("Voce nao tem essa grana neguin ! ")
    
    return 
  else:
    print("Grana apostada !")
    
  saldo -= v
  
  es = int(input("\nQual numero voce acha que a maquina rodou? ; "))
  
  if es == c:
    print(f"ACERTOUUUU, O NUMERO ERA {c} , sua aposta foi duplicadaaa !!!!")
    
    saldo += v * 2
    
  else:
    print(f"ERROUUUUU, O NUMERO ERA {c}")
    
def deposito():
  global saldo
  
  dps = int(input("\nQual valor voce deseja depositar? :"))
  
  saldo = dps + saldo 
  
  print(f"\nO valor de {dps} foi depositado com suceso !")
  
def saque():
  global saldo 
  
  sq = int(input("\nQual valor voce deseja sacar ? : "))
  
  if sq > saldo:
    print("\nVoce nao tem essa grana neguinho !")
  else:
    print("\nSaque efetuado com sucesso !")
  
  saldo = sq - saldo 
  
  
while True:
  menu()
  
  o = input("\nEscolha uma opcao: ")
  
  if o == "1":
    aposta()
  elif o == "2":
    deposito()
  elif o == "3":
    saque()
  elif o == "4":
    print("\nSaindo.......")
    break
  else:
    print("\nopcao invalida !")
