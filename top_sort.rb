require 'set'

class Node
  attr_accessor :val, :children
  def initialize(val, children=[])
    @val = val
    @children = children
  end
end

A_Node = Node.new('A')
B_Node = Node.new('B')
C_Node = Node.new('C')
D_Node = Node.new('D')
E_Node = Node.new('E')
F_Node = Node.new('F')
G_Node = Node.new('G')

A_Node.children = [C_Node]
B_Node.children = [C_Node,E_Node]
C_Node.children = [D_Node]
D_Node.children = []
E_Node.children = [F_Node]
F_Node.children = [D_Node, G_Node]
G_Node.children = []

#  All edges point downwards!
#
#  A     B
#   \  /  \
#    C    E
#   /    /
#  D <- F
#        \
#         G

class DAG
  def initialize(nodes)
    @nodes = nodes
  end

  def dfs(start,visited,stack)
    visited.add(start)
    start.children.each do |child|
      dfs(child,visited,stack) unless visited.include?(child)
    end
    stack.push(start)
  end

  def top_sort
    visited = Set.new
    stack = []
    @nodes.each do |node|
      dfs(node,visited,stack) unless visited.include?(node)
    end
    stack.reverse.map {|el| el.val }
  end
end

EX_DAG = DAG.new([A_Node, B_Node, C_Node, D_Node, E_Node, F_Node, G_Node])
