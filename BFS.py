class g_Node():
    def __init__(self, key, adj=[]):
        self.key = key
        self.adj = adj

    def __repr__(self):
        return str(self.key) + "-Node"

    def Adj(self):
        return self.adj

# 4s -- 5q -- 6w
# | \  |
# |  \ |
# 7e    8r -- 9t

#Example to check function on.
s = g_Node(4)
q = g_Node(5)
w = g_Node(6)
e = g_Node(7)
r = g_Node(8)
t = g_Node(9)
s.adj = [q,e,r]
q.adj = [s,r,w]
w.adj = [q]
e.adj = [s]
r.adj = [s,q,t]
t.adj = [r]


#takes stating node and an array of adjascent nodes.
#big O sum of all vertices over size of adjascent list. 2E for undirected, E for directed (handshaking lemma)
def BFS(s, Adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s] #all things you can reach in i-1 moves
    while frontier:
        next = [] #all things you can reach in i moves
        for u in frontier:
            for v in u.adj: #means edge from u to v.
                if v not in level: #this avoids duplicates
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    return level #or parent, depending on what you want.
