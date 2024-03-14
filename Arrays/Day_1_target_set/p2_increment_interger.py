"""
Input = Array of digits encoding a non-negative decimal integer D
Task = Update Array to represent D+1
Output = Array of digits encoding a non-negative decimal integer D+1
Example:
    Input = [1,2,9]
    Output= [1,3,0]

Explore:
Case 1: 128 -> 129
Case 2: 129 -> 130 (Carry over)
Case 3:  99 -> 100 (two digit -> three digit)

Brainstorm:
Bruteforce - Convert array to integer, add 1, convert back to array
Issue - Potential Integer Overflow could occur

Approach 2 -
1. Perform grade-school algorithm : adding digits starting from least significant digit
2. Propagate carries
99->100, We will have to change the array from 2 elements to 3 elements

Time - O(n)
Space - O(1)
Plan:
Add one to the least significant digit.
Iterate from len(A) to 1

    Check if num is 10
        True - Update current digit to 0
               Add 1 to previous digit
    else:
        break
if A[0]==10
    A[0]
    A.append(0)
return A
"""

# Implement

def plus_one(A):
    A[-1]+=1
    for i in reversed(range(1,len(A))):
        if A[i]==10:
            A[i]=0
            A[i-1]+=1
        else:
            break
    if A[0]==10:
        A[0]=1
        A.append(0)
    return A

# Verify

print(plus_one([1,2,9]))
print(plus_one([1,2,8]))
print(plus_one([9,9]))
