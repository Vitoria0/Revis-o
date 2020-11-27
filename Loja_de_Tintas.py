# Faça um Programa para uma loja de tintas. O programa deve pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R $ 80,00 ou em galões de 3,6 litros, que custam R $ 25,00.

# Informe ao usuário como quantidades de tinta a serem compradas e os preços específicos em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

l  =  float ( input ( 'Largura da parede:' ))
a  =  float ( input ( 'Altura da parede:' ))
ar  =  l  *  a
print ( "Sua parede tem a dimenção de {} x {} e a sua área é de {} m²" . format ( l , a , ar ))
t  =  ar  /  2
print ( "Para pintar essa parede você precisa de {} l de tinta".format( t ))
print('''
Latas de 18 litros custam R$ 80,00
Galões de 3,6 litros custam R$ 25,00
''')