"""
    *** EXERCISE 1 ***

    Refaça o exercício da fórmula de Bhaskara da seguinte forma:
    
    a. Com quatro raízes de saída (x1_0 e x2_0, com o resultado real, e x1_1 e x2_1 com resultado arredondado para baixo);
    b. Use funções do módulo math, sempre que possível;
    c. Calcule o erro resultante do arredondamento.
"""

import math


def calcular_raizes(a, b, c):
    """
        Calcula as raízes reais de uma equação do segundo grau usando a fórmula de Bhaskara.

        Retorna:
        tuple: as raízes reais e arredondadas para baixo, além do erro de arredondamento.
    """
    discriminante = b ** 2 - 4 * a * c
    sqrt_discriminante = math.sqrt(discriminante)

    raiz_1 = (-b + sqrt_discriminante) / (2 * a)
    raiz_2 = (-b - sqrt_discriminante) / (2 * a)

    # Raízes arredondadas para baixo
    raiz_1_rounded = math.floor(raiz_1)
    raiz_2_rounded = math.floor(raiz_2)

    # Cálculo do erro resultante do arredondamento
    erro_1 = raiz_1 - raiz_1_rounded
    erro_2 = raiz_2 - raiz_2_rounded

    return raiz_1, raiz_2, raiz_1_rounded, raiz_2_rounded, erro_1, erro_2


def main():
    # Coletando os coeficientes da equação do usuário
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    (
        raiz_1,
        raiz_2,
        raiz_1_rounded,
        raiz_2_rounded,
        erro_1,
        erro_2
    ) = calcular_raizes(a, b, c)

    print(f"Raízes reais: x1 = {raiz_1}, x2 = {raiz_2}")
    print(f"Raízes arredondadas para baixo: x1 = {raiz_1_rounded}, x2 = {raiz_2_rounded}")
    print(f"Erro de arredondamento: x1 = {erro_1}, x2 = {erro_2}")


if __name__ == "__main__":
    main()
