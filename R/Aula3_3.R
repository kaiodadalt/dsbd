require(nycflights13)

# Questao 1
flights %>%
  filter(arr_delay > 12*60 | dep_delay > 12*60) %>%
  inner_join(weather, by = c("year", "month", "day", "hour", "origin")) %>%
  group_by(month) %>%
  summarise(total_atrasos = n(),
            mean_temp = mean(temp, na.rm = TRUE),
            mean_dewp = mean(dewp, na.rm = TRUE),
            mean_humid = mean(humid, na.rm = TRUE),
            mean_wind_speed = mean(wind_speed, na.rm = TRUE),
            mean_precip = mean(precip, na.rm = TRUE)) %>%
  arrange(desc(total_atrasos))

# Questao 2
flights %>%
  group_by(dest) %>%
  summarise(total_voos = n()) %>%
  arrange(desc(total_voos)) %>%
  head(20) %>%
  inner_join(airports, by = c("dest" = "faa"))

# Questao 3
flights %>%
  inner_join(planes, by = "tailnum") %>%
  group_by(tailnum, carrier) %>%
  summarise(total_voos = n()) %>%
  arrange(desc(total_voos))

# Questao 4

