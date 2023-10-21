#SENTENCE SMASH
"""
DESCRIPTION:
Sentence Smash
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
STRINGS ARRAYS FUNDAMENTALS"""
def smash(words):
    res = ""
    limit = len(words)-1
    for i in range(0,len(words)):
        if i==limit:
            res+=words[i]
            i+=1
        elif i<=limit:
            res+=words[i]+" "
            i+=1
    return res
#OUTPUTS
"""
Time: 544ms Passed: 105Failed: 0
Test Results:
smash
Should return empty string for empty array.
One word example should return the word.
Multiple words should be separated by spaces.
 (3 of 3 Assertions)
Random Tests
 (100 of 100 Assertions)
Completed in 10.08ms
You have passed all of the tests! :)"""
#alternate solution 1
def smash(words):
    return " ".join(words)
#alternate solution 2
def smash(words):
    return ' '.join(words).strip()
#alternate solution 3
def smash(words):
    
    i=0
    l=len(words)
    str1=""
    while i<l:
        if i<l-1:
            str1+=words[i] + " "
        else: 
            str1+=words[i]
        i+=1
        
    return str1
#alternate solution 4
def smash(words):
    # Begin here
    result = ""
    for i in range(len(words)):
        if i != len(words)-1:
            result = result + words[i] + " "
        else:
            result = result + words[i]
    return result             
#alternate solution 5