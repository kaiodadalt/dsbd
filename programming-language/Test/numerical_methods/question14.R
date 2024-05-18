# Definindo o valor de mu
mu <- -0.041

# Fixando a semente para reproduzibilidade
set.seed(123)

# Número de pontos de integração
n <- 1050

# Gerar n pontos aleatórios seguindo uma distribuição uniforme
x <- runif(n, min = -10, max = 10)  # Usando intervalo amplo o suficiente para cobrir praticamente todos os valores possíveis

# Avaliar a função em cada ponto
f_x <- 0.5 * exp(-abs(x - mu))

# Calcular a estimativa da integral
integral <- mean(f_x) * 20  # Multiplicando pela largura total do intervalo [-10, 10]

# Resultado
print(integral)
