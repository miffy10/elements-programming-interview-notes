"""
Approach 3
--
Previous solution
Time complexity - O(n^2)
Space complexity - O(1)

Trying to reduce the time complexity of previous solution
We have 2 loops which is causing the time complexity to be n^2

Can we reduce the two loops to one loop ???

Loop 1 is being maintained to fill smaller array/build the smaller array

Each time a position in smaller array is filled, check is perfomed starting the next position in the array

no matter how far the previous check that moved

which is not needed

For one loop
Initialise small = 0

start from 0 to end of the array tracked by variable i
    check if num at ith position is smaller than pivot.
    If yes, add the num to position small, increment small
    repear the check

Initialize large = len(A)-1

start  i from len(A)-1 to 0
    num at ith position is smaller than pivot
        break - There is nothing to do
    check if num at position ith is greater than pivot
    If yes, add the  num to position large, decrement large


This code will run in O(n) time
Space complexity is O(1)
It requires two passes
"""

def dutch_national_flag_partition(A,pivot_idx):
    pivot = A[pivot_idx]
    small = 0
    for i in range(len(A)):
        if A[i]<pivot:
            A[i],A[small] = A[small],A[i]
            small+=1
    larger = len(A)-1
    for i in reversed(range(len(A))):
        if A[i]<pivot:
            break
        if A[i]>pivot:
            A[i],A[larger]=A[larger],A[i]
            larger-=1
    return A
# Verify
# Time complexity is  O(n^2)

print(dutch_national_flag_partition([0,1,2,0,2,1,1],2))



