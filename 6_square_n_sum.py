#SQUARE (N) SUM {sum of squares}
"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1^2 + 2^22 +2^2 = 9

ARRAYS LISTS FUNDAMENTALS"""
def square_sum(numbers):
    #your code here
    sum=0
    for i in numbers:
        sum += i*i 
    return sum
#OUTPUTS
"""
Time: 508ms Passed: 45Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (5 of 5 Assertions)
Completed in 0.09ms
Random Tests
Testing for square_sum([-7, 7, 2, -7, 18, -5, -13])
Testing for square_sum([2, -1, 20, -3, -4, -12, -3, 1, 16])
Testing for square_sum([17, -16, -20])
Testing for square_sum([-7, 0, -4, 2, 7, 16, 19, 15, -7, 9])
Testing for square_sum([11, 7, 1, 8])
Testing for square_sum([16, -17])
Testing for square_sum([-20, -8, -13, 3, -11, -16, -17, -3])
Testing for square_sum([-6, -4, -8, 14, -6])
Testing for square_sum([4, 6, -7, -6, -20, -15, 20, 10, -18])
Testing for square_sum([-8, -1, 14])
Testing for square_sum([-13, 19, -17, 8, -14, 8, -15])
Testing for square_sum([-20, -4, -9, 4, 2, 5, 3, -9, -16])
Testing for square_sum([-15, 1, 14, -2, -15, 13, -11, 10, -20, -16])
Testing for square_sum([10, 20, 5, 15, 13, -10, -17, 3, 1])
Testing for square_sum([-4, -11, -19, -13, 12, -17, -11, 19, 10])
Testing for square_sum([18, -10, -12, -1, 12])
Testing for square_sum([-11, -17, -3])
Testing for square_sum([8, 15, -5])
Testing for square_sum([18, -18, -19, 1, -5])
Testing for square_sum([-12, 9, -17, 5, 5, 6, -18])
Testing for square_sum([14, 9, -1, 10])
Testing for square_sum([19, 6, 16, -2])
Testing for square_sum([-7, -10, -7, -1, 0, -7, -14, -10, -1, 17])
Testing for square_sum([-3, 16, -5])
Testing for square_sum([-9, -13, 19, -16, 15, 13, 4, 6])
Testing for square_sum([-5, 1, 12, -1, 12, 14])
Testing for square_sum([10, 4, 20, -16, -3, 2, -17, 20])
Testing for square_sum([-6, 6, 9, 20, 9, 5, -18, 4, -3])
Testing for square_sum([13, 17, 14, 11, 1, -9, -4, -8, 17, 20])
Testing for square_sum([-15, 2])
Testing for square_sum([8, 8, -16, 3, -4, 8, 1, -4, -10])
Testing for square_sum([-8, 14, -6, 2, 2, 9, 19, -1, -6])
Testing for square_sum([-10, 2, -4, -20, -5, -7, -18, 0, -5])
Testing for square_sum([-15, -7, -5, 8, 17, 0, 10, -2])
Testing for square_sum([5, 19, 18, -15, -9, -13, 9, 1])
Testing for square_sum([-14, 6, -9, 12, -12, 0, -4, -9, 6])
Testing for square_sum([-10, -14, 18, -14, -14, -7])
Testing for square_sum([15, 12, -19, -4, -18, -18, 16, 4, 7, -13])
Testing for square_sum([20, -10, 6, -19, -8, 6, 5, -4, -13, -4])
Testing for square_sum([19, 14, 5, -20, 5])
Completed in 3.55ms
You have passed all of the tests! :)"""
#alternate solution 1
def square_sum_1(numbers):
    return sum(x ** 2 for x in numbers)
#alternate solution 2
def square_sum_2(numbers):
    return sum(map(lambda x: x**2,numbers))
#alternate solution 3
import numpy

def square_sum_3(numbers):
    return sum(numpy.array(numbers) ** 2)
#alternate solution 4
square_sum_4 = lambda n: sum(e**2 for e in n)