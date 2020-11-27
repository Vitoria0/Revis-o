# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# aparecem vezes como vogais a, e, i, o, u.

    # Bom codigo, só o print final que ficou vazio, e acaba dando erro no codigo.

palavras = []
palavras.append(input('Digite uma frase: '))
#vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:  # Verifica cada palavra
    print(f'A frase {p} tem as vogais: ', end='')
    for l in p:  # Verifica cada letra da palavra
        if l in 'aeiouáéíóúãõê':
            print(l, end='-')
    print('')
    print(len())