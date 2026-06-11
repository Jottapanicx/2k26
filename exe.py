import os

tarefas = []

def menu():
    print("1 ~ adcionar tarefa")
    print("2 ~ remover tarefa")
    print("3 ~ ver tarefas")
    print("4 ~ sair")
    
def adc():
    al = input("\n[+] Digite sua tarefa: ")
    
    tarefas.append(al)
    
    print("\nTarefa adcionada com sucesso ! ")
    
def rmv():
    print(tarefas)
    
    rm = input("\n[+] Qual tarefa voce quer remover: ")
    
    if rm in tarefas:
      tarefas.remove(rm)
      print("\nTarefa removida com sucesso ! ")
    else:
      print("\nTarefa não encontrada !  ! ")
  
  
def vt():
    print("Lista de tarefas ")
    for i, tarefa in enumerate(tarefas):
      print("\n", i, tarefas)
    
while True:
  menu()
  
  e = input("\n[+] Digite uma opção: ")
  
  if e == "1":
    adc()
  elif e == "2":
    rmv()
  elif e == "3":
    vt()
  elif e == "4":
    print("Saindo....")
    break
  else:
    print("\nOpção invalida ! ")