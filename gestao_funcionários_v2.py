import os

usuarios = [
    {"Nome": "João", "Idade": 17},
    {"Nome": "Maria", "Idade": 20},
    {"Nome": "Carlos", "Idade": 25}
]
def menu():
  print(f"\nSISTEMA DE GERENCIAMENTO DE USUARIOS")
  print(f"Total de usuarios : {len(usuarios)}")
  print("\n< 1 >  Cadastrar usuario")
  print("< 2 >  Ver usuarios")
  print("< 3 >  remover usuarios")
  print("< 4 >  sair")
  
def cadastrar_usuarios():
  os.system("clear")
  try:
    print(f"CADASTRO DE USUARIOS")
    print(f"Usuarios cadastrados {len(usuarios)}")
    nome = input("\n[+] Digite seu nome: ")
    if not nome.isalpha():
      raise ValueError

  except ValueError:
    print("\nDigite apenas numeros !")
  else:
    usuario = {
      "Nome": nome
    }

    usuarios.append(usuario)

    print(f"\n{nome} cadastrado com sucesso !")
    
def ver_usuarios():
  for i, usuario in enumerate(usuarios):
    print(f"\numero > {i}")

    for chave, valor in usuario.items():
      print(f"{chave}: {valor}")

def remover_usuarios():
  for i, usuario in enumerate(usuarios):
    print(f"\n{i} - {usuario['Nome']}")
  try:
    remover = int(input("\nDigite o numero do usuario:  "))
    usuarios.pop(remover)
    if remover not in usuarios:
      print("\nNumero nao encontrado !")
  except ValueError:
    print("\nDigite apenas numeros !")
  else:
    print(f"\nUsuario {remover} removido.")
  
while True:
  menu()
  try:
    e = int(input("\n[+] Opção:  "))
    if e == 1:
      cadastrar_usuarios()
    elif e == 2:
      ver_usuarios()
    elif e == 3:
      remover_usuarios()
    elif e == 4:
      print("\nsaindo...")
      break
  except ValueError:
    print("\nDigite apenas o numero da Opção")


    
