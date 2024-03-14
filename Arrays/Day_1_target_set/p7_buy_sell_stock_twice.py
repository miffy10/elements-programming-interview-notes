"""
Q. Buy and sell a stock twice

Write a program that computes the maximum profit that can be made by buying and selling a share at most twice.
The second buy must be made on another date after the first sale.

EXPLORE -
Can perform 2 transactions (buy and sell) at most.
Second buy must be made after first buy, can't be on same dates

Example
Input - [12,11,13,9,12,8,14,13,15]
Output - 10

Buy, Sell, Profit - 9,12,3
Buy, Sell, Profit - 8,13,7
Total Profit -  10


BRAINSTORM

Approach 1 -
Bruteforce solution
Explore every combination (i,j,x,y)
i-1st buy,j-1st sell,x-2nd buy,y-2nd sell

Time - O(n^4)


Approach 2 -
Divide and conquer
Divide the input space and perform the search in each smaller input
Time - O(n^2logn) ??

Approach 3 -
Take advantage of previous computations
Rational

If Max profit is A[0,j] where j -> [1,n-1]
Perform reverse iteration to find A[j,n-1], j [1,n-1] and the max profit


Forward pass - min price seen so far, max profit seen so far
Keep track of the min price seen so far to perform buy and find the sell price which can produce max profit
Backward pass - max price seen so far, max profit seen so far
Keep track of the max price seen so far to perform sell and find the buy price which can produce max profit

We have 2 lists -
List1 - max profit optimized for min buy
List 2 - max Profit optimized for max sell

Compute the max profit by combination of the results from forward and backward pass
Since the 2nd buy can happen only after the first sell
Combination should be - M[i] = F[i-1]+B[i]
where F[-1] is initialized to 0
Time - O(n)
Space - O(n)

PLAN
Initialize variable min_price_seen_so_far to inf
Initialize list first_buy_profit to 0 for len(prices)+1
Iterate over prices array
    compare current price and min_price_so_far and get min price and update the min_price_so_far
    get the current profit from min_price_so_far and current price and update the first_buy_profit

Initialize variable max_price_so_far to -inf
Initialize list second_buy_profit to 0 for len(prices)+1
Iterate over prices array from reverse
    compare current price and max_price_so_far and get max price and update the mqx_price_so_far
    get the current profit from max_price_so_far and current price and update the second_buy_profit

Add profits from  first_buy_profit and second_buy_profit and get the max profit

return max profit
"""

def get_max_profit_twice(prices):
    len_prices = len(prices)
    min_price_so_far = float('inf')
    max_profit_so_far = 0.0
    first_buy_profit = [0]*(len_prices+1)
    for idx,cur_price in enumerate(prices):
        min_price_so_far = min(cur_price, min_price_so_far)
        cur_profit = cur_price-min_price_so_far
        max_profit_so_far = max(cur_profit,max_profit_so_far)
        first_buy_profit[idx+1]=max_profit_so_far

    max_price_so_far = float('-inf')
    max_profit_so_far = 0.0
    second_buy_profit = [0] * (len_prices + 1)
    for idx, cur_price in reversed(list(enumerate(prices))):
        max_price_so_far = max(cur_price, max_price_so_far)
        cur_profit = max_price_so_far-cur_price
        max_profit_so_far = max(cur_profit, max_profit_so_far)
        second_buy_profit[idx] = max_profit_so_far

    max_profit = 0.0
    for i in range(len(first_buy_profit)):
        max_profit=max(max_profit, (first_buy_profit[i]+second_buy_profit[i]))
    return max_profit

print(get_max_profit_twice([12,11,13,9,12,8,14,13,15]))