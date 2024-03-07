"""
    *** EXERCISE 1 ***
    
    Defina a variável "nome" e atribua a ela o nome de uma pessoa.
    Depois imprima o nome da pessoa no lugar de 'fulano' na mensagem:

    a. "Oi fulano, vamos aprender Python?"
    b. Imprima a mensagem em maiúsculo.
"""

nome = input("Digite seu nome: ")
mensagem = f"Oi {nome}, vamos aprender Python?"

print(mensagem)
print(mensagem.upper())
