# # 4.6 - Working with Strings and Numbers
# # Solution to review exercise
#
# # Exercise 1
# # Store an integer as a string
# my_integer_string = "6"
#
# # Convert the 'integer' string into an int object using int()
# # Multiply the integer by 7 and display the result
# print(int(my_integer_string) * 7)
#
# # Exercise 2
# # Store a floating-point number as a string
# my_float_string = "6.01"
#
# # Convert the 'float' string into a number using float()
# # Multiply the number by 7 and display the result
# print(float(my_float_string) * 7)

# Exercise 3
# Get two numbers from the user, multiply them,
# and display the result
a = input("Enter a number: ")
b = input("Enter another number: ")
product = float(a) + float(b)
print("The product of " + a + " and " + b + " is " + str(product) + ".")
