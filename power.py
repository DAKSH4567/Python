# Program to calculate the power of a number using loop

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1

for _ in range(abs(exponent)):
    result = base

# If exponent is negative, convert result to fraction
if exponent < 0:
    result = 1 / result

print(f"{base} raised to the power {exponent} is:", result)