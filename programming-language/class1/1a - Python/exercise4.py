"""
    *** EXERCISE 4 ***

    Dado um retângulo de lado a=7 e área 63, escreva:
    a. Uma instrução em Python que calcule o valor do lado b.
    b. Uma instrução que calcule a diagonal deste retângulo.
    c. Uma função que calcule a área e a diagonal de qualquer retângulo, dados os valores dos lados a e b.
"""

import math


def calcular_area_diagonal(a, b):
    area = a * b
    diagonal = math.sqrt(a ** 2 + b ** 2)
    return area, diagonal


def main():
    # calcular o valor do lado b
    a = 7
    area = 63
    b = area / a

    # calcular a diagonal do retângulo
    diagonal = math.sqrt(a ** 2 + b ** 2)

    # calcular área e diagonal do retângulo
    area_calculada, diagonal_calculada = calcular_area_diagonal(a, b)

    print(f"Lado b: {b}")
    print(f"Diagonal: {diagonal:.3f}")
    print(f"Área calculada: {area_calculada}, Diagonal calculada: {diagonal_calculada:.3f}")


if __name__ == "__main__":
    main()
