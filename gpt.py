# Define variables to hold the lowest and highest life expectancy values
lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')

# Define variables to hold the largest drop from one year to the next
largest_drop = 0
largest_drop_country = ''
largest_drop_year = 0

# Define variables to hold life expectancy data for each country
country_life_expectancies = {}

# Read the life expectancy data from a file (assuming the file is named 'life_expectancy_data.txt')
with open('life_expectancy_data.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into parts
        parts = line.strip().split(',')

        # Extract the year, country, and life expectancy from the parts
        year = int(parts[0])
        country = parts[1]
        life_expectancy = float(parts[2])

        # Update the lowest and highest life expectancy values
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

        # Update the largest drop from one year to the next
        if country in country_life_expectancies:
            prev_year_expectancy = country_life_expectancies[country][-1]
            drop = prev_year_expectancy - life_expectancy
            if drop > largest_drop:
                largest_drop = drop
                largest_drop_country = country
                largest_drop_year = year

        # Update the life expectancy data for the country
        if country not in country_life_expectancies:
            country_life_expectancies[country] = []
        country_life_expectancies[country].append(life_expectancy)

# Calculate the average life expectancy for each country
country_averages = {country: sum(expectancies) / len(expectancies) for country, expectancies in country_life_expectancies.items()}

# Display the lowest and highest life expectancy values
print(f"Lowest life expectancy: {lowest_life_expectancy}")
print(f"Highest life expectancy: {highest_life_expectancy}")

# Display the country and year with the largest drop from one year to the next
print(f"Largest drop from one year to the next: {largest_drop} in {largest_drop_country}, {largest_drop_year}")

# Allow the user to type in a country and show the minimum, maximum, and average life expectancy for that country
user_country = input("Enter a country: ")
if user_country in country_life_expectancies:
    min_expectancy = min(country_life_expectancies[user_country])
    max_expectancy = max(country_life_expectancies[user_country])
    avg_expectancy = country_averages[user_country]
    print(f"For {user_country}:")
    print(f"Minimum life expectancy: {min_expectancy}")
    print(f"Maximum life expectancy: {max_expectancy}")
    print(f"Average life expectancy: {avg_expectancy}")
else:
    print("Country not found in the dataset")

# Look for interesting anomalies or patterns in the data
# You can analyze trends, fluctuations, or any unusual patterns in the life expectancy data
# This could involve plotting graphs, calculating statistics, etc.
