"""
Temperature Conversion Program
A beginner-friendly console application that converts temperatures between
Celsius, Fahrenheit, and Kelvin units.

Author: Professional Software Developer
Date: January 30, 2026
"""

def celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
   
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
   
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
   
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


def get_temperature_input():
    while True:
        try:
            # Prompt user to enter temperature value
            temperature = float(input("Enter the temperature value: "))
            return temperature
        except ValueError:
            # Handle non-numeric input
            print("❌ Invalid input! Please enter a numeric value.\n")


def get_unit_input():
    while True:
        # Display unit selection menu
        print("\nSelect the temperature unit:")
        print("1. Celsius (C)")
        print("2. Fahrenheit (F)")
        print("3. Kelvin (K)")
        
        # Get user choice
        choice = input("Enter your choice (1/2/3 or C/F/K): ").strip().upper()
        
        # Map numeric choices to unit letters
        unit_map = {'1': 'C', '2': 'F', '3': 'K'}
        
        # Validate and return the unit
        if choice in unit_map:
            return unit_map[choice]
        elif choice in ['C', 'F', 'K']:
            return choice
        else:
            print("❌ Invalid choice! Please select 1, 2, 3, or C, F, K.\n")


def validate_temperature(temperature, unit):
    if unit == 'C' and temperature < -273.15:
        print(f"⚠️  Warning: {temperature}°C is below absolute zero (-273.15°C)!")
        return False
    elif unit == 'F' and temperature < -459.67:
        print(f"⚠️  Warning: {temperature}°F is below absolute zero (-459.67°F)!")
        return False
    elif unit == 'K' and temperature < 0:
        print(f"⚠️  Warning: {temperature}K is below absolute zero (0K)!")
        return False
    
    return True


def convert_temperature(temperature, unit):
    if not validate_temperature(temperature, unit):
        print("Please enter a valid temperature above absolute zero.\n")
        return
    
    print("\n" + "="*50)
    print("           CONVERSION RESULTS")
    print("="*50)
    
    if unit == 'C':
        # Convert from Celsius to Fahrenheit and Kelvin
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        
        print(f"Original Temperature:  {temperature:.2f}°C")
        print(f"Converted to Fahrenheit: {fahrenheit:.2f}°F")
        print(f"Converted to Kelvin:     {kelvin:.2f}K")
    
    elif unit == 'F':
        # Convert from Fahrenheit to Celsius and Kelvin
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        
        print(f"Original Temperature:  {temperature:.2f}°F")
        print(f"Converted to Celsius:    {celsius:.2f}°C")
        print(f"Converted to Kelvin:     {kelvin:.2f}K")
    
    elif unit == 'K':
        # Convert from Kelvin to Celsius and Fahrenheit
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        
        print(f"Original Temperature:  {temperature:.2f}K")
        print(f"Converted to Celsius:    {celsius:.2f}°C")
        print(f"Converted to Fahrenheit: {fahrenheit:.2f}°F")
    
    print("="*50 + "\n")


def main():
    # Display welcome message
    print("\n" + "="*50)
    print("   TEMPERATURE CONVERSION PROGRAM")
    print("="*50)
    print("Convert between Celsius, Fahrenheit, and Kelvin\n")
    
    # Main program loop
    while True:
        # Get temperature value from user
        temperature = get_temperature_input()
        
        # Get temperature unit from user
        unit = get_unit_input()
        
        # Perform conversion and display results
        convert_temperature(temperature, unit)
        
        # Ask if user wants to perform another conversion
        continue_choice = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        
        if continue_choice not in ['yes', 'y']:
            # Exit the program
            print("\n" + "="*50)
            print("Thank you for using the Temperature Converter!")
            print("="*50 + "\n")
            break
        else:
            print("\n")  # Add spacing for next conversion


# Entry point of the program
if __name__ == "__main__":
    main()
