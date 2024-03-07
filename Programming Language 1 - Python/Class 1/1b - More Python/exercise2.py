"""
    *** EXERCISE 2 ***
    
    Escreva uma instrução que calcule a raiz cúbica de uma variável "x".
"""

import math

x = float(input("Digite o valor de x para calcular sua raiz cúbica: "))

raiz_cubica = math.pow(x, 1/3)

print(f"A raiz cúbica de {x} é: {raiz_cubica}")

