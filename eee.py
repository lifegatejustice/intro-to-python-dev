file_name = "life-expectancy.csv"

# Function to load the data from the CSV file
def load_data(file_name):
    data = []
    with open(file_name, 'r') as lifeexpectancies:
        next(lifeexpectancies)  # Skip the header row
        for line in lifeexpectancies:
            # Split each line into parts and append to the data list
            parts = line.strip().split(',')
            data.append(parts)
    return data

# Load the data from the CSV file
data = load_data(file_name)


lowestlifeexpectancie = float('inf')
highestlifeexpectancy = float(-1)
lowestlifeexpectanciecountry = ''
highestlifeexpectancycountry = ''

# Initialize variables for calculating average life expectancy for a specific year
total_life_expectancy = 0
num_countries = 0

# Initialize a dictionary to store life expectancies by year
countrylifeexpect = {}

# Iterate through the data to find overall minimum and maximum life expectancies,
# and calculate total life expectancy for each year
for entry in data:
    country = entry[0]
    year = int(entry[2])
    lifeexpectancie = float(entry[3])

    # Update overall minimum and maximum life expectancies and corresponding countries
    if lifeexpectancie < lowestlifeexpectancie:
        lowestlifeexpectancie = lifeexpectancie
        lowestlifeexpectanciecountry = country
        lowestlifeexpectancieyear = year
    if lifeexpectancie > highestlifeexpectancy:
        highestlifeexpectancy = lifeexpectancie
        highestlifeexpectancycountry = country
        highestlifeexpectancyyear = year

    # Update total life expectancy for the specific year
    total_life_expectancy += lifeexpectancie
    num_countries += 1

    ques = int(input("Enter the year of interest: "))

    # Update life expectancies by year
    if year == ques:
        if country not in countrylifeexpect:
            countrylifeexpect[country] = []
        countrylifeexpect[country].append(lifeexpectancie)

    if country in countrylifeexpect:
        previousexpect = countrylifeexpect[country][-1]
        countrydrop = previousexpect - lifeexpectancie
        if countrydrop > largesstdrop:
            largesstdrop = countrydrop
            largesdropyear = year

    if country not in countrylifeexpect:
        countrylifeexpect[country] = []
        countrylifeexpect[country].append(lifeexpectancie)

    if year == ques:
        if countrylifeexpect and len(countrylifeexpect[country]) > 1:
            previousexpect = countrylifeexpect[country][-2]
            drop = previousexpect - lifeexpectancie
            if drop > largestdropcountry:
                largestdropcountry = country
                largestdropyear = year


if largesstdrop != 0:
    print(f'Largest drop from one year to the next: {largesstdrop} in {largestdropcountry}, {largesdropyear}')
else:
    print('No significant drop found.')


if ques in countrylifeexpect:
    totallifeexpect = sum(countrylifeexpect[ques])
    nocountries = len(countrylifeexpect[ques])
    averagelifeexpect = totallifeexpect / nocountries
    maxlifeexpect = max(countrylifeexpect[ques])
    minlifeexpect = min(countrylifeexpect[ques])
    countrymax = max(countrylifeexpect[ques], key=countrylifeexpect[ques].get)
    countrymin = min(countrylifeexpect[ques], key=countrylifeexpect[ques].get)
    print(f'For the year {ques}:')
    print(f'The average life expectancy across all countries was {averagelifeexpect:.2f}')
    print(f'The max life expectancy was in {countrymax} with {maxlifeexpect:.2f}')
    print(f'The min life expectancy was in {countrymin} with {minlifeexpect:.3f}')
else:
    print(f'For the year {ques}:')
    print('No significant drop found.')



# countryaverage = {country: sum(expectancies) / len(expectancies) for country, expectancies in countrylifeexpect.items()}
       
print(f'The overall max life expectancy is: {highestlifeexpectancy} from {highestlifeexpectancycountry} in {highestlifeexpectancyyear}')              
print(f'The overall min life expectancy is:  {lowestlifeexpectancie} from {lowestlifeexpectanciecountry} in {lowestlifeexpectancieyear}')
