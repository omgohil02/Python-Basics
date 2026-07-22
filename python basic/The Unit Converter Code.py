#Unit converter in Python

print("Fahrenheit to Celsius Converter")

# We wrap it in float() because input() always reads text, and we need a number.
fahrenheit = float(input("Enter temperature in Fahrenheit: ")) 

# 2. Do the math
celsius = (fahrenheit - 32) * 5 / 9  #formula to convert fahrenheit to celsius

# 3. Print the result. 
# We use round() to keep it to 2 decimal places.
print(f"{fahrenheit}°F is equal to {round(celsius, 2)}°C")

