#EVEN OR ODD
"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

MATHEMATICSFUNDAMENTALS"""
def even_or_odd(number):
    return "Even" if number%2 == 0 else "Odd"
#OUTPUTS
"""
Time: 520ms Passed: 109Failed: 0
Test Results:
Submission tests
Positive odd numbers
 (2 of 2 Assertions)
Positive even numbers
 (2 of 2 Assertions)
Negative odd numbers
 (2 of 2 Assertions)
Negative even numbers
 (2 of 2 Assertions)
Zero
Random Tests
 (100 of 100 Assertions)
Completed in 1.23ms
You have passed all of the tests! :)"""
#alternate solution 1
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
#alternate solution 2
"""
    # function takes single parameter
    def check_even_or_odd(number):
        # check if the number is an integer
        if type(number) != int:
            return 'Invalid input'
        return even_or_odd(number) # return the function to check for even or odd
        
    # function to check odd or even
    def even_or_odd(number):
        if number % 2 == 0:
            # if value of number is integer returns even
            return 'Even'
        # else it should return odd
        return 'Odd'
"""
#alternate solution 3
def even_or_odd(number):
    even_or_odd = {0: "Even", 1: "Odd"}
    return even_or_odd[number % 2]