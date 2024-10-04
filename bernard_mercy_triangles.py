#Name: Mercy Bernard
#Program description:This is an algorithm to calculate the area and perimeter of a triangle using the user entered side lengths
#and also determine the type of triangle.
#The math module was imported to allow mathematical calculations, variables were used to store values for calculations,
#then the if/else block to determine the type of triangle based on the Pythagorean Theorem.

import math

#Set variables to store values from user input and format to integer.
a = int(input("Please enter the length of side A of the triangle (in meters): "))
b = int(input("Please enter the length of side B of the triangle (in meters): "))
c = int(input("Please enter the length of side C of the triangle (in meters): "))

#Calculate the perimeter of the triangle using the user inputs
perimeter = a + b + c

#Using the Heron's formula to calculate the area of a triangle
s = 1/2 * perimeter #Calculate the semi-perimeter

x = s * (s - a) * (s - b) * (s -c) #Store a part of the calculation for area in a variable x

area = math.sqrt(x) #The square root of x gives the area of the triangle

#Output the perimeter and area of the triangle
print(f"The perimeter of the triangle is {perimeter}m")
print(f"The area of the triangle is {area:.2f}m^2")

#Create a conditional block to determine the type of triangle
#Using the Pythagorean Theorem

if (a^2) + (b^2) == c^2:
    print("It is a Right Triangle.")

elif (a^2) + (b^2) > c^2:
    print("It is an Acute Triangle.")

elif (a^2) + (b^2) < c^2:
    print("It is an Obtuse Triangle.")