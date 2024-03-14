"""
Approach 1

Brainstorm


Input - Array of integers, Pivot index

Form three list

List 1 - Elements less than the pivot
List 2 - Elements equal to the pivot
List 3 - Elements greater than the pivot

Write each list into back into the input list

Complexity
Time - O(n)
Space - O(n)

PLAN

Initialize variable pivot with element at the pivot index in the array
Initialise three empty arrays - list_1, list_2, list_3
Iterate through input array A
    if current element is smaller than the pivot, add it to the list_1
    else if current element is equal to the pivot, add it to the list_2
    else add to the current element to the list_3
Copy each elements from the 3 lists to the input array A in the order list_1, list_2, list_3

return array A
"""
# Implement
def dutch_national_flag_partition(A,pivot_index):
    pivot = A[pivot_index]
    list1,list2,list3=[],[],[]
    for i in range(len(A)):
        if A[i]<pivot:
            list1.append(A[i])
        elif A[i]==pivot:
            list2.append(A[i])
        else:
            list3.append(A[i])
    a_idx=0
    for num in list1:
        if a_idx<len(A):
            A[a_idx]=num
            a_idx+=1
    for num in list2:
        if a_idx < len(A):
            A[a_idx]=num
            a_idx+=1
    for num in list3:
        if a_idx < len(A):
            A[a_idx]=num
            a_idx+=1
    return A

# Verify

print(dutch_national_flag_partition([0,1,2,0,2,1,1],2))