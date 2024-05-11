"""
    *** EXERCISE 2 ***
    
    Imprima a citação a seguir em uma linha e seu autor na linha seguinte, 
    deslocados três tabs à direita:
    
    "No Brasil, quando o feriado é religioso, até ateu comemora", Jô Soares
"""

# Imprimindo a citação e o autor com deslocamento de três tabs
# impressão símples
# print("\t\t\t\"No Brasil, quando o feriado é religioso, até ateu comemora\"")
# print("\t\t\tJô Soares")

# impressão com format()
tabs = "\t\t\t{}"
citacao = '"No Brasil, quando o feriado é religioso, até ateu comemora"'
autor = "Jô Soares"
print(tabs.format(citacao))
print(tabs.format(autor))
