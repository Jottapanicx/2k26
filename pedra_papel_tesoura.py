# Pedra papel ou tesoura, faltou algumas vitorias e derrotas mas eu fiquei com preguiça de terminar

import random

objetos = ["Pedra", "Papel", "Tesoura"]

rodar_objeto = random.choice(objetos)

print("PEDRA PAPEL OU TESOURA")
print("o computador ja rodou, agora falta voce.")
jogador = input("\nDigite Sua escolha: ").lower()

if jogador == rodar_objeto:
print(f"Empate, voce jogou {jogador}, e o computador jogou {rodar_objeto}, portanto deu empate ! ")
elif jogador == "Pedra" and rodar_objeto == "Tesoura":
print("Voce ganhou, Pedra amassa Tesoura !")

elif jogador == "Tesoura" and rodar_objeto == "Pedra":
print("O computador ganhou, Pedra ganha de Tesoura !")

elif jogador == "Papel" and rodar_objeto == "Pedra":
print("Voce ganhou, Papel ganha de Pedra ! ")

elif jogador == "Pedra" and rodar_objeto == "Papel":
print("O computador ganhou, Papel vence Pedra !")

elif jogador == "Papel" and rodar_objeto == "Tesoura":
print("Voce perdeu, Papel perde pra Tesoura !  !")
