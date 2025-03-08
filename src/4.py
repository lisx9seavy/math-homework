import random

def get_random_code(n):
    # Generate n random numbers between 0 and 10
    numbers = [random.randint(0, 10) for i in range(n)]
    # Join the numbers into a string
    code = "".join(str(number) for number in numbers)
    return code