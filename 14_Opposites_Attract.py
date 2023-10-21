#OPPOSITES ATTRACT
"""
DESCRIPTION:
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

FUNDAMENTALS"""
def lovefunc( flower1, flower2 ):
    # ...
    ch1 = flower1%2
    ch2 = flower2%2
    if(ch1!=ch2):
        return True
    else:
        return False
#OUTPUTS
"""
Time: 501ms Passed: 104Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (4 of 4 Assertions)
Completed in 0.06ms
Random Tests
testing for lovefunc(671, 281)
testing for lovefunc(313, 876)
testing for lovefunc(555, 885)
testing for lovefunc(316, 384)
testing for lovefunc(264, 671)
testing for lovefunc(77, 890)
testing for lovefunc(800, 812)
testing for lovefunc(896, 676)
testing for lovefunc(393, 927)
testing for lovefunc(375, 928)
testing for lovefunc(923, 814)
testing for lovefunc(163, 361)
testing for lovefunc(991, 216)
testing for lovefunc(71, 289)
testing for lovefunc(618, 534)
testing for lovefunc(52, 107)
testing for lovefunc(644, 187)
testing for lovefunc(327, 285)
testing for lovefunc(27, 833)
testing for lovefunc(257, 169)
testing for lovefunc(313, 826)
testing for lovefunc(371, 268)
testing for lovefunc(538, 92)
testing for lovefunc(207, 790)
testing for lovefunc(309, 829)
testing for lovefunc(756, 368)
testing for lovefunc(287, 881)
testing for lovefunc(788, 107)
testing for lovefunc(733, 656)
testing for lovefunc(290, 800)
testing for lovefunc(451, 459)
testing for lovefunc(794, 244)
testing for lovefunc(168, 30)
testing for lovefunc(69, 233)
testing for lovefunc(531, 687)
testing for lovefunc(139, 819)
testing for lovefunc(461, 310)
testing for lovefunc(257, 973)
testing for lovefunc(810, 261)
testing for lovefunc(184, 953)
testing for lovefunc(370, 360)
testing for lovefunc(260, 524)
testing for lovefunc(132, 892)
testing for lovefunc(605, 721)
testing for lovefunc(578, 152)
testing for lovefunc(798, 84)
testing for lovefunc(545, 402)
testing for lovefunc(632, 905)
testing for lovefunc(78, 91)
testing for lovefunc(126, 675)
testing for lovefunc(691, 398)
testing for lovefunc(378, 547)
testing for lovefunc(911, 581)
testing for lovefunc(13, 730)
testing for lovefunc(240, 321)
testing for lovefunc(425, 781)
testing for lovefunc(100, 215)
testing for lovefunc(428, 229)
testing for lovefunc(146, 32)
testing for lovefunc(121, 364)
testing for lovefunc(328, 605)
testing for lovefunc(267, 785)
testing for lovefunc(391, 411)
testing for lovefunc(126, 934)
testing for lovefunc(724, 589)
testing for lovefunc(940, 74)
testing for lovefunc(96, 957)
testing for lovefunc(123, 188)
testing for lovefunc(424, 932)
testing for lovefunc(397, 929)
testing for lovefunc(902, 864)
testing for lovefunc(432, 651)
testing for lovefunc(709, 681)
testing for lovefunc(49, 467)
testing for lovefunc(480, 944)
testing for lovefunc(869, 3)
testing for lovefunc(773, 113)
testing for lovefunc(426, 475)
testing for lovefunc(776, 904)
testing for lovefunc(189, 111)
testing for lovefunc(18, 12)
testing for lovefunc(824, 716)
testing for lovefunc(294, 978)
testing for lovefunc(638, 898)
testing for lovefunc(760, 706)
testing for lovefunc(405, 442)
testing for lovefunc(163, 769)
testing for lovefunc(148, 848)
testing for lovefunc(674, 338)
testing for lovefunc(26, 892)
testing for lovefunc(418, 629)
testing for lovefunc(645, 889)
testing for lovefunc(75, 91)
testing for lovefunc(368, 427)
testing for lovefunc(140, 907)
testing for lovefunc(423, 101)
testing for lovefunc(6, 26)
testing for lovefunc(701, 213)
testing for lovefunc(407, 148)
testing for lovefunc(385, 481)
Completed in 4.84ms
You have passed all of the tests! :)"""
#alternate solution 1
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
#alternate solution 2
def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2
#alternate solution 3
def lovefunc(f1, f2):
    return True if (f1 % 2 == 0 and f2 % 2 != 0) or (f2 % 2 == 0 and f1 % 2 != 0) else False
#alternate solution 4
def lovefunc( flower1, flower2 ):
    if flower1%2 != flower2%2:
        return True
    else:
        return False