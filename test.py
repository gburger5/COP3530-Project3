# Test merge and quicksort
from main import mergesort, merge, quicksort
'''
To-Do:
Test each and make sure they pass for quicksort
'''
testList = [2, 6, 8, 5] # Even Number
sortedList = mergesort(testList)

''' for item in sortedList:
    print(item) # Expected 2 5 6 8, MergeSort Passed'''

testList_2 = [2, 3, 4, 5, 6, 7] # Odd Number
sortedist_2 = mergesort(testList_2)

'''for item in sortedist_2:
    print(item) # Expected 2 3 4 5 6 7: MergeSort Passed'''

testList_3 = [5, 4, 3, 2, 1, 6, 8, 10, 12, 25] 
sortedList_3 = mergesort(testList_3)

'''for item in sortedList_3:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: MergeSort, Passed'''

