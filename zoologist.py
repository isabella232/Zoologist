from math import log
import csv

def assignRankings(pop_growths):
    animals = [
        "elephants",
        "pandas",
        "bears",
        "humans",
        "honeybadgers",
        "antelopes",
        "t-rex",
        "dodo",
        "snakes",
        "gazelles",
        "ants",
        "squirrels",
        "cows",
        "horses",
    ]

    # obtain values
    values = []
    for animal in animals:
        value = pop_growths[animal]
        values.append(value)

    # rank values descending order
    rankings = [] # key: rank, value: growth index
    while (not max(values) == -1):
        nextValue = max(values)
        index = values.index(nextValue) # find index
        values[index] = -1
        rankings.append(index)

    return rankings
        
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements ar5e already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
                
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        print(arr)

def read(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        return next(reader)

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
            print(arr)
  
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print(arr)
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
        
def main():
    n = 100000
    pop_growths = {
        "elephants"    : n**2,       # 0
        "pandas"       : log(n),     # 1
        "bears"        : n,          # 2
        "humans"       : 2**n,       # 3
        "honeybadgers" : n**3,       # 4
        "antelopes"    : 4*n,        # 5
        "t-rex"        : 1,          # 6
        "dodo"         : 10,         # 7
        "snakes"       : 4*n**3,     # 8
        "gazelles"     : n*log(n),   # 9
        "ants"         : n**n,       # 10
        "squirrels"    : n**2+n**3,  # 11
        "cows"         : n**4,       # 12
        "horses"       : n**4+n**5  # 13
    }

    ranks = assignRankings(pop_growths)

    print("BUBBLE SORT")
    bubbleSort(ranks.copy())
    print("INSERTION SORT")
    insertionSort(ranks.copy())
    print("QUICK SORT")
    quickSort(ranks.copy(), 0, 10)
main()
