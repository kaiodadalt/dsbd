"""
    *** EXERCISE 2 ***
    
    Escreva um programa que solicita o raio de um círculo, e exibe o perímetro e a área desse círculo.
    Para calcular a área, utilize o operador de exponenciação **.
"""

import math


def calcular_area(raio):
    return math.pi * (raio ** 2)


def calcular_perimetro(raio):
    return 2 * math.pi * raio


def main():
    try:
        # Solicita ao usuário o raio do círculo
        raio = float(input("Digite o raio do círculo: "))

        # Calcula a área e o perímetro
        area = calcular_area(raio)
        perimetro = calcular_perimetro(raio)

        # Exibe os resultados
        print(f"A área do círculo é: {area:.2f}")
        print(f"O perímetro do círculo é: {perimetro:.2f}")

    except ValueError:
        print("Por favor, digite um número válido para o raio.")


if __name__ == "__main__":
    main()
