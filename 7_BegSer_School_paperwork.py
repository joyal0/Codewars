#Beginner Series #1 School Paperwork
"""
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
Example:
n= 5, m=5: 25
n=-5, m=5:  0
Waiting for translations and Feedback! Thanks!

FUNDAMENTALS"""
def paperwork(n, m):
    # Happy Coding! ^_^
    if ((n>0)and(m>0)):
            return n*m
    else:
        return 0
    
#OUTPUTS
"""
Time: 488ms Passed: 156Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (6 of 6 Assertions)
Completed in 0.13ms
Random Tests
Testing for paperwork(1, 3)
Testing for paperwork(1, 2)
Testing for paperwork(0, 0)
Testing for paperwork(5, 1)
Testing for paperwork(0, 0)
Testing for paperwork(2, 3)
Testing for paperwork(1, 3)
Testing for paperwork(3, 3)
Testing for paperwork(1, 4)
Testing for paperwork(0, 1)
Testing for paperwork(4, 5)
Testing for paperwork(1, 2)
Testing for paperwork(2, 2)
Testing for paperwork(3, 1)
Testing for paperwork(1, 2)
Testing for paperwork(1, 4)
Testing for paperwork(1, 5)
Testing for paperwork(0, 2)
Testing for paperwork(5, 0)
Testing for paperwork(5, 3)
Testing for paperwork(5, 5)
Testing for paperwork(2, 4)
Testing for paperwork(0, 5)
Testing for paperwork(4, 0)
Testing for paperwork(5, 1)
Testing for paperwork(2, 2)
Testing for paperwork(4, 1)
Testing for paperwork(0, 3)
Testing for paperwork(5, 5)
Testing for paperwork(4, 5)
Testing for paperwork(3, 2)
Testing for paperwork(2, 0)
Testing for paperwork(2, 5)
Testing for paperwork(2, 0)
Testing for paperwork(4, 0)
Testing for paperwork(0, 3)
Testing for paperwork(0, 0)
Testing for paperwork(5, 1)
Testing for paperwork(0, 2)
Testing for paperwork(2, 1)
Testing for paperwork(5, 3)
Testing for paperwork(4, 1)
Testing for paperwork(0, 5)
Testing for paperwork(2, 4)
Testing for paperwork(4, 5)
Testing for paperwork(4, 3)
Testing for paperwork(1, 1)
Testing for paperwork(5, 0)
Testing for paperwork(4, 4)
Testing for paperwork(1, 1)
Testing for paperwork(-22, 18)
Testing for paperwork(-1, 25)
Testing for paperwork(32, -79)
Testing for paperwork(-72, 23)
Testing for paperwork(-6, -98)
Testing for paperwork(-29, 58)
Testing for paperwork(-32, -66)
Testing for paperwork(0, 96)
Testing for paperwork(75, -13)
Testing for paperwork(32, 9)
Testing for paperwork(-11, 76)
Testing for paperwork(98, 30)
Testing for paperwork(42, 14)
Testing for paperwork(98, 47)
Testing for paperwork(-57, -13)
Testing for paperwork(35, -52)
Testing for paperwork(12, -78)
Testing for paperwork(-17, -100)
Testing for paperwork(-24, 56)
Testing for paperwork(-69, -15)
Testing for paperwork(-99, 95)
Testing for paperwork(100, -2)
Testing for paperwork(-76, -18)
Testing for paperwork(-19, 98)
Testing for paperwork(-89, 62)
Testing for paperwork(17, 69)
Testing for paperwork(13, -66)
Testing for paperwork(7, -19)
Testing for paperwork(95, -25)
Testing for paperwork(55, 77)
Testing for paperwork(-96, 79)
Testing for paperwork(96, 43)
Testing for paperwork(-86, 95)
Testing for paperwork(-2, -96)
Testing for paperwork(-33, 79)
Testing for paperwork(62, 1)
Testing for paperwork(8, -3)
Testing for paperwork(27, 2)
Testing for paperwork(-20, -63)
Testing for paperwork(22, 2)
Testing for paperwork(93, 61)
Testing for paperwork(-67, -25)
Testing for paperwork(94, 9)
Testing for paperwork(-66, -17)
Testing for paperwork(-77, 58)
Testing for paperwork(48, 87)
Testing for paperwork(-43, -94)
Testing for paperwork(5, 60)
Testing for paperwork(-18, -23)
Testing for paperwork(62, -13)
Testing for paperwork(79, 83)
Testing for paperwork(19, -87)
Testing for paperwork(14, 23)
Testing for paperwork(84, 95)
Testing for paperwork(83, -77)
Testing for paperwork(-62, -92)
Testing for paperwork(61, 76)
Testing for paperwork(62, -84)
Testing for paperwork(-22, -96)
Testing for paperwork(94, -16)
Testing for paperwork(-11, -68)
Testing for paperwork(-32, 68)
Testing for paperwork(4, -9)
Testing for paperwork(-66, -98)
Testing for paperwork(-64, 53)
Testing for paperwork(-11, 59)
Testing for paperwork(-81, 8)
Testing for paperwork(-48, 49)
Testing for paperwork(-76, 51)
Testing for paperwork(2, -74)
Testing for paperwork(38, 39)
Testing for paperwork(95, 96)
Testing for paperwork(-43, -66)
Testing for paperwork(38, 21)
Testing for paperwork(-13, -47)
Testing for paperwork(-78, 36)
Testing for paperwork(36, 84)
Testing for paperwork(-29, -3)
Testing for paperwork(-36, 3)
Testing for paperwork(-49, -49)
Testing for paperwork(-18, -3)
Testing for paperwork(-82, 50)
Testing for paperwork(-99, 43)
Testing for paperwork(56, 20)
Testing for paperwork(82, -51)
Testing for paperwork(-11, 89)
Testing for paperwork(-80, -75)
Testing for paperwork(76, 2)
Testing for paperwork(-22, 99)
Testing for paperwork(-50, 73)
Testing for paperwork(39, -47)
Testing for paperwork(-6, -36)
Testing for paperwork(89, 29)
Testing for paperwork(2, 48)
Testing for paperwork(95, 50)
Testing for paperwork(39, 51)
Testing for paperwork(65, 85)
Testing for paperwork(-83, -100)
Testing for paperwork(-26, 84)
Testing for paperwork(-7, 42)
Completed in 5.96ms
You have passed all of the tests! :)"""
# my alternate solution 1
def paperwork(n, m):
    # Happy Coding! ^_^
    return n*m if ( n>0 and m>0 ) else 0
