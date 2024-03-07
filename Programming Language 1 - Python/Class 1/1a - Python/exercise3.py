"""
    *** EXERCISE 3 ***
    
    Faça um programa que leia os coeficientes a, b e c de uma equação de segundo grau. 
    O programa deve calcular por Bhaskara as raízes dessa equação. Para esse problema, 
    assuma que a equação sempre vai ter raízes reais (o usuário não vai digitar 
    valores a, b e c que levam a uma equação que não possui raízes). 
    Caso a equação possua apenas uma raiz, como a equação x2, repita a raiz na resposta duas vezes.

    Exemplo de execução do programa:
    
    Digite a: 2
    Digite b: 0
    Digite c: 0
    Raiz 1: 0
    Raiz 2: 0
"""

import math


def calcular_raizes(a, b, c):
    """
    Calcula as raízes de uma equação do segundo grau usando a fórmula de Bhaskara.

    Retorna:
    tuple: as duas raízes da equação.
    """
    # Calcula o discriminante
    discriminante = b ** 2 - 4 * a * c

    # Calcula as raízes
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)

    return raiz1, raiz2


def main():
    try:
        # Solicita ao usuário os coeficientes a, b e c da equação do segundo grau
        a = float(input("Digite a: "))
        b = float(input("Digite b: "))
        c = float(input("Digite c: "))

        # Verifica se a é diferente de zero para ser uma equação do segundo grau
        if a == 0:
            print("O coeficiente 'a' deve ser diferente de zero para uma equação do segundo grau.")
        else:
            # Calcula as raízes da equação
            raiz1, raiz2 = calcular_raizes(a, b, c)

            # Exibe os resultados
            print(f"Raiz 1: {raiz1}")
            print(f"Raiz 2: {raiz2}")

    except ValueError:
        print("Por favor, digite números válidos para os coeficientes.")


if __name__ == "__main__":
    main()
