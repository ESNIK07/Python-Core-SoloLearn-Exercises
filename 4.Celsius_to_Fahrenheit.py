""" 
You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

Sample Input
36

Sample Output
96.8
"""
def converter(celsius):
    output = 9 / 5 * celsius + 32
    return output

celsius = int(input())
temp_fahrenheit = converter(celsius)
print(temp_fahrenheit)


