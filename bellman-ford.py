import sys
## Example graph:

##        1
##    A ---- B
##    |      |
## -1 |      | -1
##    |      |
##    C ---- D
##       -1

ex_ADJ = [
    [['B',1],['C',-1]],
    [['A',1],['D',-1]],
    [['A',-1],['D',-1]],
    [['B',-1],['C',-1]]
]
ex_MAP = {
    'A':0,
    'B':1,
    'C':2,
    'D':3
}

class directed_weighted_graph():
    def __init__(self, adj_list, map_to_idx):
        self.adj_list = adj_list
        self.map_to_idx = map_to_idx

    def weight(self,u,v):
        idx = self.map_to_idx[u]
        for key,weight in self.adj_list[idx]:
            if key is v:
                return weight

    def relax(self,u,v,d,pi):
        if d[v] > d[u] + self.weight(u,v):
            d[v] = d[u] + self.weight(u,v)
            pi[v] = u
        return

    ## Complexity is O(V*E). If E = V^2, it's O(V^3).
    def bellman_ford(self,start):
        d, pi = { key : 0 if start is key else sys.maxsize for key in self.map_to_idx.keys() }, {start: None}
        ## Vertices - 1 times...
        for i in range(1,len(self.adj_list)):
            for u, idx in self.map_to_idx.items():
                for v, w in self.adj_list[idx]:
                    self.relax(u,v,d,pi)
        for u, idx in self.map_to_idx.items():
            for v, w in self.adj_list[idx]:
                if d[v] > d[u] + self.weight(u,v):
                    return 'Negative Weight Cycle Detected'
                else:
                    return d, pi



ex_GRAPH = directed_weighted_graph(ex_ADJ,ex_MAP)
