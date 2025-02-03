# Subtraction Program
def subtract_numbers(num1, num2):
    return num1 - num2

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Call the function and print the result
result = subtract_numbers(num1, num2)
print(f"The difference between {num1} and {num2} is {result}")
