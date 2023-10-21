#Counting sheep...
"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

ARRAYSFUNDAMENTALS"""
def count_sheeps(sheep):
    count = 0
    for ch in sheep:
        if ch:
            count += 1
    return count
#OUTPUTS
"""
Time: 462ms Passed: 53Failed: 0
Test Results:
Tests
Fixed Tests
 (3 of 3 Assertions)
Random Tests
 (50 of 50 Assertions)
Completed in 3.07ms
You have passed all of the tests! :)
"""
#alternate solution 1
def count_sheeps(sheep):
    return sheep.count(True)
#alternate solution 2
def count_sheeps(sheep):
  return len([x for x in sheep if x])
#alternate solution 3
