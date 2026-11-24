# Factorial Calculator
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    print(f"{number}! = {factorial}")
