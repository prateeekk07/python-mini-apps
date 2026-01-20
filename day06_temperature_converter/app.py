def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


print("🌡️ Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {result:.2f}°F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {result:.2f}°C")
else:
    print("Invalid choice ❌")