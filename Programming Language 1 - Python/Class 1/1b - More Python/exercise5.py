"""
    *** EXERCISE 5 ***
    
    Escreva uma instrução que calcule a área de um círculo (use função pow())
"""

import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * math.pow(raio, 2)

print(f"A área do círculo com raio '{raio}' é '{area:.2f}'")