#OUTPUTS
"""
Time: 486ms Passed: 156Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (6 of 6 Assertions)
Completed in 0.11ms
Random Tests
Testing for paperwork(1, 1)
Testing for paperwork(4, 2)
Testing for paperwork(3, 5)
Testing for paperwork(3, 3)
Testing for paperwork(5, 3)
Testing for paperwork(3, 3)
Testing for paperwork(3, 3)
Testing for paperwork(2, 2)
Testing for paperwork(1, 0)
Testing for paperwork(1, 1)
Testing for paperwork(2, 2)
Testing for paperwork(1, 2)
Testing for paperwork(4, 4)
Testing for paperwork(0, 4)
Testing for paperwork(5, 2)
Testing for paperwork(1, 4)
Testing for paperwork(4, 5)
Testing for paperwork(5, 4)
Testing for paperwork(0, 1)
Testing for paperwork(2, 3)
Testing for paperwork(1, 3)
Testing for paperwork(4, 1)
Testing for paperwork(0, 5)
Testing for paperwork(2, 0)
Testing for paperwork(0, 3)
Testing for paperwork(5, 3)
Testing for paperwork(2, 2)
Testing for paperwork(5, 3)
Testing for paperwork(3, 2)
Testing for paperwork(4, 0)
Testing for paperwork(4, 1)
Testing for paperwork(2, 0)
Testing for paperwork(1, 2)
Testing for paperwork(5, 2)
Testing for paperwork(2, 3)
Testing for paperwork(0, 2)
Testing for paperwork(3, 2)
Testing for paperwork(3, 4)
Testing for paperwork(0, 4)
Testing for paperwork(2, 2)
Testing for paperwork(1, 0)
Testing for paperwork(1, 1)
Testing for paperwork(0, 3)
Testing for paperwork(1, 5)
Testing for paperwork(4, 5)
Testing for paperwork(5, 5)
Testing for paperwork(4, 3)
Testing for paperwork(3, 4)
Testing for paperwork(2, 1)
Testing for paperwork(3, 4)
Testing for paperwork(74, -75)
Testing for paperwork(-22, -86)
Testing for paperwork(-63, 1)
Testing for paperwork(-41, -51)
Testing for paperwork(2, 4)
Testing for paperwork(-82, 30)
Testing for paperwork(-86, -4)
Testing for paperwork(-97, 24)
Testing for paperwork(-63, -83)
Testing for paperwork(-90, 26)
Testing for paperwork(83, 31)
Testing for paperwork(15, -93)
Testing for paperwork(11, 58)
Testing for paperwork(-74, 35)
Testing for paperwork(82, -66)
Testing for paperwork(43, -82)
Testing for paperwork(13, -90)
Testing for paperwork(-39, 30)
Testing for paperwork(50, -96)
Testing for paperwork(96, 43)
Testing for paperwork(35, -7)
Testing for paperwork(-72, 98)
Testing for paperwork(-40, 87)
Testing for paperwork(5, -73)
Testing for paperwork(-36, -23)
Testing for paperwork(-37, -2)
Testing for paperwork(44, 38)
Testing for paperwork(-100, -90)
Testing for paperwork(-2, 12)
Testing for paperwork(12, -9)
Testing for paperwork(15, 21)
Testing for paperwork(-40, -44)
Testing for paperwork(13, 99)
Testing for paperwork(-33, 84)
Testing for paperwork(92, 49)
Testing for paperwork(93, -90)
Testing for paperwork(7, -53)
Testing for paperwork(-52, 82)
Testing for paperwork(13, -19)
Testing for paperwork(85, -79)
Testing for paperwork(65, 79)
Testing for paperwork(-24, 6)
Testing for paperwork(-66, -1)
Testing for paperwork(34, -53)
Testing for paperwork(41, -86)
Testing for paperwork(-75, -95)
Testing for paperwork(-5, -75)
Testing for paperwork(-13, 82)
Testing for paperwork(-49, 88)
Testing for paperwork(37, -44)
Testing for paperwork(-55, -39)
Testing for paperwork(88, -83)
Testing for paperwork(35, 35)
Testing for paperwork(-40, 80)
Testing for paperwork(-2, 68)
Testing for paperwork(-92, -96)
Testing for paperwork(20, 46)
Testing for paperwork(-3, 88)
Testing for paperwork(82, 84)
Testing for paperwork(49, 83)
Testing for paperwork(83, 1)
Testing for paperwork(-37, -78)
Testing for paperwork(89, 5)
Testing for paperwork(-35, -32)
Testing for paperwork(-48, 50)
Testing for paperwork(-35, 47)
Testing for paperwork(73, -68)
Testing for paperwork(32, -39)
Testing for paperwork(98, -30)
Testing for paperwork(-88, 92)
Testing for paperwork(-37, -61)
Testing for paperwork(-69, -90)
Testing for paperwork(-57, 25)
Testing for paperwork(51, -76)
Testing for paperwork(-68, -84)
Testing for paperwork(-91, 59)
Testing for paperwork(73, -54)
Testing for paperwork(-48, -81)
Testing for paperwork(-43, 90)
Testing for paperwork(-36, 28)
Testing for paperwork(-18, -66)
Testing for paperwork(-81, 16)
Testing for paperwork(15, 15)
Testing for paperwork(-15, 83)
Testing for paperwork(-99, 61)
Testing for paperwork(37, 63)
Testing for paperwork(76, -70)
Testing for paperwork(25, -7)
Testing for paperwork(-59, 25)
Testing for paperwork(51, 79)
Testing for paperwork(68, -73)
Testing for paperwork(45, -94)
Testing for paperwork(-62, -99)
Testing for paperwork(65, -29)
Testing for paperwork(46, 19)
Testing for paperwork(3, 23)
Testing for paperwork(-10, -13)
Testing for paperwork(4, 61)
Testing for paperwork(85, -47)
Testing for paperwork(-40, -52)
Completed in 6.09ms
You have passed all of the tests! :)"""
#alternate solution 2
def paperwork(n, m):
    return max(n, 0)*max(m, 0)
#alternate solution 3
def paperwork(n, m):
    return n*m*(n>0)*(m>0)
#alterrnate solution 4
def paperwork(n, m):
    return [0, n * m][n > 0 and m > 0]
