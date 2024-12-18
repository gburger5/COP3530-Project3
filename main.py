import time

# Merge sort 
def merge_sort(data):
    # Base case
    if len(data) <= 1:
        return data
    # Split data in half
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Recursive sort left and right
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the halves
    return merge(left, right)

def merge(left, right):
    return_list = []
    index_left = 0
    index_right = 0

    # Iterate through left and right add smaller element to return
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            return_list.append(left[index_left])
            index_left += 1
        else:
            return_list.append(right[index_right])
            index_right += 1

    # Add all remaining elements
    while index_left < len(left):
        return_list.append(left[index_left])
        index_left += 1

    while index_right < len(right):
        return_list.append(right[index_right])
        index_right += 1

    return return_list


# Quick Sort
def quick_sort(data):
    # Base case
    if len(data) <= 1:
        return data

    # Choose a pivot (the middle value) to sort all other values around
    pivot = data[len(data) // 2]
    lesser = []
    middle = []
    greater = []

    for item in data:

        if item < pivot:
            lesser.append(item)

        elif item == pivot:
            middle.append(item)

        else:
            greater.append(item)

    # Recursive call outside of loop
    return quick_sort(lesser) + middle + quick_sort(greater)
            

  # Heap Sort requires that the strcuture of the heap remains in tact with each sorted node
  # A heapify function is required to maintain the strcuture of the heap
def heapify(data, n, i):

    # Create heap (max heap in this case) with the largest node being the root initially
    largest = i

    # Initialize left and right children (heap represented as an array)
    left = 2 * i + 1
    right = 2 * i + 2 

    # Check if there is a left child and if so, if it is greater than root
    if left < n and data[left] > data[largest]:
        largest = left

    # Check if there is a right child and if so, if it is greater than largest
    if right < n and data[right] > data[largest]:
        largest = right

    # If largest is not root, continue heapifying
    if largest != i:
        # Swap necessary values
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heapsort(data):
    # After implementing heapify algorithm, we can now implement heapsort

    # Begin by using the length of the data array to build a max heap using heapify 
    n = len(data)

    for i in range(n // 2 -1, -1, -1):
        heapify(data, n, i)

    # Extract the root one by one as heapify swaps elements and changes it
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0)
    return data

def min_run(n):
    # Calculates the minimum run length.
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r
# Insertion Sort
def insertion_sort(arr):
  # Check if the input array is empty
  if not arr:
    return None
  # Loop through the array starting at the second element
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr[:i+1]

def tim_sort(data):
    # Sorts the array using Timsort.
    n = len(data)
    minrun = min_run(n)

    # Sort individual subarrays of size minrun
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(data[start:end+1])  # Using existing insertion_sort

    # Merge subarrays to produce sorted arrays
    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            merge(left, right)  # Using existing merge function
        size *= 2
    return data
