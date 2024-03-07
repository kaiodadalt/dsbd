"""
    *** EXERCISE 1 ***
    
    Faça um programa que pergunta o peso (em kg) e a altura (em metros) do usuário. 
    O programa deve calcular o Índice de Massa Corpórea (IMC) do usuário,
    dado por peso / (altura * altura) e exibir o valor de IMC na tela.

    Dica: use float para ler o input. Para separar as casas decimais quando estiver 
    digitando, utilize ponto (e.g., digite 1.8 para uma altura de 1). 
    Isso pode ser diferente em alguns sistemas. Por exemplo, alguns terminais de 
    sistema Mac utilizam vírgula para separar as casas decimais.
"""


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def main():
    try:
        # Solicita ao usuário seu peso e altura, utilizando ponto para casas decimais
        peso = float(input("Digite seu peso em kg (exemplo: 70.5): "))
        altura = float(input("Digite sua altura em metros (exemplo: 1.75): "))

        # Calcula o IMC
        imc = calcular_imc(peso, altura)

        # Exibe o resultado
        print(f"Seu Índice de Massa Corpórea (IMC) é: {imc:.2f}")

    except ValueError:
        print("Por favor, digite um número válido. Utilize ponto para separar as casas decimais.")


if __name__ == "__main__":
    main()
