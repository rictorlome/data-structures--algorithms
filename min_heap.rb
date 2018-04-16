## Implements a min binary heap using a map and an array.
## - The map provides lookup in O(1).
## The array encodes the heap property where:
## - the smallest element is at index 0
## - each node located at index i is smaller than the two children located at indices 2i+1 and 2i+2

## The structure supports:
# - decreasing a node's value in O(logn)
# - adding a key in O(logn)
# - removing the min in O(logn) (O(1) to find min, O(logn) to maintain heap property after extraction)

class Node
  attr_accessor :key, :val
  def initialize(key, val)
    @key = key
    @val = val
  end
end

A_Node = Node.new('A', -1)
B_Node = Node.new('B', 2)
C_Node = Node.new('C', 6)
D_Node = Node.new('D', 4)
E_Node = Node.new('E', 5)
F_Node = Node.new('F', 7)
G_Node = Node.new('G', 8)

#             A,-1
#           /      \
#         B,2      C,6
#        /  \      /   \
#     D,4  E,5   F,7   G,8

class MinBinaryHeap
  attr_reader :nodes

  def initialize(nodes=[])
    @nodes = nodes
    @map = create_map
  end

  def create_map
    map = Hash.new
    @nodes.each_with_index do |node, idx|
      map[node.key] = idx
    end
    map
  end

  def left_child(key)
    i = @map[key]
    @nodes[2*i + 1]
  end

  def right_child(key)
    i = @map[key]
    @nodes[2*i + 2]
  end

  def parent(key)
    i = @map[key]
    return nil if i == 0
    @nodes[(i-1)/2]
  end

  def add(key,val)
    throw 'Already in Heap' if self.contains?(key)
    node = Node.new(key,val)
    @nodes << node
    @map[key] = @nodes.length - 1
    until parent(node.key) == nil || parent(node.key).val <= node.val
      swap_child_parent(node,parent(node.key))
    end
  end

  def contains?(key)
    !!@map[key]
  end

  def decrease_val(key,new_val)
    i = @map[key]
    node = @nodes[i]
    node.val = new_val
    until parent(node.key) == nil || parent(node.key).val <= node.val
      swap_child_parent(node,parent(node.key))
    end
  end

  def swap_child_parent(child,parent)
    @nodes[@map[child.key]], @nodes[@map[parent.key]] = @nodes[@map[parent.key]], @nodes[@map[child.key]]
    @map[child.key], @map[parent.key] = @map[parent.key], @map[child.key]
  end

  def smaller_child(node)
    left, right = self.left_child(node.key), self.right_child(node.key)
    return nil if left == nil && right == nil
    return (left.val <= right.val ? left : right) if left && right
    left || right
  end

  def extract_min
    min = @nodes[0]
    until self.smaller_child(min) == nil
      nxt = self.smaller_child(min)
      self.swap_child_parent(nxt,min)
    end
    idx = @map[min.key]
    @map.delete(min.key)
    @nodes[idx] = nil
    min
  end
end

EX_HEAP = MinBinaryHeap.new([A_Node, B_Node, C_Node, D_Node, E_Node, F_Node, G_Node])
