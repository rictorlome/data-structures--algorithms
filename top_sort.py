class Node():
    def __init__(self, key, children=[]):
        self.key = key
        self.children = children

    def __repr__(self):
        return self.key

 ## All edges point downward..
#   A    B
#     \ / \
#      C    E
#     /    /
#    /    F
#    \  /  \
#      D    G

A_Node = Node('A')
B_Node = Node('B')
C_Node = Node('C')
D_Node = Node('D')
E_Node = Node('E')
F_Node = Node('F')
G_Node = Node('G')

A_Node.children = [C_Node]
B_Node.children = [C_Node,E_Node]
C_Node.children = [D_Node]
D_Node.children = []
E_Node.children = [F_Node]
F_Node.children = [D_Node, G_Node]
G_Node.children = []

class DAG():
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def dfs(self,start,visited,stack):
        visited.add(start)
        for child in start.children:
            if child not in visited:
                self.dfs(child,visited,stack)
        stack.append(start)

    def top_sort(self):
        visited = set()
        stack = []
        for node in self.nodes:
            if node not in visited:
                self.dfs(node,visited,stack)
        stack.reverse()
        return stack

ex_DAG = DAG([A_Node, B_Node, C_Node, D_Node, E_Node, F_Node, G_Node])
ex_DAG.top_sort() ## => [B, E, F, G, A, C, D]


