###Reaching permutation

'''given an array of N integers, your task is to transform this array into a permutation of the first N positive intefers. A permutation of size N is an arrangement of numbers such that each numer from 1 to n appears exactly once.
in one operation, you canc increase or decrease any element of the array by 1

the challenge is to figure out the smalles number operations required to convert the given array

examples:

1. Input N = [3,2,1,4]
output: 0
explanation: no operation needed, already a permutation

2.Input N = [4,1,4,2]
output: 1
explanation: decrease one '4' to '3' to form the permutation [4,1,3,2]

contraints:
-the integers in the array N will be equal or bigger than 1
-the size of the array N can range from 1 to 10^5'''








from typing import List

def min_operations_to_permutation(arr: List[int]) -> int:
    #Solution
    n = len(arr)
     # Create a set to keep track of unique elements in the array
    unique_elements = set()

    # Count the number of elements that need to be changed
    count = 0
    
    for i in range(n):
        # Calculate the correct position for the current element
        correct_position = i + 1
        
        # Calculate the absolute difference between the current element and its correct position
        diff = abs(arr[i] - correct_position)
        
        # If the current element is not in the unique_elements set and the difference is not zero,
        # it means this element needs to be changed to its correct position
        if arr[i] not in unique_elements and diff != 0:
            count += 1
            unique_elements.add(arr[i])
    
    return count




#readme
#DO NOT CHANGE THE CODE BELOW

if __name__ == '__main__':
    line=input()
    k = [int(i) for i in line.strip().split()]
    print(min_operations_to_permutation(k))