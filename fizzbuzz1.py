# Iterate through the range of numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is a multiple of both 3 and 5
    if num % 15 == 0:
        print("FizzBuzz")
    # Check if the number is a multiple of 3 only
    elif num % 3 == 0:
        print("Fizz")
    # Check if the number is a multiple of 5 only
    elif num % 5 == 0:
        print("Buzz")
    # If the number is not a multiple of 3 or 5, print the number itself
    else:
        print(num)
