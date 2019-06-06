'''Решить несколько задач из projecteuler.net

Ваши решения должны быть максимально лаконичными - используйте list comprehensions, reduce, etc.

problem9 - list comprehension : one line
problem6 - list comprehension : one line
problem48 - list comprehension : one line
problem40 - list comprehension, reduce
'''
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

# print(number_letter_counts(1000))
# print(factorial_digit_sum(100))
# print(even_Fibonacci_numbers([0,1]))
'''

#problem6 - list comprehension : one line
#Find the difference between the sum of 
#the squares of the first one hundred natural numbers and the square of the sum.
def Sum_square_difference(n):
    return [(sum(x for x in range(1,n+1)))**2 - sum(x**2 for x in range(1,n+1))]


#problem9 - list comprehension : one line
#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
def Special_Pythagorean_triplet():
    return [[a,b,c] for c in range(0,1000) for b in range(0,c) for a in range(0,b) if a+b+c==1000 and a**2+b**2==c**2]

#problem40 - list comprehension, reduce
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
from functools import reduce
def Champernowne_constant():
    return reduce((lambda a, x: a*x), [int((''.join([str(i) 
        for i in range(1,500000)]))[i-1]) for i in [1,10,100,1000,10000,100000,1000000]])
    
#problem48 - list comprehension : one line
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
def Self_powers():
    return sum(x**x for x in range(1,1001))%(10**10)

print(Sum_square_difference(100))
print(Special_Pythagorean_triplet())
print(Champernowne_constant())
print(Self_powers())
