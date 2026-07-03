# mini sistema de gestão de funcionarios
funcionarios = []

def menu():
  print("1 > cadastro de funcionarios")
  print("2 > ver funcionarios")
  print("3 > remover funcionarios")
  print("4 > buscar funcionarios pelo nome")
  print("5 > sair")

def cadastrar_funcionarios():
  nome = input("<\> Digite seu nome: ")
  idade = int(input("<\> Digite a sua idade: "))
  cidade = input("<\> Digite sua cidade: ")
  cargo = input("<\> Qual cargo voce deseja alcansar: "))

  funcionario = {
    "Nome": nome,
    "Idade": idade,
    "Cidade": cidade,
    "Cargo": cargo
  }
  
  funcionarios.append(funcionario)
  
  print("\n<\> Funcionario cadastrado com sucesso ! ")

def ver_usuarios_cadastrados():
  print("Total de usuarios cadastrados: ", len(funcionarios))

  for indice, funcionario in enumerate(funcionarios, start=1):
    print(f"{indice}: {funcionario['nome']}")

def remover_funcionario():
  indice = int(input("Digite o indice de qual funcionario voce quer remover: "))

  if 1 <= indice <= len(funcionarios):
    removido = funcionarios.pop(indice - 1)
    print(f"{removido['nome']} foi removido com sucesso ! ")
  else:
    print("Indice não encontrado !")

def buscar_funcionario():
  print("\nSistema de busca de funcionario pelo nome ")
  busca = input("\nDigite o nome do funcionario: ")

  for funcionario in funcionarios:
    if busca == funcionario['Nome']:
      print(f"Nome: {funcionario['Nome']}")
      print(f"Idade: {funcionario['Idade']}")
      print(f"Cidade: {funcionario['Cidade']}")
      print(f"Cargo: {funcionario['Cargo']}")
      
while True:
  menu()
  e = int(input("\nDigite a opção: "))

  if e == 1:
    cadastrar_funcionarios()
  elif e == 2: 
    ver_usuarios_cadastrados()
  elif e == 3:
    remover_funcionario()
  elif e == 4: 
    buscar_funcionario()
  elif e == 5:
    print("saindo...")
    break
  else:
    print("Opção invalida ! ")

