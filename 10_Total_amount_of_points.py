#TOTAL AMOUNT OF POINTS
"""
DESCRIPTION:
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
FUNDAMENTALSARRAYSSTRINGS"""
def points(games):
    point_x = 0
    for str in games:
        if (0<=int(str[0])<=4) and (0<=int(str[2])<=4):   #optional
            if (str[0]>str[2]):
                point_x+=3
            elif (str[0]==str[2]):
                point_x+=1
    return point_x
#OUTPUTS
"""
Time: 519ms Passed: 55Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (5 of 5 Assertions)
Completed in 0.13ms
Random Tests
Testing for points points(['1:4', '2:2', '3:0', '1:0', '2:3', '2:0', '0:0', '1:1', '4:4', '1:2'])
Testing for points points(['0:0', '2:3', '0:4', '3:1', '3:3', '1:4', '1:1', '2:1', '4:1', '0:1'])
Testing for points points(['0:0', '1:2', '0:0', '2:3', '3:1', '4:3', '1:4', '4:2', '1:1', '1:2'])
Testing for points points(['3:4', '4:4', '1:2', '1:0', '0:0', '0:3', '3:1', '2:3', '3:4', '1:2'])
Testing for points points(['1:4', '1:3', '1:2', '2:1', '3:1', '3:4', '0:3', '3:1', '3:3', '2:3'])
Testing for points points(['4:3', '2:4', '0:0', '3:2', '2:2', '3:4', '0:2', '3:3', '4:3', '2:4'])
Testing for points points(['0:2', '3:4', '3:2', '1:0', '2:4', '1:0', '0:3', '0:0', '4:4', '1:1'])
Testing for points points(['0:4', '4:1', '1:1', '2:4', '4:3', '3:2', '1:0', '3:2', '2:3', '3:4'])
Testing for points points(['1:2', '4:3', '0:3', '0:4', '0:3', '4:0', '0:4', '2:1', '3:2', '4:0'])
Testing for points points(['1:3', '2:4', '2:2', '4:3', '2:4', '3:1', '4:0', '3:3', '1:4', '0:4'])
Testing for points points(['0:0', '1:1', '4:2', '4:3', '0:4', '2:2', '3:3', '1:4', '4:1', '4:3'])
Testing for points points(['1:3', '1:3', '1:4', '2:1', '4:1', '3:1', '0:2', '2:1', '4:4', '1:1'])
Testing for points points(['1:2', '3:2', '3:4', '2:2', '0:2', '4:1', '3:3', '0:3', '3:4', '0:3'])
Testing for points points(['2:3', '4:3', '4:0', '0:2', '4:3', '0:4', '4:1', '0:2', '1:1', '4:0'])
Testing for points points(['1:0', '2:1', '0:4', '2:3', '1:3', '4:1', '3:0', '2:3', '2:3', '4:4'])
Testing for points points(['3:3', '2:2', '2:4', '0:4', '4:3', '2:4', '2:2', '1:3', '1:3', '2:1'])
Testing for points points(['2:3', '4:4', '3:1', '0:2', '1:2', '3:2', '4:0', '0:4', '3:3', '1:0'])
Testing for points points(['4:0', '1:0', '3:0', '1:3', '4:0', '0:3', '0:4', '3:2', '0:4', '1:4'])
Testing for points points(['0:4', '0:3', '3:3', '3:1', '1:4', '0:2', '3:4', '3:1', '4:4', '1:3'])
Testing for points points(['2:0', '4:2', '0:3', '4:2', '2:0', '2:3', '1:1', '2:1', '3:1', '0:1'])
Testing for points points(['3:4', '4:1', '3:3', '1:3', '4:4', '4:1', '3:1', '1:0', '0:0', '4:2'])
Testing for points points(['3:2', '3:2', '0:0', '1:2', '3:0', '1:2', '0:1', '3:2', '4:3', '2:2'])
Testing for points points(['4:2', '1:0', '4:0', '2:2', '0:1', '1:3', '2:0', '4:3', '3:2', '1:0'])
Testing for points points(['2:3', '1:4', '0:2', '1:1', '3:0', '3:4', '3:4', '2:1', '4:2', '0:3'])
Testing for points points(['1:4', '1:0', '4:2', '1:0', '1:0', '3:2', '3:1', '4:3', '1:1', '2:0'])
Testing for points points(['4:1', '3:3', '1:0', '4:3', '2:3', '0:4', '2:4', '2:1', '0:3', '4:3'])
Testing for points points(['3:4', '0:1', '4:2', '2:3', '0:4', '2:0', '1:0', '1:4', '0:4', '3:3'])
Testing for points points(['3:1', '0:1', '3:0', '4:3', '2:0', '3:2', '3:0', '3:2', '0:4', '1:4'])
Testing for points points(['0:4', '4:2', '0:4', '2:1', '4:2', '4:2', '3:3', '2:2', '2:3', '3:2'])
Testing for points points(['4:4', '2:4', '3:2', '4:1', '3:2', '3:3', '3:4', '0:4', '0:3', '1:3'])
Testing for points points(['1:2', '2:4', '1:0', '2:4', '4:3', '4:2', '3:3', '1:3', '2:3', '1:2'])
Testing for points points(['2:0', '0:2', '3:2', '0:3', '1:0', '0:1', '0:0', '0:2', '3:2', '2:4'])
Testing for points points(['2:1', '3:4', '4:0', '4:1', '0:3', '3:4', '4:3', '3:3', '1:1', '4:4'])
Testing for points points(['0:0', '3:3', '2:4', '3:1', '2:1', '0:3', '0:4', '0:3', '4:0', '2:1'])
Testing for points points(['1:1', '4:3', '3:1', '2:3', '2:1', '1:1', '1:2', '2:2', '4:2', '4:0'])
Testing for points points(['3:3', '1:2', '3:3', '1:1', '3:1', '4:2', '0:0', '1:0', '1:4', '4:0'])
Testing for points points(['2:4', '2:0', '3:3', '4:3', '2:1', '4:3', '2:1', '4:0', '3:3', '3:1'])
Testing for points points(['0:3', '3:4', '1:1', '4:0', '1:1', '2:4', '4:3', '4:3', '1:0', '0:2'])
Testing for points points(['1:0', '2:4', '2:3', '2:4', '0:4', '1:0', '0:4', '1:4', '2:2', '4:2'])
Testing for points points(['4:2', '3:2', '4:4', '3:2', '1:3', '4:4', '1:1', '2:3', '2:1', '2:2'])
Testing for points points(['2:4', '4:2', '2:3', '0:0', '2:0', '2:2', '2:2', '1:2', '0:0', '0:1'])
Testing for points points(['3:1', '1:3', '0:3', '1:4', '0:3', '2:0', '0:4', '1:3', '1:3', '2:0'])
Testing for points points(['1:1', '2:3', '3:3', '4:0', '1:0', '1:4', '0:1', '2:1', '4:1', '1:0'])
Testing for points points(['0:0', '1:3', '3:1', '1:0', '2:0', '4:2', '3:2', '0:1', '1:4', '4:0'])
Testing for points points(['0:2', '4:2', '4:0', '0:2', '0:2', '4:3', '2:0', '4:0', '0:0', '3:0'])
Testing for points points(['1:1', '1:4', '1:1', '4:0', '3:0', '4:1', '4:2', '3:2', '0:0', '2:2'])
Testing for points points(['3:4', '0:3', '3:3', '1:3', '1:4', '1:2', '0:2', '1:4', '2:0', '2:4'])
Testing for points points(['0:1', '4:3', '2:3', '0:3', '2:3', '2:3', '2:3', '1:1', '0:3', '2:4'])
Testing for points points(['4:4', '1:3', '4:1', '1:0', '2:2', '3:1', '1:3', '1:1', '4:4', '2:2'])
Testing for points points(['4:1', '3:0', '1:0', '3:2', '2:4', '2:3', '4:0', '2:0', '0:2', '2:3'])
Completed in 5.66ms
You have passed all of the tests! :)"""
#alternate solution 1
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count
#aalaternate solution 2
def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))
#alternate solution 3
def points(games):
    result = 0
    for item in games:
        result += 3 if item[0] > item[2] else 0
        result += 1 if item[0] == item[2] else 0
    return result
#alternate solution 4
def points(games):
	return sum([0,1,3][1+(g[0]>g[2])-(g[0]<g[2])] for g in games)