"""
Q. Write a program which takes an array of n integers, where A[i] denotes the maximum you can advance from index i,
 and returns whether it is possible to advance to the last index starting from the beginning of the array.


Explore

Input - Array of n integers
Output - Boolean possible to reach the end of the array
Task - A[i] denotes the maximum you can jump from index i


Brainstorm

Greedy approach

We can apply a greedy approach and try to make furthest jump whenever possible.

Start from the beginning,
0 - A[0] -> current furthest jump. If this jump is greater than or equal to last index. Return True. Else continue
1 - A[1] -> If current furthest jump equals index. Check can help jump further?? No, return False. Yes, update current furthest jump. If this jump is greater than or equal to last index. Return True. Else continue
2 - A[2] -> If current furthest jump equals index. Check can help jump further?? No, return False. Yes, update current furthest jump. If this jump is greater than or equal to last index. Return True. Else continue
.
.
.
n-1 - A[n-1] ->


Time - O(n)
Space - O(1)

PLAN

curr_furthest_jump = 0
Iterate over indices of Array - 0 to len(Array)-1
    jumps  = index + Array[index]
    if jumps greater than curr_furthest_jump or curr_furthest_jump == index,
        update curr_furthest_jump to jumps
    if curr_furthest_jump equals last index, return True

"""

#Implement

def jumping_game(arr):
    curr_furthest_jump = 0
    last_index = len(arr)-1
    # for idx in range(len(arr)):
    #     if idx > curr_furthest_jump:
    #         return False
    #     curr_furthest_jump = max(curr_furthest_jump,idx + arr[idx])
    #     if curr_furthest_jump >= last_index:
    #         return True

    idx=0
    while idx<=curr_furthest_jump and curr_furthest_jump<last_index:
        curr_furthest_jump = max(curr_furthest_jump, idx + arr[idx])
        idx+=1
    return curr_furthest_jump>=last_index

# Verify
print(jumping_game([3,3,1,0,2,0,1]))
print(jumping_game([3,2,0,0,2,0,1]))