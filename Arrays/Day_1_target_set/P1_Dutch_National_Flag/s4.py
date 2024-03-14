"""
Previous solution used teo passes to solve the problem

Is it possible to do this in one pass??
Time - O(n)
Space - O(1)
Tradeoff - Trickier


Approach 1  - Perform the operations in 1 pass

Maintain four subarrays -
1. Bottom - elements less than pivot
2. Middle - elements equal to pivot
3. Unclassified
4. Top - elements more than pivot

Initial status
All elements are unclassified
small = 0
equal = 0
larger = len(A)

Unclassified is between equal[0] to larger[len(A)]

while equal<larger
    check if element at index equal is smaller than pivot
        We found our first element belonging to smaller subarray, move it to the small position and
            increment small indicating it is ready to accept next smaller element
            increment equal indicating we have processed one unclassified element and ready to process next element
            in the unclassified subarray
    check if element at index equal is equal to pivot
        We found an element which is at its right position, move to process next element
        increment equal index
    Check if element at index equal is greater than pivot
        We found an element which needs to be moved to next larger subarray
        decrement larger index
        put the element at this index
Repeat
"""

def dutch_national_flag_partition(A,pivot_idx):
    pivot = A[pivot_idx]
    small, equal = 0,0
    large = len(A)
    while equal<large:
        if A[equal]<pivot:
            A[small],A[equal]=A[equal],A[small]
            small+=1
            equal+=1
        elif A[equal]==pivot:
            equal+=1
        elif A[equal]>pivot:
            large-=1
            A[equal],A[large]=A[large],A[equal]
    return A

print(dutch_national_flag_partition([0,1,2,0,2,1,1],0))

# Complexity
# Time - O(n)
# Space - O(1)
