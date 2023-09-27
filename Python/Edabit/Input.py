# # 4.4 Interact With user Input
# # Solutions to review exercise
#
# # Exercise 1
# # Take input from the user and display that input back
# my_input = input("Type something: ")
# print(my_input)
#
# # Exercise 2
# # Display the input string converted to lower-case letters
# print(my_input.lower())
#
# # Exercise 3
# # Take user input and display the number of input characters.
# input_string = input("Type something: ")
# print(len(input_string))
#
# # Exercise 4
# # Return the upper-case first letter entered by the user

user_input = input("Tell me your password: ")
first_letter = user_input[0]
print("The first letter you entered was: " + first_letter.upper())