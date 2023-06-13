#!/usr/bin/python3
'''
Author: Ismail
'''
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10) * (-1 if number < 0 else 1)
print(
    f'Last digit of {number} is {last_digit} and',
    'is 0' if last_digit == 0 else 'is greater than 5'
    if last_digit > 5 else 'is less than 6 and not 0')
'''
last_digit = int(str(number)[-1]) * (-1 if number < 0 else 1)
last_digit = number % 10 if number >= 0 else ((number * -1) % 10) * -1
message = f'Last digit of {number} is {last_digit} and '
if last_digit == 0:
    message += 'is 0'
elif last_digit > 5:
    message += 'is greater than 5'
else:
    message += 'is less than 6 and not 0'
'''
