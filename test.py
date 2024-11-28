# Test merge and quicksort
from main import mergesort, merge, quicksort, selection_sort, insertion_sort
'''
To-Do:
Test each and make sure they pass for quicksort

Simplify this code to make it easier to read, especially with more sorting algorithms
'''
testList = [2, 6, 8, 5] # Even Number
sortedList = mergesort(testList)
sortedList_4 = quicksort(testList)
sortedList_7 = selection_sort(testList)
sortedList_10 = insertion_sort(testList)

''' for item in sortedList:
    print(item) # Expected 2 5 6 8, MergeSort Passed'''
'''
for item in sortedList_4:
    print(item) # Expected 2 5 6 8, QuickSort Passed'''
'''
for item in sortedList_7:
    print(item) # Expected 2 5 6 8, SelectionSort Passed'''
'''
for item in sortedList_10:
    print(item) # Expected 2 5 6 8, InsertionSort Passed'''

testList_2 = [2, 3, 4, 5, 6, 7] # Odd Number
sortedist_2 = mergesort(testList_2)
sortedList_5 = quicksort(testList_2)
sortedList_8 = selection_sort(testList_2)
sortedList_11 = insertion_sort(testList_2)

'''for item in sortedist_2:
    print(item) # Expected 2 3 4 5 6 7: MergeSort Passed'''
'''
for item in sortedList_5:
    print(item) # Expected 2 3 4 5 6 7: QuickSort Passed'''
'''
for item in sortedList_8:
    print(item) # Expected 2 3 4 5 6 7: SelectionSort Passed'''
'''
for item in sortedList_11:
    print(item) # Expected 2 3 4 5 6 7: InsertionSort Passed'''

testList_3 = [5, 4, 3, 2, 1, 6, 8, 10, 12, 25] 
sortedList_3 = mergesort(testList_3)
sortedList_6 = quicksort(testList_3)
sortedList_9 = selection_sort(testList_3)
sortedList_12 = insertion_sort(testList_3)

'''for item in sortedList_3:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: MergeSort, Passed'''
''' 
for item in sortedList_6:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: QuickSort, Passed'''
'''
for item in sortedList_9:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: SelectionSort, Passed'''
'''
for item in sortedList_12:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: InsertionSort, Passed'''