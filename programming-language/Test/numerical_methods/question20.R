# Método de Newton modificado para aceitar um intervalo para a raiz
newton_method_interval <- function(y, interval, epsilon = 0.0001, max_iter = 1000) {
  a <- interval[1]
  b <- interval[2]
  mu <- (a + b) / 2  # Ponto inicial como o ponto médio do intervalo
  
  for (i in 1:max_iter) {
    mu_new <- mu - f(mu, y) / f_prime(mu, y)
    if (abs(mu_new - mu) < epsilon) {
      return(mu_new)
    }
    mu <- mu_new
    
    # Verifica se a raiz está dentro do intervalo
    if (mu < a || mu > b) {
      stop("O método de Newton saiu do intervalo de busca.")
    }
  }
  stop("O método de Newton não convergiu após ", max_iter, " iterações.")
}

# Valores de y
y <- c(4, 6, 5, 7, 7, 2, 5, 7, 5, 5)

# Escolhendo um intervalo para a raiz
interval <- c(-2, 3)

# Chamando o método de Newton modificado
raiz <- newton_method_interval(y, interval)

# Imprimindo o resultado
cat("A raiz à direita do ponto crítico é:", round(raiz, 3))

