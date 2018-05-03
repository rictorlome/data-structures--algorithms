## Given two strings x,y
## What is cheapest way to convert x into y
## Allow character edits (insert,delete,replace)

## Longest common subsequence
## Example: hieroglyphology .. michaelangelo

## Subproblem:
## Edit distance on x[i:] & y[j:] for all i,j
## Num of Subproblems = O(|x| * |y|)

## Guess 1 of 3 possibilities:
## replace x[i] => y[j]
## insert y[j]
## delete x[i]

## Recurrence
## D(i,j) = min(
##              cost of replace x[i] =>y[j] + DP(i+1,j+1),
##              cost of insert y[j] + DP(i,j+1),
##              cost of delete x[i] + DP(i+1,j)
##              )

## Topological order: from end to beginning. Small suffixes to large suffixes.
## O(1) per subproblem. Time = O(|x| * |y|)

## Arbitrary cost function
def cost(type,char1,char2):
    if type is 'delete' or 'add': return 1
    if type is 'replace':
        if char1 is char2: return 0
        return 2

## Below is the prefix variation, not the suffix
def edit_distance(x,y):
    n, m = len(x) + 1, len(y) + 1
    memo_table = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i is 0: memo_table[i][j] = j
            elif j is 0: memo_table[i][j] = i
            else: memo_table[i][j] = min(
                memo_table[i-1][j-1] + cost('replace', x[j-1], y[i-1]),
                memo_table[i][j-1] + cost('insert', y[i-1], None),
                memo_table[i-1][j] + cost('delete', x[j-1], None)
            )
    return memo_table[m-1][n-1]
