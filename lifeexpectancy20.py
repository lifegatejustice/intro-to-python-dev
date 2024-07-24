with open('life-expectancy.csv') as lifeexpectancies:
    #i had a very though time in next line of code😪.
    #it is meant to skip the header in the csv file.
    next(lifeexpectancies)

    
    ques = int(input('Enter the year of interest: '))

    lowestlifeexpectancie = float(9999999999999)
    highestlifeexpectancy = float(-1)

    largesstdrop = 0
    largestdropcountry = ''
    largesdropyear = 0

    countrylifeexpect = {}
    for line in lifeexpectancies:
        parts = line.strip().split(',')

        year = int(parts[2])
        country = parts[0]
        lifeexpectancie = float(parts[3])


        if lifeexpectancie < lowestlifeexpectancie:
              lowestlifeexpectancie = lifeexpectancie
              lowestlifeexpectanciecountry = country 
              lowestlifeexpectancieyear = year 

        if lifeexpectancie > highestlifeexpectancy:
              highestlifeexpectancy = lifeexpectancie
              highestlifeexpectanciecountry = country 
              highestlifeexpectancieyear = year


        if country in countrylifeexpect:
              previousexpect = countrylifeexpect[country][-1]
              countrydrop = previousexpect - lifeexpectancie
              if countrydrop > largesstdrop:
                    largesstdrop = countrydrop
                    largesdropyear = year

        if country not in countrylifeexpect:
                          countrylifeexpect[country] = []
                          countrylifeexpect[country].append(lifeexpectancie)
        else:
              countrylifeexpect[country] = [lifeexpectancie]

countryaverage = {country: sum(expectancies) / len(expectancies) for country, expectancies in countrylifeexpect.items()}

# yearofinterest = ques
# totallifeexpectancy = 0
# nocountries = 0
# mmaxlifeexpectancy = float(-1)
# minlifeexpectancy = float(9999999999)

# if yearofinterest in countrylifeexpect:
#         for expectancy in countrylifeexpect[yearofinterest]:
#             totallifeexpectancy += expectancy
#             nocountries += 1

#             if expectancy > maxlifeexpectancy:
#                 maxlifeexpectancy = expectancy

#             if expectancy < minlifeexpectancy:
#                 minlifeexpectancy = expectancy

#         averagelifeexpectancy = totallifeexpectancy / nocountries

# for line in lifeexpectancies:
#     parts = line.strip().split(',')
#     country = parts[0]
#     lifeexpectancie = float(parts[3])

#     if int(parts[2]) == yearofinterest:
#         totallifeexpectancy += lifeexpectancie
#         nocountries += 1

#         if lifeexpectancie > mmaxlifeexpectancy:
#             mmaxlifeexpectancy = lifeexpectancie
#             countrymax = country

#         if lifeexpectancie < minlifeexpectancy:
#               minlifeexpectancy = lifeexpectancie
#               countrymin = country

# averagelifeexpectancie = totallifeexpectancy / nocountries

print(f"The overall max life expectancy is: {highestlifeexpectancy} from {highestlifeexpectanciecountry} in {highestlifeexpectancieyear}")              
print(f"The overall min life expectancy is:  {lowestlifeexpectancie} from {lowestlifeexpectanciecountry} in {lowestlifeexpectancieyear}")
# print(f"For the year {yearofinterest}:")
# print(f"The average life expectancy across all countries was {averagelifeexpectancie:.2f}")
# print(f"The max life expectancy was in {countrymax} with {mmaxlifeexpectancy:.2f}")
# print(f"The min life expectancy was in {countrymin} with {minlifeexpectancy:.3f}")



# print(f"Largest drop from one year to the next: {largesstdrop} in {countrydrop}, {largesdropyear}")


    



