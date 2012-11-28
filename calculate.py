#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
"""вычисление синуса угла с точностью до сотого знака после запятой
методом разложения синуса в ряд Тейлора"""


#Calculate n!
def factorial(n):
    temp = 1
    for i in range(1, n + 1):
        temp *=i
    return temp

#Calculate n-th member of Taylor series
def Taylor(x, n):
    return (-1.0)**n * x**(2*n + 1)/factorial(2*n + 1)

epsilon = 10**-100

x = float(raw_input("Enter angle(in radians):"))
#x = math.pi/2 #pi/2
sum = Taylor(x, 0) + Taylor(x, 1)
prevSum = Taylor(x, 0)
n = 1

while (abs(sum - prevSum) > epsilon):
    prevSum = sum
    n +=1
    sum += Taylor(x, n)

approx = x - 1.0 * x**3/factorial(3) + 1.0 * x**5/factorial(5) - 1.0 * x**7/factorial(7)

print "Taylor: sin(" + str(x) + ")=" + str(sum);
print "Python: sin(" + str(x) + ")=" + str(math.sin(x));
print "Approx: sin(" + str(x) + ")=" + str(approx);




