"""
    *** EXERCISE 4 ***
    
    Como saber se um número é par ou ímpar? Escreva uma instrução que resolva esse problema.
"""

numero = int(input("Digite um número para verificar se é par ou ímpar: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
