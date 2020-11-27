# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# aparecem vezes como vogais a, e, i, o, u.

def contador(f):
    frase = f.lower()
    print(f'''
    Frase: {f}
    Quantidade de A: {f.count('a')}
    Quantidade de E: {f.count('b')}
    Quantidade de I: {f.count('c')}
    Quantidade de O: {f.count('d')}
    Quantidade de U: {f.count('e')}
    Quantidade de espaços em branco: {f.count(' ')}
    ''')

if __name__ == "__main__":

    f = str(input('Digite uma frase: '))
    contador(f)
