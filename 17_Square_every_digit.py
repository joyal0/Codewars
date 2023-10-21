#SQUARE EVERY DIGIT
"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!

MATHEMATICSFUNDAMENTALS"""
def square_digits(num):
    # Your code here
    sum=""
    l=[]
    if num==0:
        l.append(0)
    while num>0:
        l.append((num%10)**2)
        num= int(num/10)
    for x in l:
        sum = str(x)+sum
    return int(sum)
#OUTPUTS
"""
Time: 475ms Passed: 103Failed: 0
Test Results:
Fixed tests: 
testing for square_digits(3212)
testing for square_digits(2112)
testing for square_digits(0)
Completed in 0.16ms
Random Tests: 
testing for square_digits(4426493)
testing for square_digits(4907243)
testing for square_digits(2170540)
testing for square_digits(7980340)
testing for square_digits(413594)
testing for square_digits(6513538)
testing for square_digits(8549846)
testing for square_digits(8139055)
testing for square_digits(664360)
testing for square_digits(8125802)
testing for square_digits(8224801)
testing for square_digits(9332322)
testing for square_digits(3044046)
testing for square_digits(4024738)
testing for square_digits(831688)
testing for square_digits(9241919)
testing for square_digits(790518)
testing for square_digits(2163893)
testing for square_digits(4928669)
testing for square_digits(8717558)
testing for square_digits(6250877)
testing for square_digits(1757872)
testing for square_digits(9523837)
testing for square_digits(2924328)
testing for square_digits(4654494)
testing for square_digits(1595972)
testing for square_digits(1226917)
testing for square_digits(867693)
testing for square_digits(2863923)
testing for square_digits(9060321)
testing for square_digits(7202889)
testing for square_digits(2960756)
testing for square_digits(9301062)
testing for square_digits(23667)
testing for square_digits(9089452)
testing for square_digits(2858536)
testing for square_digits(2159491)
testing for square_digits(3817110)
testing for square_digits(1563611)
testing for square_digits(6978771)
testing for square_digits(6892144)
testing for square_digits(5411561)
testing for square_digits(646111)
testing for square_digits(5444691)
testing for square_digits(4533033)
testing for square_digits(3987093)
testing for square_digits(3199020)
testing for square_digits(942127)
testing for square_digits(6271664)
testing for square_digits(6348669)
testing for square_digits(3019419)
testing for square_digits(3974625)
testing for square_digits(4366730)
testing for square_digits(6222404)
testing for square_digits(780667)
testing for square_digits(7832399)
testing for square_digits(9300960)
testing for square_digits(9947396)
testing for square_digits(8651473)
testing for square_digits(8567328)
testing for square_digits(3314745)
testing for square_digits(101678)
testing for square_digits(2766847)
testing for square_digits(6295351)
testing for square_digits(4924201)
testing for square_digits(9665526)
testing for square_digits(7349200)
testing for square_digits(6056403)
testing for square_digits(1903035)
testing for square_digits(1190620)
testing for square_digits(8778419)
testing for square_digits(9557865)
testing for square_digits(5942286)
testing for square_digits(3658551)
testing for square_digits(9746089)
testing for square_digits(8882446)
testing for square_digits(4436928)
testing for square_digits(8137775)
testing for square_digits(5163504)
testing for square_digits(6072081)
testing for square_digits(4139532)
testing for square_digits(9982790)
testing for square_digits(580595)
testing for square_digits(6902774)
testing for square_digits(1733130)
testing for square_digits(2018317)
testing for square_digits(6265126)
testing for square_digits(1790407)
testing for square_digits(3857754)
testing for square_digits(2454488)
testing for square_digits(2213085)
testing for square_digits(6251860)
testing for square_digits(4122267)
testing for square_digits(9169323)
testing for square_digits(8903662)
testing for square_digits(7642151)
testing for square_digits(122494)
testing for square_digits(69653)
testing for square_digits(8866281)
testing for square_digits(268041)
Completed in 5.69ms
You have passed all of the tests! :)"""

#alternate solution 1
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

#alternate solution 2
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

#alternate solution 3
def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)
        
#alternate solution 4
