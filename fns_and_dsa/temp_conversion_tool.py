CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FAHRENHEIT_OFFSET = 32

def celsius_to_fahrenheit(c):
    return c * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET

def fahrenheit_to_celsius(f):
    return (f - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp:.1f}°F is {converted:.15f}°C")
        elif unit == "C":
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp:.1f}°C is {converted:.1f}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
