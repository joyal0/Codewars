#Keep Hydrated!
"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
ALGORITHMSMATHEMATICSFUNDAMENTALS"""

#Solution
def litres(time):
    return int(time/2)
#OUTPUTS
"""
Time: 509ms Passed: 107Failed: 0
Test Results:
Fixed tests
Basic Test Cases
 (7 of 7 Assertions)
Completed in 0.11ms
Random Tests
Testing for litres(266)
Testing for litres(270)
Testing for litres(879)
Testing for litres(896)
Testing for litres(70)
Testing for litres(273)
Testing for litres(55)
Testing for litres(831)
Testing for litres(952)
Testing for litres(166)
Testing for litres(71)
Testing for litres(909)
Testing for litres(483)
Testing for litres(633)
Testing for litres(258)
Testing for litres(147)
Testing for litres(798)
Testing for litres(603)
Testing for litres(387)
Testing for litres(959)
Testing for litres(945)
Testing for litres(968)
Testing for litres(607)
Testing for litres(102)
Testing for litres(508)
Testing for litres(326)
Testing for litres(887)
Testing for litres(427)
Testing for litres(68)
Testing for litres(234)
Testing for litres(538)
Testing for litres(770)
Testing for litres(873)
Testing for litres(160)
Testing for litres(429)
Testing for litres(414)
Testing for litres(10)
Testing for litres(302)
Testing for litres(697)
Testing for litres(439)
Testing for litres(785)
Testing for litres(247)
Testing for litres(351)
Testing for litres(489)
Testing for litres(813)
Testing for litres(782)
Testing for litres(3)
Testing for litres(641)
Testing for litres(246)
Testing for litres(766)
Testing for litres(752)
Testing for litres(709)
Testing for litres(861)
Testing for litres(642)
Testing for litres(507)
Testing for litres(960)
Testing for litres(51)
Testing for litres(629)
Testing for litres(371)
Testing for litres(205)
Testing for litres(251)
Testing for litres(488)
Testing for litres(680)
Testing for litres(594)
Testing for litres(560)
Testing for litres(735)
Testing for litres(304)
Testing for litres(606)
Testing for litres(365)
Testing for litres(550)
Testing for litres(505)
Testing for litres(723)
Testing for litres(168)
Testing for litres(34)
Testing for litres(578)
Testing for litres(318)
Testing for litres(238)
Testing for litres(156)
Testing for litres(890)
Testing for litres(67)
Testing for litres(148)
Testing for litres(550)
Testing for litres(390)
Testing for litres(28)
Testing for litres(468)
Testing for litres(202)
Testing for litres(222)
Testing for litres(293)
Testing for litres(862)
Testing for litres(218)
Testing for litres(845)
Testing for litres(584)
Testing for litres(873)
Testing for litres(321)
Testing for litres(834)
Testing for litres(200)
Testing for litres(343)
Testing for litres(435)
Testing for litres(363)
Testing for litres(896)
Completed in 4.51ms
You have passed all of the tests! :)"""

#alternate solution
def litres(time):
    return time // 2
#alternate solution
import math
def litres(time):
    return math.floor(.50 * time)
#alternate solution