#EX1-------------------------------------------------------
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
print("Hello,", name, surname + "!")
print("You are", name, surname + ",", "and you are", age, "years old.")

#EX2----------------------------------------------
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)

#EX3---------------------------------------------------------------------------------
work_in_class = float(input("Enter your score for work in class: "))
test = float(input("Enter your score for test: "))
project = float(input("Enter your score for project: "))
total_score = (work_in_class * 0.2) + (test * 0.3) + (project * 0.5)
if total_score >= 90:
    grade = "5"
elif total_score >= 80:
    grade = "4.5"
elif total_score >= 70:
    grade = "4"
elif total_score >= 60:
    grade = "3.5"
elif total_score >= 50:
    grade = "3"
else:
    grade = "2"
print("Your grade is:", grade)

#EX4 ---------------------------------
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# First input
number1 = int(input("Enter the first number: "))
result1 = check_even_odd(number1)
print("The first number is:", result1)

# Second input
number2 = int(input("Enter the second number: "))
result2 = check_even_odd(number2)
print("The second number is:", result2)

#EX5---------------------------------------
# Prompt the user to enter values of different types
var_int = int(input("Enter an integer value: "))
var_float = float(input("Enter a float value: "))
var_str = input("Enter a string value: ")
var_bool = input("Enter a boolean value (True or False): ").lower() == "true"

# Determine the type of each variable
type_int = type(var_int).__name__
type_float = type(var_float).__name__
type_str = type(var_str).__name__
type_bool = type(var_bool).__name__

# Print the type of each variable
print("Type of var_int:", type_int)
print("Type of var_float:", type_float)
print("Type of var_str:", type_str)
print("Type of var_bool:", type_bool)

#EX6________________________-
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if a triangle can be formed
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # Check the type of triangle
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    # Print the type of triangle
    print("The triangle is:", triangle_type)
else:
    print("These side lengths cannot form a triangle.")

#EX7_______________________________________
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check if the second number is zero
    if num2 == 0:
        result = "Error! Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

# Print the result
print("Result:", result)