# Test merge and quicksort
from main import merge_sort, quick_sort, heapsort, tim_sort
'''
To-Do:
Test each and make sure they pass for quicksort

Simplify this code to make it easier to read, especially with more sorting algorithms
'''
# Pretty sure these all work now, updated some things in the main.py file
testList = [2, 6, 8, 5] # Even Number

sortedList = merge_sort(testList)
sortedList_4 = quick_sort(testList)
sortedList_13 = heapsort(testList)
sortedList_16 = tim_sort(testList)

print("MergeSort Passed")
for item in sortedList:
    print(item) # Expected 2 5 6 8, MergeSort Passed

print("QuickSort Passed")
for item in sortedList_4:
    print(item) # Expected 2 5 6 8, QuickSort Passed

print("HeapSort Passed")
for item in sortedList_13:
    print(item) # Expected 2 5 6 8, HeapSort Passed

print("TimSort Passed")
for item in sortedList_16:
    print(item) # Expected 2 5 6 8, TimSort Passed

testList_2 = [2, 3, 4, 5, 6, 7] # Odd Number
sortedist_2 = merge_sort(testList_2)
sortedList_5 = quick_sort(testList_2)
sortedList_14 = heapsort(testList_2)
sortedList_17 = tim_sort(testList_2)

print("MergeSort Passed")
for item in sortedist_2:
    print(item) # Expected 2 3 4 5 6 7: MergeSort Passed

for item in sortedList_14:
    print(item) # Expected 2 3 4 5 6 7: HeapSort Passed
print("TimSort Passed")

for item in sortedList_17:
    print(item) # Expected 2 3 4 5 6 7: TimSort Passed

testList_3 = [5, 4, 3, 2, 1, 6, 8, 10, 12, 25] 
sortedList_3 = merge_sort(testList_3)
sortedList_6 = quick_sort(testList_3)
sortedList_15 = heapsort(testList_3)
sortedList_18 = tim_sort(testList_3)

for item in sortedList_3:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: MergeSort, Passed
 
for item in sortedList_6:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: QuickSort, Passed
    
for item in sortedList_15:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: HeapSort, Passed

for item in sortedList_18:
    print(item) # Expected 1 2 3 4 5 6 8 10 12 25: TimSort, Passed