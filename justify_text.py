import sys
# split text into "good" lines
# text is a list of words
# badness(i,j) how bad it is to use words[i:j] as a line
# badness = infinity if the words don't fit. ie, if total length of word > length of line.
#            otherwise it's (pagewidth - totalwidth(words plus spaces)) ^ 3
# problem: minimize sum of badness of lines.

# 1. define subproblem. after the first guess, make a problem of the same type.
# 1... subproblems are suffixes: words[i:]
# 1... number of subproblems is n. only n choices

# 2. where to start 2nd line.
# 2... number of choices of a guess is <= n - i = O(n)

# 3. recurrence. DP(i)
# 3... this is a for loop, for j in range(i+1,n+1). anywhere from the 1st word, to the last (no 2nd line)
# 3... DP(j), the cost of the rest of the problem.
# 3... so DP(i) = MIN(    DP(J) + badness(i,j),
#                       for j in range(i+1,n+1)
#                   )
# 3... Basecase: DP(N) = 0, blank line is free.

# 4. What is topological order of this problem? We have to do it from the Right End back to Beginning.
# 4... top.order i = n, n-1, ... , 0

# 5. Runtime O(n^2).
# 5... Order N work per choice. Order N choices.
# 5... This returns the cost of the solution. Total min badness.
# 5... Parent pointers help in actually splitting the text. Remember which guess was best.
# 5... Parent[i] is a j value.
# 5... We start at 0 because we know that 0 starts a line. So parent[0] gives us best nextline.

def badness(i,j,words,width):
    line = " ".join(words[i:j])
    if (len(line) > width):
        return sys.maxsize
    else:
        return (width-len(line))**3

def text_justification(words, n, width, i):
    if i is n:
        return 0
    return min([text_justification(words,n,width,j) + badness(i,j,words,width) for j in range(i+1,n+1)])

## Example
words = ["hello","hello","hello","hello","hello"]
width = 6
