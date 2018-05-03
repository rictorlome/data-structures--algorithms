import sys
# Params:
# List of n items - each with integer size, and some value
# Knapsack of size S
# Problem: maximize sum of values of subset of items of total size <= S

# Subproblem = suffix [i:] of items, and X <= S (remaining capacity)
# Guessing: is item i in subset or not.
# Number of subproblems is O(n * S). Number of possible states: one weight <= S per item.
# There are n decisions: D_i, take item i or not?

# DP(i,s) = Max(
#            DP(i+1,x),
#            DP(i+1,x-size(i)) + val(i)
#           )

def knapsack(items,s):
    n = len(items)
    memo_table = [[0 if col is n else None for col in range(n+1)] for _ in range(s+1)]
    ## Outer loop is through items:
    for j in range(n-1,-1,-1):
        ## Inner loop is through weights:
        for i in range(s,-1,-1):
            item = items[j]
            memo_table[i][j] = max(
                memo_table[i][j+1],
                worth(item) + memo_table[i-weight(item)][j+1] if i >= weight(item) else -sys.maxsize
            )
    return memo_table[s][0]

# Example from Ocw 6.006 R21:
items = ['statue','ball','fountainpen']
s = 5
def weight(item):
    if item is 'statue': return 4
    if item is 'ball': return 2
    if item is 'fountainpen': return 3

def worth(item):
    if item is 'statue': return 10
    if item is 'ball': return 4
    if item is 'fountainpen': return 7
