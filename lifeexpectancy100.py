


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

        if year == ques:
               if country not in countrylifeexpect:
                   countrylifeexpect[country] = []
        countrylifeexpect[country].append(lifeexpectancie)


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
        
        if year == ques:
               if countrylifeexpect and len(countrylifeexpect[country]) >1:
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
       
print(f'The overall max life expectancy is: {highestlifeexpectancy} from {highestlifeexpectanciecountry} in {highestlifeexpectancieyear}')              
print(f'The overall min life expectancy is:  {lowestlifeexpectancie} from {lowestlifeexpectanciecountry} in {lowestlifeexpectancieyear}')

