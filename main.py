import time
'''
To-Do:
Build Out QuickSort
'''


''' Commented out so it doesn't run during tests.
with open('GRU_Customer_Electric_Consumption_2012-2022_20241126.csv', 'r') as file: # Takes in each KWH measurement from ~12mil rows of data
    data = []
    next(file) # Skips header
    for line in file:
        row = line.split(',')
        kwh = float(row[6])
        data.append(kwh)
'''
    

# Merge sort 
def mergesort(data):
    # Base case
    if len(data) <= 1:
        return data
    # Split data in half
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Recursive sort left and right
    left = mergesort(left)
    right = mergesort(right)

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
def quicksort(data):
    pass


if __name__ == "__main__":
    # Get times for both merge and quick sort to compare on frontend
    start_time = time.time()
    mergesort_data = mergesort(data)
    mergesort_time = time.time() - start_time

    start_time = time.time()
    quicksort_data = quicksort(data)
    quicksort_time = time.time() - start_time

    # Some type of frontend function to visualize the times it took/data etc