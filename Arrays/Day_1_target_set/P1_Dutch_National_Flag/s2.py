"""
Approach 2

Trying to reduce the space complexity from O(n) to O(1)

Iterate through the array and move nums smaller than the pivot to the smaller subarray
Iterate through the array and move nums greater than the pivot to the larger subarray

Iteration 1 - Builds the smaller subarray
Index i tracks the smaller subarray
Initialize i to the 0th index and go till the end of the array
Find the num which can take the first place in the smaller subarray which is held by i variable

Start a loop tracked by variable j going from i+1 to the end of the array.
    Check if num at jth index is smaller than the pivot,
    if yes put this element at the ith index which is building the smaller array
    At this point break as we have found the num for ith position
increment the value at i, which means now we want num in the second position of the smaller array
start a loop again tracked by j and initialized to i+1 and check if the num is smaller the pivot,
If yes, we have found our 2nd num, put that in the location of i which is pointing to the second position.

Continue this until we reach the end of the array

At the end of this, we would have completely built a smaller subarray towards the left of the original subarray.
It's time to build the subarray with nums larger than the pivot

Instead of starting from the end and keeping track of the elements.
Reverse the Array and access the nums

Iteration 2 - Builds the larger subarray

Index i track the larger subarray

Reverse the array and Initialize i to the 0th the index and go till the end of the array
We have already build the smaller array, so no need to go till the end,
 stop when we find a num smaller than the pivot

Reverse the array and start to iterate
i variable is going to track the larger subarray one num at a time from back.
We will first try to find a num which is suitable for ith position i.e last position in the array

We will find the num suitable for last position by tracking with variable j
j starts from the end
check if the last num is greater then pivot  if yes put it in the last position
and break go to the next num

THis code is not readable. Can you make it readable/


PLAN:

INPUT - Array of n nums and pivot index
OUTPUT - Array of nums with partitions

We are creating the partitions in place and preventing the need of extra space

Build smaller subarray

Iterate over 0 to length of the array using i
    Iterate over i+1 to length of the array
        check if num at j is smaller than pivot
            if True
                swap num at ith index and num at jth index
                break
Build Larger Subarray

Iterate over length of the array upto 0 using i
    if num at ith element is smaller than pivot stop.
    Iterate over i upto 0 using j
        check if num at j is greater then pivot
        if true
            swap num at ith index and num at jth index
            break

return Array
"""

def dutch_national_flag_partition(A,pivot_idx):
    pivot = A[pivot_idx]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j]<pivot:
                A[i],A[j]=A[j],A[i]
                break

    for i in reversed(range(len(A))):
        if A[j]<pivot:
            break
        for j in reversed(range(i)):
            if A[j]>pivot:
                A[i], A[j] = A[j], A[i]
                break
    return A
# Verify
# Time complexity is  O(n^2)

print(dutch_national_flag_partition([0,1,2,0,2,1,1],2))



