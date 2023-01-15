""" 
FizzBuzz is a well known programming assignment, asked during interviews.

The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn".

You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.
"""
n = int(input())
for i in range(1,n):
    if i % 2 == 0:
        continue
    elif i % 3 == 0 and i % 5 ==0:
        print("SoloLearn")
    elif i % 3 == 0:
        print("Solo")
    elif i % 5 == 0:
        print("Learn")
    else:
        print(i)