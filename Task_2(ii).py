# Write a program to check if a string is a palindrome
string = input("Enter a string: ")
string_upper = string.upper() 
reverse_string = string_upper[::-1] 
if string_upper == reverse_string:
    print("True") 
else:
    print("False") 
