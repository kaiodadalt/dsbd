# Carregar bibliotecas necessárias
library(dplyr)
library(lubridate)

# Supondo que o dataset car_crash esteja em um arquivo CSV
car_crash <- read.csv("car_crash.csv")

car_crash %>%
  mutate(data = dmy(data)) %>%
  mutate(ano = year(data),
         mes = month(data)) %>%
  select(data, ano, mes, mortos) %>%
  filter(mortos > 0) %>%
  group_by(mes) %>%
  summarise(total_mortos = sum(mortos)) %>%
  arrange(desc(total_mortos))
