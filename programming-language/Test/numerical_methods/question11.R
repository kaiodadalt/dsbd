# Função que define o sistema de equações e sua matriz jacobiana
equations <- function(vars) {
  x <- vars[1]
  y <- vars[2]
  
  f <- c(
    x^3 + y - 1,
    y^3 - x + 1
  )
  
  J <- matrix(0, nrow = 2, ncol = 2)
  J[1, 1] <- 3 * x^2
  J[1, 2] <- 1
  J[2, 1] <- -1
  J[2, 2] <- 3 * y^2
  
  list("f" = f, "J" = J)
}

# Função que implementa o método de Newton
newton_method <- function(equations, x0, epsilon = 0.0001, max_iter = 1000) {
  x <- x0
  for (i in 1:max_iter) {
    result <- equations(x)
    f <- result$f
    J <- result$J
    delta <- solve(J, -f)
    x <- x + delta
    if (max(abs(delta)) < epsilon) {
      break
    }
  }
  return(x)
}

# Valor inicial
x0 <- c(1, 1)

# Chamar o método de Newton
solution <- newton_method(equations, x0)

# Exibir a solução
print(solution)
