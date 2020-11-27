# Faça um programa que simule um lançamento de dados.
# Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, muitas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores (1-6) e uma função para gerar numeros aleatórios,
# simulando os lançamentos dos dados.,0

from random import randrange
lista = []

for i in range(100):
    lista.append(randrange(1,7))

print(lista)

for i in range (1,7):
    print(f'O número {i} apareceu', lista.count(i), 'vezes')
