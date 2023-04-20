# Task: display the total population count for the next 3 years
# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

current_population = 380123456
year_in_seconds = 60 * 60 * 24 * 365
print(year_in_seconds/40)

# Add people which are born throughout the year
# As year_in_seconds is dividable through 6 there is no need to add rest to next year
born_person_per_year = year_in_seconds / 6
# Substract people which die throughout the year
# As year_in_seconds is dividable through 12 there is no need to add rest to next year
dead_persons_per_year = year_in_seconds / 12
# Add people which immigrated throughout the year
# As year_in_seconds is dividable through 40 there is no need to add rest to next year
immigrated_person_per_year = year_in_seconds / 40
# Estimate the total growth
growth_per_year = born_person_per_year + immigrated_person_per_year - dead_persons_per_year

#Results
population_1styear = current_population + growth_per_year
population_2ndyear = current_population + 2 * growth_per_year
population_3rdyear = current_population + 3 * growth_per_year

print("1st Year: " + str(population_1styear) + "; 2nd Year: " + str(population_2ndyear) + "; 3rd year: " + str(population_3rdyear))