# Load necessary libraries
library(ggplot2)
library(dplyr)
library(readr)
library(forcats)
library(RColorBrewer)

# Load the cheese data
cheeses <- read_csv("cheeses.csv")

# A. Number of observations and variables
num_observations <- nrow(cheeses)
num_variables <- ncol(cheeses)

# Basic summary of the data
summary_cheeses <- summary(cheeses)

# Print summary information to the console
cat("Cheeses Data Summary\n")
cat("Number of observations:", num_observations, "\n")
cat("Number of variables:", num_variables, "\n")
cat("\nSummary statistics:\n")
print(summary_cheeses)

# B. Graphs to describe the data

# Aggregate countries with few observations into an "Other" category
country_counts <- cheeses %>%
  count(country) %>%
  arrange(desc(n))

# Define a threshold for the number of observations to retain a country
threshold <- 5

# Recode countries with few observations
cheeses <- cheeses %>%
  mutate(country = fct_lump_n(country, n = threshold))

# Reorder the countries based on frequency
cheeses <- cheeses %>%
  mutate(country = fct_infreq(country))

# Plot the distribution of 'milk' types across 'country'
p <- ggplot(cheeses, aes(x = country, fill = milk)) +
  geom_bar(position = "fill") +
  theme_minimal() +
  ggtitle("Distribution of Milk Types Across Countries") +
  xlab("Country") +
  ylab("Proportion") +
  theme(axis.text.y = element_text(size = 8),
        legend.title = element_text(size = 10),
        legend.text = element_text(size = 8),
        plot.title = element_text(hjust = 0.5)) +
  scale_fill_brewer(palette = "Paired") +
  coord_flip() # Flip coordinates for better readability

print(p)
