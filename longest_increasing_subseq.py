# The longest increasing subsequence problem.
# Example input: arr = [8,3,5,2,4,9,7,11]
# Answer: 4, because 3-5-9-11 or 3-5-7-11 or  2-4-9-11

# What is the subproblem?
# Start at number i, what is the longest subsequence from here?
# Solve the problem from the end of the array moving to the front.
# If the current element (i) < another element further on (j)
# Add a new possible longest subsequence from i which is dp[j]+1
# Take the max of all the choices.

# After this loop, the memo table will contain the longest increasing subsequences for each i
# Take the max of the memo table.

# The runtime is O(n^2) because there is O(n) loop nested in an O(n) loop, and
# The operations in the inner loop are all constant time.

def longest_increasing_subsq(arr):
    n = len(arr)
    dp = [0 for _ in range(n)]
    ## interate backwards through array to zero index.
    for i in range(n-1, -1, -1):
        cur_max = 1
        for j in range(i+1, n):
            ## this choice is only possible if arr[j] > arr[i]
            possible_choice = dp[j] + 1
            if arr[j] > arr[i] and possible_choice > cur_max:
                cur_max = possible_choice
        dp[i] = cur_max
    return max(dp)

example = [15,27,14,38,26,55,46,65,85]
