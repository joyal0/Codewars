#Disemvowel Trolls
"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

STRINGSREGULAR EXPRESSIONSFUNDAMENTALS"""
def disemvowel(string_):
    str = ""
    for ch in string_:
        if ch.upper() not in ['A','E','I','O','U']:
            str += ch
    return str
#OUTPUTS
"""
Time: 500ms Passed: 103Failed: 0
Test Results:
Fixed Tests
First fixed test
Second fixed test
Third fixed test
Random Tests
 (100 of 100 Assertions)
Completed in 9.96ms
You have passed all of the tests! :)"""

#alternate solution 1
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

#alternate solution 2
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

#alternate solution 3
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

#alternate solution 4
def disemvowel(string):
        
    s = ""
    for c in string:
        if c.lower() not in "aeiou":
            s += c
    return s

#alternate solution 5
def disemvowel(string):
    return string.translate(None, 'aAeEuUoOiI')