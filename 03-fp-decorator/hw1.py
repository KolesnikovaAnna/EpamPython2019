'''Решить несколько задач из projecteuler.net

Ваши решения должны быть максимально лаконичными - используйте list comprehensions, reduce, etc.

problem9 - list comprehension : one line
problem6 - list comprehension : one line
problem48 - list comprehension : one line
problem40 - list comprehension, reduce
'''

#Problem 17 - Number letter counts
#If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?
import num2words
def number_letter_counts(num):
    return len(''.join([(num2words.num2words(i)).replace(' ','').replace('-','') for i in range(1,num+1)]))

#Problem 20 - Factorial digit sum
#Find the sum of the digits in the number 100!
#10! = 10×9×...×3×2×1 = 3628800,sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

import math
def factorial_digit_sum(num):
    return sum(map(int, str(math.factorial(num))))
    
#Problem 2 - Even Fibonacci numbers
#By considering the terms in the Fibonacci sequence 
#whose values do not exceed four million, find the sum of the even-valued terms.
from functools import reduce
def even_Fibonacci_numbers(fib):
    # a, b, total = 1, 1, 0
    # while a <= 4000000:
    #     if a % 2 == 0:
    #         total += a
    #     a, b = b, a+b 
    # print(total)
    
    [fib.append(fib[-1] +fib[-2]) for ctr in range(32)]
    return (reduce(lambda x,y: x+y, list((filter(lambda x : x % 2 == 0, fib)))))

print(number_letter_counts(1000))
print(factorial_digit_sum(100))
print(even_Fibonacci_numbers([0,1]))