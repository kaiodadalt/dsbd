# Definição da função
f <- function(x) {
  log(cos(x))
}

# Ponto onde vamos avaliar a derivada
x <- 5

# Tamanho do passo
h <- 0.01

# Derivada numérica usando a fórmula de diferença finita progressiva
derivada_numerica <- (f(x + h) - f(x)) / h

# Exibindo o resultado
print(round(derivada_numerica, 3))
