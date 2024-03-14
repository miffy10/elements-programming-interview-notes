"""
Q. Buy and sell a stock once

EXPLORE: Problem is to buy and sell a stock exactly once which maximizes the profit
Examples
Input - [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
Max profit 30 would be made when buy is done at 260 and sell at 290


BRAINSTORM
Approach 1 - Check each combination of buy and sell (i,j) j>i, Keep track of the max profit made
Time - O(n^2)
Space - O(1)

Approach 2 - Divide and conquer. We can divide the input space into halves and find the max solution at each section
and combine the solutions.

Edge case 1 - Best solution occurs when buy and sell appears in different sections. In this case we have to find the min and max in individual sections.
Edge case 2 - Empty array
Edge case 3 -  1 element

Time - O(nlogn)

Approach 3 - Traverse through array and keep track of the min price seen so far and max profit made so far
Time - O(n)
Space - O(1)


PLAN

Initialize variable min_price_so_far to inf
Initialize variable max_profit_so_far to 0
Iterate over prices array
    compare current price and min_price_so_far and get min price and update the min_price_so_far
    get the current profit from min_price_so_far and current price and update the max_profit_so_far
return max_profit_so_far
"""

def get_max_profit(prices):
    min_price_so_far, max_profit_so_far = float("inf"),0
    for cur_price in prices:
        min_price_so_far=min(min_price_so_far,cur_price)
        cur_profit = cur_price-min_price_so_far
        max_profit_so_far=max(max_profit_so_far,cur_profit)
    return max_profit_so_far

print(get_max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

