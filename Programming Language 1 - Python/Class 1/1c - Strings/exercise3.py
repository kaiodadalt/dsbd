"""
    *** EXERCISE 3 ***

    Imprima a mensagem "O resultado da fórmula de Bhaskara é" e o resultado

    a. Em seguida da mensagem
    b. Abaixo da mensagem
    c. Como uma string formatada com a, b, c, e as raízes, cada um em uma linha
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


def impressao_simples(**kwargs):
    # imprimindo o resultado na mesma linha da mensagem
    print(f"O resultado da fórmula de Bhaskara é: raiz1 = {kwargs['raiz_1']}, raiz2 = {kwargs['raiz_2']}")

    # imprimindo o resultado abaixo da mensagem
    print("O resultado da fórmula de Bhaskara é:")
    print(f"raiz1 = {kwargs['raiz_1']}, raiz2 = {kwargs['raiz_2']}")

    # imprimindo como uma string formatada com a, b, c, e as raízes, cada um em uma linha
    content = f"""
    O resultado da fórmula de Bhaskara para a equação com:
    a = {kwargs['a']}
    b = {kwargs['b']}
    c = {kwargs['c']}
    é:
    raiz1 = {kwargs['raiz_1']}
    raiz2 = {kwargs['raiz_2']}
    Raízes arredondadas para baixo: x1 = {kwargs['raiz_1_rounded']}, x2 = {kwargs['raiz_2_rounded']}
    Erro de arredondamento: x1 = {kwargs['erro_1']}, x2 = {kwargs['erro_2']}
    """
    print(content)


def impressao_format(**kwargs):
    # imprimindo o resultado na mesma linha da mensagem
    print("O resultado da fórmula de Bhaskara é: raiz1 = {raiz_1}, raiz2 = {raiz_2}"
          .format(raiz_1=kwargs['raiz_1'], raiz_2=kwargs['raiz_2']))

    # imprimindo o resultado abaixo da mensagem
    print("O resultado da fórmula de Bhaskara é:")
    print("raiz1 = {raiz_1}, raiz2 = {raiz_2}".format(raiz_1=kwargs['raiz_1'], raiz_2=kwargs['raiz_2']))

    # imprimindo como uma string formatada com a, b, c, e as raízes, cada um em uma linha
    content = """
    O resultado da fórmula de Bhaskara para a equação com:
    a = {a}
    b = {b}
    c = {c}
    é:
    raiz1 = {raiz_1}
    raiz2 = {raiz_2}
    Raízes arredondadas para baixo: x1 = {raiz_1_rounded}, x2 = {raiz_2_rounded}
    Erro de arredondamento: x1 = {erro_1}, x2 = {erro_2}
    """.format(
        a=kwargs['a'],
        b=kwargs['b'],
        c=kwargs['c'],
        raiz_1=kwargs['raiz_1'],
        raiz_2=kwargs['raiz_2'],
        raiz_1_rounded=kwargs['raiz_1_rounded'],
        raiz_2_rounded=kwargs['raiz_2_rounded'],
        erro_1=kwargs['erro_1'],
        erro_2=kwargs['erro_2']
    )
    print(content)


def main():
    # Coletando os coeficientes da equação do usuário
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    raiz_1, raiz_2, raiz_1_rounded, raiz_2_rounded, erro_1, erro_2 = calcular_raizes(a, b, c)

    # impressao_simples(
    #     a=a,
    #     b=b,
    #     c=c,
    #     raiz_1=raiz_1,
    #     raiz_2=raiz_2,
    #     raiz_1_rounded=raiz_1_rounded,
    #     raiz_2_rounded=raiz_2_rounded,
    #     erro_1=erro_1,
    #     erro_2=erro_2
    # )

    impressao_format(
        a=a,
        b=b,
        c=c,
        raiz_1=raiz_1,
        raiz_2=raiz_2,
        raiz_1_rounded=raiz_1_rounded,
        raiz_2_rounded=raiz_2_rounded,
        erro_1=erro_1,
        erro_2=erro_2
    )


if __name__ == "__main__":
    main()
