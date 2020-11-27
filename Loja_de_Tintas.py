# Faça um Programa para uma loja de tintas. O programa deve pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R $ 80,00 ou em galões de 3,6 litros, que custam R $ 25,00.

# Informe ao usuário como quantidades de tinta a serem compradas e os preços específicos em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metragem  =  float ( input ( 'INFORME QUANTOS MT² POSSUI A ÁREA A SER PINTADA:' ))


# cálculo para latas exigido e valor de custo utilizando latas de 18 litros
litros_necess á rios  =  metragem  /  6

latas  = ( litros_necess á rios  //  18 )

if  litros_necess á rios  %  18  ==  0 :
    latas  =  latas
mais :
    latas  =  latas  +  1
valor  =  latas  *  80

imprimir ( f '' '
ORÇAMENTO PARA LATAS DE 10L
METRAGEM: { metragem } mt²
LITROS NECESSÁRIOS: { litros_necess á rios : .2f } litros
LATAS: { int ( latas ) } un
VALOR TOTAL: R $ { valor : .2f }
'' ' )



# cálculo para latas exigido e valor de custo utilizando latas de 3.6 litros
litros_necess á rios  =  metragem  /  6

galao  = ( litros_necess á rios  //  3.6 ) +  1

if  litros_necess á rios  %  3.6  ==  0 :
    galao  =  galao
    valor  =  galao  *  25
mais :
    galao  =  galao  +  1
    valor  =  galao  *  25
imprimir ( f '' '
ORÇAMENTO PARA LATAS DE 3.6L
METRAGEM: { metragem } mt²
LITROS NECESSÁRIOS: { litros_necess á rios : .2f } litros
LATAS: { int ( galao ) } un
VALOR TOTAL: R $ { valor : .2f }
'' ' )

# cálculo para latas requer e valor de custo utilizando latas mistas
latas_18  =  metragem  //  108
metragem_restante  =  metragem % 108
galao_3_6  =  metragem_restante  //  21.6
se  metragem_restante  %  21.6  ! =  0 :
    galao_3_6  =  galao_3_6  +  1



imprimir ( f '' '
METRAGEM: { metragem } mt²
QUANTIDADE DE LATAS DE 18L: { latas_18 } un
QUANTIDADE DE LATAS DE 3.6L: { galao_3_6 } un
VALOR: { ( latas_18  *  80 ) + ( galao_3_6  *  25 ) }
'' ' )
