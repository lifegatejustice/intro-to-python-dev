

def wind_chill(temperature_fahrenheit, wind_speed):
    """
    Calculate wind chill based on temperature (Fahrenheit) and wind speed (mph).
    """
    if wind_speed < 3:
        return temperature_fahrenheit
    else:
        return 35.74 + (0.6215 * temperature_fahrenheit) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature_fahrenheit * (wind_speed ** 0.16)


def celsius_to_fahrenheit(celsius_temperature):
    """
    Convert Celsius temperature to Fahrenheit.
    """
    return (celsius_temperature * 9/5) + 32


def main():
    
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    
    if unit == 'C':
        temperature = celsius_to_fahrenheit(temperature)

 
    for wind_speed in range(5, 61, 5):
        windchill = wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature:.2f}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F")


if __name__ == "__main__":
    main()
