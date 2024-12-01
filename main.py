import time
'''
To-Do:
Build Out QuickSort, Heap Sort
''' 

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
    pass

# Selection Sort
def selection_sort(data):

    for i in range(len(data)):
        # Find the index of the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        data[i], data[min_index] = data[min_index], data[i]

    return data

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
  return arr