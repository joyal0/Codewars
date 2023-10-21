#CALCULATE BMI
"""
DESCRIPTION:
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

FUNDAMENTALS"""
def bmi(weight, height):
    #your code here
    res = weight / height**2
    if res<=18.5:
        return "Underweight"
    elif res<=25:
        return "Normal"
    elif res<=30:
        return "Overweight"
    elif res>30:
        return "Obese"
#OUTPUTS
"""
Time: 474ms Passed: 45Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (5 of 5 Assertions)
Completed in 0.11ms
Random tests
Testing for 77 and 1.86
Testing for 80 and 1.72
Testing for 103 and 1.7
Testing for 90 and 1.73
Testing for 149 and 1.65
Testing for 50 and 2.07
Testing for 85 and 1.41
Testing for 112 and 1.16
Testing for 120 and 1.24
Testing for 47 and 1.66
Testing for 129 and 1.73
Testing for 87 and 1.98
Testing for 137 and 2.01
Testing for 143 and 1.46
Testing for 115 and 1.1
Testing for 79 and 1.6
Testing for 53 and 1.33
Testing for 116 and 1.12
Testing for 74 and 1.79
Testing for 33 and 1.61
Testing for 118 and 1.38
Testing for 96 and 1.75
Testing for 37 and 1.3
Testing for 144 and 2.03
Testing for 39 and 2.08
Testing for 57 and 1.31
Testing for 38 and 1.33
Testing for 111 and 1.21
Testing for 83 and 1.8
Testing for 99 and 1.28
Testing for 56 and 1.51
Testing for 87 and 1.41
Testing for 119 and 2.0
Testing for 102 and 1.42
Testing for 49 and 1.75
Testing for 114 and 1.5
Testing for 81 and 1.95
Testing for 48 and 1.89
Testing for 104 and 1.63
Testing for 127 and 1.51
Completed in 3.07ms
You have passed all of the tests! :)"""
#alternate solution 1
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
#alternative solution 2
def bmi(weight, height):
    bmi = weight / height ** 2
    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"
#alternate solution 3
def bmi(weight, height):
    index = weight/height/height
    return "Underweight" if index <= 18.5 else "Normal" if index <= 25.0 else\
      "Overweight" if index <= 30.0 else "Obese"
#alternate solution 4
def bmi(weight, height):
    result = weight / height / height
    return "Underweight Normal Overweight Obese".split()[
            (result > 18.5) +
            (result > 25.0) +
            (result > 30.0)]
#alternative solution 5
def bmi(weight, height):
    ratio = weight / height ** 2
    
    if ratio > 18.5:
        if ratio > 25:
            if ratio > 30:
                return 'Obese'
            return 'Overweight'
        return 'Normal'
    return 'Underweight'