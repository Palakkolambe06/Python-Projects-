# Prime Number Checker
# A prime number has exactly two factors: 1 and itself.

number = int(input("Enter a whole number: "))

if number <= 1:
    print(number, "is not a prime number.")
else:
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
