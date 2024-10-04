import math
import random

radius = int(input("Please enter the radius of the sphere: "))

volume = 4/3 * math.pi * pow(radius, 3)

print(f"The volume of a sphere with radius of {radius} is {volume:.2f}")
print()

random_num = random.randint(1, 10)
factorial_num = math.factorial(random_num)

print(f"The factorial of {random_num} is {factorial_num}")