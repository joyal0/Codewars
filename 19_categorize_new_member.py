#CATEGORIZE NEW MEMBER
"""
DESCRIPTION:
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
FUNDAMENTALS"""

def open_or_senior(data):
    ls = []
    for x in data:
        if x[0]>=55 and x[1]>7:
            ls.append('Senior')
        else:
            ls.append('Open')
    return ls

#OUTPUTS
"""
Time: 521ms Passed: 105Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (5 of 5 Assertions)
Completed in 0.11ms
Random tests
testing for open_or_senior([(26, 11), (63, 4), (48, 12), (80, 7), (38, 24), (81, 22), (14, 7), (88, 4)])
testing for open_or_senior([(65, 26), (17, 3), (84, 17), (34, -1), (27, 13), (26, 5)])
testing for open_or_senior([(53, 10), (24, 1), (30, 1)])
testing for open_or_senior([(27, 12), (12, 17), (17, 15), (25, 8), (13, 2), (66, 24)])
testing for open_or_senior([(42, 2), (30, 24), (37, 5), (58, 25), (62, 0), (44, 25), (76, 6), (46, 20)])
testing for open_or_senior([(28, 12), (90, 4), (35, 3), (80, 10), (31, 7), (90, -2), (35, 10), (65, 20)])
testing for open_or_senior([(14, 21), (76, 23), (12, 3), (17, 19)])
testing for open_or_senior([(27, 19), (35, 21), (55, 7)])
testing for open_or_senior([(41, 0), (44, 21), (89, 6)])
testing for open_or_senior([(18, 14), (18, 23), (14, 8), (31, 2), (85, 10)])
testing for open_or_senior([(48, 7), (59, 5), (33, 21), (21, 21), (11, 19), (79, 3), (47, 18)])
testing for open_or_senior([(54, 26), (34, 6), (28, 23), (73, 1)])
testing for open_or_senior([(58, 13), (81, 15), (90, 1), (53, 8), (58, 8), (80, 24), (47, 10), (49, 6)])
testing for open_or_senior([(12, 11), (53, 14), (81, 25), (72, 5), (43, 3), (15, 7), (17, -2)])
testing for open_or_senior([(79, 11), (52, 2), (24, 1), (18, 13), (22, -2), (60, 22), (28, 24), (15, 16)])
testing for open_or_senior([(50, 24), (80, -1), (54, 20), (27, 12), (64, 13), (58, 26), (37, 20)])
testing for open_or_senior([(69, 10), (62, 10), (35, -2), (27, 20), (21, -2)])
testing for open_or_senior([(68, 17), (68, 23), (74, 2), (67, 1), (33, 22), (38, 22), (11, 6)])
testing for open_or_senior([(22, 24), (33, 20), (47, 14), (46, 2), (67, 18)])
testing for open_or_senior([(62, 7), (76, 4), (65, 9), (42, 4), (63, 1), (65, 0), (27, 0), (79, 11)])
testing for open_or_senior([(16, 13), (48, 18), (16, 11), (66, 2), (18, 5), (80, 24), (76, 20), (83, 11)])
testing for open_or_senior([(27, 1), (87, 22), (23, 25)])
testing for open_or_senior([(38, 6), (11, 16), (41, 3), (35, 0), (82, 13)])
testing for open_or_senior([(13, 6), (21, 11), (71, 5), (48, 13), (12, 21), (10, 24), (63, 13)])
testing for open_or_senior([(25, 0), (54, 8), (43, 10), (89, -2), (52, 18), (30, 4)])
testing for open_or_senior([(60, 13), (16, 12), (63, 19), (46, 17), (53, 6), (40, 3), (22, 14), (45, 17)])
testing for open_or_senior([(42, 5), (90, 6), (15, 9)])
testing for open_or_senior([(30, 18), (30, 13), (17, 10), (69, 21), (87, 1)])
testing for open_or_senior([(73, 10), (11, -1), (74, 24)])
testing for open_or_senior([(18, 8), (79, 26), (17, 9), (44, 0), (30, 15), (79, 3), (42, 23)])
testing for open_or_senior([(84, 14), (69, 8), (28, 9)])
testing for open_or_senior([(66, 17), (60, 11), (30, 0), (45, 12)])
testing for open_or_senior([(89, 2), (55, -2), (44, 24)])
testing for open_or_senior([(44, 13), (21, 8), (20, 5), (21, 7), (26, 3)])
testing for open_or_senior([(44, 3), (62, -2), (54, 9)])
testing for open_or_senior([(53, 23), (68, 26), (72, 24), (85, 1)])
testing for open_or_senior([(75, 19), (74, 17), (79, 23), (50, 21), (60, 5)])
testing for open_or_senior([(58, 14), (50, 18), (63, 3), (25, 3), (27, 5), (83, 4), (28, 24), (50, 14)])
testing for open_or_senior([(18, 18), (39, 26), (13, 1), (14, -1), (16, -1), (82, 1), (20, -2)])
testing for open_or_senior([(34, 16), (55, 21), (25, 21), (40, 26), (36, 13), (35, -2), (60, 7)])
testing for open_or_senior([(61, 8), (90, 5), (67, 13)])
testing for open_or_senior([(72, 10), (44, 18), (14, 2), (41, 14), (38, 20), (89, 22), (70, 6)])
testing for open_or_senior([(22, 15), (62, 4), (89, 9), (22, 22), (71, -2)])
testing for open_or_senior([(15, 20), (60, 16), (60, 23), (57, 13), (18, 1), (32, 21), (88, 1)])
testing for open_or_senior([(50, 4), (34, 3), (38, 4), (52, 1), (57, 17), (53, 21), (37, 12), (39, 18)])
testing for open_or_senior([(83, 21), (86, 14), (11, -2)])
testing for open_or_senior([(90, 12), (12, 25), (81, 20), (12, 7), (87, 17), (68, 13), (23, 11), (66, 10)])
testing for open_or_senior([(21, 0), (35, 15), (63, 3), (81, 13), (43, 13), (19, 12), (24, 16)])
testing for open_or_senior([(78, 4), (73, 3), (69, 17), (66, -2), (52, 15), (17, 14)])
testing for open_or_senior([(75, 14), (76, 5), (73, 16), (33, 23), (63, 1), (78, 17), (47, -2), (52, 22)])
testing for open_or_senior([(82, 12), (18, 0), (67, 2), (38, 6), (73, 26), (85, -1), (25, 13), (61, 25)])
testing for open_or_senior([(86, 7), (89, 20), (39, 23), (78, 2), (51, 20), (88, 8)])
testing for open_or_senior([(55, 18), (35, 14), (14, 1)])
testing for open_or_senior([(60, 19), (19, 24), (40, 9), (51, 25), (14, 9)])
testing for open_or_senior([(64, 16), (58, 12), (51, -2), (57, 8), (75, -2), (51, 10), (26, 1), (28, 0)])
testing for open_or_senior([(65, 4), (63, 26), (61, 3), (69, 21)])
testing for open_or_senior([(64, 20), (88, 17), (44, 26), (24, 8), (88, 14), (58, 7)])
testing for open_or_senior([(38, 9), (10, 26), (60, 23), (57, 12), (68, 11), (43, 12)])
testing for open_or_senior([(19, -2), (36, 22), (12, 16), (61, 10), (64, -2)])
testing for open_or_senior([(60, 2), (15, 20), (15, 25)])
testing for open_or_senior([(59, 22), (19, 17), (67, 12), (33, 6), (60, 26), (10, 12), (73, 20)])
testing for open_or_senior([(18, 22), (33, 12), (23, 26), (21, 4), (37, 17)])
testing for open_or_senior([(12, 3), (81, 0), (19, 16), (43, 5), (45, 13), (57, 3)])
testing for open_or_senior([(12, 18), (40, 2), (12, 5), (13, 5), (11, 19), (18, 1), (88, 1), (29, 1)])
testing for open_or_senior([(81, -1), (29, 15), (32, 1), (44, 8), (37, 22), (22, 5), (66, 17)])
testing for open_or_senior([(28, 21), (46, 0), (61, 3)])
testing for open_or_senior([(62, 10), (12, 2), (29, 3), (68, 17)])
testing for open_or_senior([(74, -1), (59, 22), (33, 24), (40, 14)])
testing for open_or_senior([(70, 11), (16, 10), (74, -1)])
testing for open_or_senior([(84, 26), (80, 0), (84, -1), (13, 5), (30, 14), (36, 0)])
testing for open_or_senior([(66, 10), (50, -1), (70, 10)])
testing for open_or_senior([(76, 16), (89, 1), (64, 11), (66, 18)])
testing for open_or_senior([(71, 26), (52, 16), (26, 0)])
testing for open_or_senior([(65, 14), (31, 1), (22, 7), (74, 5), (71, 9), (83, 1), (41, 18), (24, 15)])
testing for open_or_senior([(78, 9), (73, 10), (87, 0)])
testing for open_or_senior([(29, 5), (32, 21), (81, 26), (19, 5), (56, 17), (89, 26), (29, 13)])
testing for open_or_senior([(56, 18), (70, 1), (75, -1)])
testing for open_or_senior([(67, 10), (77, 14), (57, 26), (54, 21), (85, 25), (85, 9), (10, 14)])
testing for open_or_senior([(62, 13), (90, 21), (20, 17), (82, 3), (32, 6), (30, 1)])
testing for open_or_senior([(16, 18), (61, -2), (26, 25), (47, 2), (69, 0)])
testing for open_or_senior([(19, 13), (49, 10), (56, 25), (45, 0), (78, 21), (17, 0)])
testing for open_or_senior([(62, 7), (33, 8), (54, 4), (50, 16), (23, 20), (84, 11), (13, 10)])
testing for open_or_senior([(80, 23), (89, 16), (80, 1)])
testing for open_or_senior([(77, 20), (71, 6), (89, 16), (50, 22), (62, 24), (22, 14), (74, 1), (57, 8)])
testing for open_or_senior([(61, 11), (13, 16), (72, 25), (78, 24), (43, 15)])
testing for open_or_senior([(83, 0), (37, 10), (51, 14), (39, 17), (78, 25), (82, -1), (15, 21), (42, 6)])
testing for open_or_senior([(68, 6), (45, 23), (18, 7), (61, 23), (10, 17), (41, -1), (81, 17), (62, 19)])
testing for open_or_senior([(61, 12), (30, -1), (62, 9), (56, 0), (29, 2), (70, -1), (43, 6)])
testing for open_or_senior([(78, 1), (40, 8), (46, 17), (14, 1), (90, 14)])
testing for open_or_senior([(37, 26), (76, 24), (78, 1), (56, 17)])
testing for open_or_senior([(21, 5), (36, 26), (74, 0), (29, 23), (81, 24), (39, 14), (59, 20), (27, 24)])
testing for open_or_senior([(26, 17), (17, 26), (79, 6)])
testing for open_or_senior([(21, 2), (68, 23), (71, -2), (36, 20)])
testing for open_or_senior([(85, 8), (12, 25), (76, 17), (72, 20), (28, 13), (49, -1), (59, 21), (88, 26)])
testing for open_or_senior([(66, -2), (79, 15), (85, 7), (58, 4), (16, 16), (38, 25), (22, 19)])
testing for open_or_senior([(42, 15), (65, 16), (35, 25), (68, 10), (23, 16), (44, 6), (84, 19), (34, 6)])
testing for open_or_senior([(21, 4), (21, -1), (28, 7), (48, 14)])
testing for open_or_senior([(39, 25), (58, 14), (54, 10), (14, 21), (73, 1), (52, 4), (90, 25), (53, 4)])
testing for open_or_senior([(33, 26), (71, 20), (65, 18), (39, 15)])
testing for open_or_senior([(10, 10), (19, 7), (35, 3), (44, 26), (65, 26), (25, 12), (86, 1)])
Completed in 7.04ms
You have passed all of the tests! :)"""

#alternate solution 1
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

#alternate solution 2
def openOrSenior(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]

#alternate solution 3
def openOrSenior(data):
    return [['Open', 'Senior'][age >= 55 and handicap > 7] for age, handicap in data]