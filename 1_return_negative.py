#Return Negative
"""In this simple assignment you are given a number and have to make it negative. 
But maybe the number is already negative?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
"""

#Solutions
def make_negative( number ):
    return(number if number<0 else -number)

"""
OUTPUTS
Time: 476ms Passed: 103Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (3 of 3 Assertions)
Completed in 0.05ms
Random Tests
testing for make_negative(612)
testing for make_negative(-68)
testing for make_negative(453)
testing for make_negative(-644)
testing for make_negative(-563)
testing for make_negative(591)
testing for make_negative(291)
testing for make_negative(99)
testing for make_negative(133)
testing for make_negative(-364)
testing for make_negative(883)
testing for make_negative(-564)
testing for make_negative(-222)
testing for make_negative(137)
testing for make_negative(-416)
testing for make_negative(-866)
testing for make_negative(-219)
testing for make_negative(226)
testing for make_negative(581)
testing for make_negative(570)
testing for make_negative(-385)
testing for make_negative(417)
testing for make_negative(-166)
testing for make_negative(592)
testing for make_negative(486)
testing for make_negative(199)
testing for make_negative(548)
testing for make_negative(-56)
testing for make_negative(-697)
testing for make_negative(145)
testing for make_negative(936)
testing for make_negative(-191)
testing for make_negative(-352)
testing for make_negative(-970)
testing for make_negative(-240)
testing for make_negative(902)
testing for make_negative(289)
testing for make_negative(107)
testing for make_negative(810)
testing for make_negative(90)
testing for make_negative(457)
testing for make_negative(928)
testing for make_negative(964)
testing for make_negative(-162)
testing for make_negative(-234)
testing for make_negative(86)
testing for make_negative(543)
testing for make_negative(569)
testing for make_negative(339)
testing for make_negative(478)
testing for make_negative(616)
testing for make_negative(145)
testing for make_negative(-743)
testing for make_negative(310)
testing for make_negative(628)
testing for make_negative(303)
testing for make_negative(-112)
testing for make_negative(-938)
testing for make_negative(20)
testing for make_negative(570)
testing for make_negative(659)
testing for make_negative(-953)
testing for make_negative(677)
testing for make_negative(310)
testing for make_negative(713)
testing for make_negative(-448)
testing for make_negative(543)
testing for make_negative(-334)
testing for make_negative(621)
testing for make_negative(458)
testing for make_negative(-995)
testing for make_negative(-753)
testing for make_negative(419)
testing for make_negative(-443)
testing for make_negative(-593)
testing for make_negative(-864)
testing for make_negative(888)
testing for make_negative(51)
testing for make_negative(-375)
testing for make_negative(-139)
testing for make_negative(-281)
testing for make_negative(408)
testing for make_negative(585)
testing for make_negative(-993)
testing for make_negative(-970)
testing for make_negative(-240)
testing for make_negative(81)
testing for make_negative(831)
testing for make_negative(-377)
testing for make_negative(755)
testing for make_negative(162)
testing for make_negative(-384)
testing for make_negative(-68)
testing for make_negative(661)
testing for make_negative(413)
testing for make_negative(-590)
testing for make_negative(191)
testing for make_negative(861)
testing for make_negative(553)
testing for make_negative(95)
Completed in 4.26ms
You have passed all of the tests! :)"""