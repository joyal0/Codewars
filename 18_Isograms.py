#ISOGRAMS
"""
DESCRIPTION:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
STRINGSFUNDAMENTALS"""
def is_isogram(string):
    #your code here
    str = ""
    for x in string:
        if x.upper() not in str:
            str += x.upper()
        else:
            return False
    return True

#outputs
"""
Time: 477ms Passed: 50Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (10 of 10 Assertions)
Completed in 0.16ms
Random tests
Testing for PEclXYn
Testing for KCJbxDzBMsDxnmBSJQJBJre
Testing for RxfIRAPweIIXSOGGyYRNgrJMWdXyXLxB
Testing for nqrBYQkyLtwPlQK
Testing for icbIoqQEekIeSRBgykTgJaPtiFIsETctifgo
Testing for oAUjRIfKiY
Testing for SLlrXDAt
Testing for hjVgBdzLjORNDBDvISAkKHOTIwkflOhRbVIhislhWLdxF
Testing for nRBzEWCmnkmXallmFEfq
Testing for XCBriiOWhUPEjjiAwlJcwIWiWKFoM
Testing for VqYkZmuSeQXGKnRaleDQLLsrDFt
Testing for KVYJoRiiEpKZVrzrzOsUmJTGoZcxdlV
Testing for nvBJvcsXFLjI
Testing for GhcHBYUpYeIqRkmD
Testing for YlsZkMjdLsVuGbhElnPxSBenlMFSIjMOU
Testing for vHlVEnrqpDMMET
Testing for kYmIeyESnTCiZpeeqkFYjUMGG
Testing for ShJuRKGYEsqCRHoyGCXMUOVNmLqrIVRHphPFoUe
Testing for pVKjsWNMgzhEiopaU
Testing for zUoSRL
Testing for yMOEwjSJpFnwGaVhbMfNd
Testing for UNvEOJcniTOCUUpwjylfz
Testing for ICvWeBuchrD
Testing for tskqSYhlSIgXrJePjWIGnKqztHRHBCn
Testing for LcThyJEMinTkYGFUsHZ
Testing for qoMCmIFYmDCNfWhGsPUnpU
Testing for acDOhkb
Testing for MSpuBYGjGTgjsr
Testing for OAirYhiBMXFXGHJlWQfBsKVokVASvpsxwjYPZNmi
Testing for cnpAJI
Testing for enKPhtEkqcweYRUcYjfuLWOlnVMVjGVtp
Testing for kPlgyFSmuXPzvqU
Testing for oSyjVFKqGjFgDyuDofEkDSO
Testing for ZVUhGqApQtLIFEYdEtrvPDG
Testing for IOtJg
Testing for fsdHITAwYHZQRTfZKOcGCJEloQkeTkOqvknCjrBHXDjJk
Testing for ObBrhPwfmUFkIxQaeRqeHQBuprR
Testing for RFaOUHQkOSLphQ
Testing for evzUWbAvvJhQJyajW
Testing for dZIRKfHeYMZSlLKgokfqFoi
Completed in 3.85ms
You have passed all of the tests! :)"""

#alternate solution 1
def is_isogram(string):
    return len(string) == len(set(string.lower()))

#alternate solution 2
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True

#alternate solution 3
def is_isogram(string): 
    return len(set(string.lower())) == len(string)

#alternate solution 5
def is_isogram(string):
    s = set(string.lower()) 
    if len(s) == len(string): 
        return True
    return False