"""
INPUT : Two arrays representing integers
TASK : Perform multiplication of two arrays
OUTPUT: Integer representing their product

Example:
    Array1 = [1,9,3,7,0,7,7,2,1] -> 193707721
    Array2 = [-7,6,1,8,3,8,2,5,7,2,8,7] -> -761838257287
    Product = [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,7] -> -14757395258967641297

Brainstorm

Approach 1
Bruteforce - convert to integers and multiply the numbers and convert back to array
Issue - Potential integer overflow

Approach 2
Grade-school multiplication
Note - Number of digits required for the product is at most n+m for n and m digit operands,
       we use an array of size n+m for the result
123x987

123x7 = 861
123x80 = 9840
123x900 = 10701

Add = 121401

PLAN
Input - num1,num2
result = array of size len(num1)+len(num2)
Run 2 loops starting with least significant digit of num1 and num2
for loop i len(num1)-1 to 0
    for loop j len(num2)-1 to 0
        result[i+j+] = num1[i]*num2[j]
        result[i+j]+=result[i+j]//10
        result[i+j]%=10
"""

result = [0]*10
print(result)