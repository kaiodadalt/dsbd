
library(dplyr)
data("starwars")

# 1. Número total de espécies únicas presentes
num_especies_unicas <- starwars %>%
  filter(!is.na(species)) %>%
  distinct(species) %>%
  count()
print(num_especies_unicas)

# Frequência de indivíduos por espécie
freq_individuos_especie <- starwars %>%
  filter(!is.na(species)) %>%
  count(species, sort = TRUE)
print(freq_individuos_especie)

# 2. Altura média de personagens masculinos e femininos
altura_media_genero <- starwars %>%
  filter(!is.na(height), !is.na(gender)) %>%
  group_by(gender) %>%
  summarise(altura_media = mean(height, na.rm = TRUE))
print(altura_media_genero)

# 3. Peso médio dos personagens de cada espécie para personagens masculinos
peso_medio_masculino_especie <- starwars %>%
  filter(!is.na(mass), gender == "male", !is.na(species)) %>%
  group_by(species) %>%
  summarise(peso_medio = mean(mass, na.rm = TRUE))
print(peso_medio_masculino_especie)

# 4. Personagem mais pesado de cada espécie e seu peso correspondente
personagem_mais_pesado_especie <- starwars %>%
  filter(!is.na(mass), !is.na(species)) %>%
  group_by(species) %>%
  summarise(personagem_mais_pesado = name[which.max(mass)],
            peso_maximo = max(mass, na.rm = TRUE))
print(personagem_mais_pesado_especie)

