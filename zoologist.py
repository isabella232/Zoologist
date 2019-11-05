from math import log
import csv

def assignRankings(pop_growths):
    
    # rank values descending order
    rankings = []
    while (not max(pop_growths) == -1):
        nextValue = max(pop_growths)
        index = pop_growths.index(nextValue) # find index
        rankings.append(index)
        pop_growths[index] = -1

    # get ascending order
    rankings.reverse()
    
    return rankings


def bubbleSort(arr):
    n = len(arr)
    print(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (arr[j] > arr[j+1]):
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


def selectionSort(arr):
    # Traverse through all array elements 
    for i in range(len(arr)): 
      
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)



def read(filename):
    with open(filename, 'r') as file:
        result = {}
        index = 0
        for line in file.read().split("\n"):
            noTabs = line.split("\t")
            lastElement = noTabs[len(noTabs) - 1]
            result[index] = lastElement
            index += 1

    print(result)
    return result

def main():
    n = 1
    pop_growths = [
        n**2,       # 0
        log(n),     # 1
        n,          # 2
        2**n,       # 3
        n**3,       # 4
        4*n,        # 5
        1,          # 6
        10,         # 7
        4*n**3,     # 8
        n*log(n),   # 9
        n**n,       # 10
        n**2+n**3,  # 11
        n**4,       # 12
        n**4+n**5   # 13
    ]

    animals = read("animalNames.txt") # animals = {index : animalName}
    ranks = assignRankings(pop_growths.copy()) # ranks = {index : rank}

    for i in range(len(ranks)):
        print(animals[ranks[i]])

    print("BUBBLE SORT")
    bubbleSort(ranks
               .copy())
    print("INSERTION SORT")
    insertionSort(ranks.copy())
    print("SELECTION SORT")
    selectionSort(ranks.copy())


main()
