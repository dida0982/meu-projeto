names = []
ages = []
heights = []

for i in range(3):
    name = input(f"Enter name {i+1}: ")
    age = int(input(f"Enter age {i+1}: "))
    height = float(input(f"Enter height {i+1}: "))

    names.append(name)
    ages.append(age)
    heights.append(height)

for i in range(3):
    print(f"People {i+1}: Name: {names[i]}, Age: {ages[i]}, Height: {heights[i]}")
