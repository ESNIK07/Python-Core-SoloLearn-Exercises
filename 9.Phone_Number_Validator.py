""" 
Phone Number Validator


You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid
You can use a reg
"""
import re
#your code goes here
num = input()
pattern = r"[1|8|9]\d\d\d\d\d\d\d$"
if re.match(pattern,num):
    print("Valid")
else:
    print("Invalid")