with open('life-expectancy.csv') as lifeexpectancies:
    next(lifeexpectancies)  # Skip header line
    
    year_of_interest = int(input('Enter the year of interest: '))
    
    lowest_life_expectancy = float('inf')
    highest_life_expectancy = float('-inf')
    largest_std_drop = 0
    largest_std_drop_country = ''
    largest_std_drop_year = 0
    
    country_life_expectancies = {}
    
    for line in lifeexpectancies:
        parts = line.strip().split(',')
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        
        # Update min and max life expectancies
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            lowest_life_country = country
            lowest_life_year = year
        
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            highest_life_country = country
            highest_life_year = year
        
        # Update largest std drop
        if country in country_life_expectancies:
            prev_expectancy = country_life_expectancies[country][-1]
            drop = prev_expectancy - life_expectancy
            if drop > largest_std_drop:
                largest_std_drop = drop
                largest_std_drop_country = country
                largest_std_drop_year = year
        
        country_life_expectancies.setdefault(country, []).append(life_expectancy)
    
    # Calculate statistics for the specified year
    if year_of_interest in country_life_expectancies:
        life_expectancies = country_life_expectancies[year_of_interest]
        total_expectancy = sum(life_expectancies)
        num_countries = len(life_expectancies)
        average_life_expectancy = total_expectancy / num_countries
        max_life_expectancy = max(life_expectancies)
        min_life_expectancy = min(life_expectancies)
        
        print(f"For the year {}:")
        print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
        print(f"The max life expectancy was in {highest_life_country} with {max_life_expectancy:.2f}")
        print(f"The min life expectancy was in {lowest_life_country} with {min_life_expectancy:.3f}")
    