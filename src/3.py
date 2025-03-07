def get_random_number(low, high):
    return randint(low, high)

def calculate_area(shape):
    if shape == "rectangle":
        width = get_random_number(1, 10)
        height = get_random_number(1, 10)
        return width * height
    elif shape == "circle":
        radius = get_random_number(1, 10)
        return pi * radius ** 2
    else:
        return None

def main():
    shape = input("Enter the shape of the area you want to calculate (rectangle/circle): ")
    if shape == "rectangle" or shape == "circle":
        print(calculate_area(shape))
    else:
        print("Invalid shape")

if __name__ == "__main__":
    main()
