require 'set'
require './min_heap.rb'

## Implementation of Prim's Minimum Spanning Tree Algorithm
## Uses BinaryMinHeap and HashMap of Vertices to ShortestEdge

## Time Complexity -> O(E) operations on O(V) vertices,
##                    where each operation is O(logv) (add, decreaseVal, extractMin)


#        1      6
#    A ---- D ----  E
#    |     /|     / |
#  3 |  3/  |1  /5  | 2
#    | /    | /     |
#    B ---  C ----  F
#       1       4
FIXNUM_MAX = (2**(0.size * 8 -2) -1)

EX_ADJ_LIST = [
  [['D',1],['B',3]],                    #A
  [['A',3],['C',1],['D',3]],            #B
  [['B',1],['D',1],['E',5],['F',4]],    #C
  [['A',1],['B',3],['C',1],['E',6]],    #D
  [['D',6],['C',5],['F',2]],            #E
  [['C',4],['E',2]]                     #F
]
EX_MAP_TO_IDX = {
    'A' => 0,
    'B' => 1,
    'C' => 2,
    'D' => 3,
    'E' => 4,
    'F' => 5,
}

class WeightedGraph
  attr_reader :adj_list, :map_to_idx
  
  def initialize(adj_list=[], map_to_idx={})
    @adj_list = adj_list
    @map_to_idx = map_to_idx
  end

  def prims(start)
    heap = initialize_heap(start)
    map = Hash.new
    res = []

    min = heap.extract_min.key

    until heap.empty?
      edges = @adj_list[@map_to_idx[min]]
      edges.each do |edge|
        key, weight = edge
        if heap.contains?(key) && heap.get_val(key) > weight
          heap.decrease_val(key,weight)
          map[key] = [min,edge]
        end
      end
      min = heap.extract_min.key
      res << map[min]
    end

    res
  end

  def initialize_heap(start)
    heap = MinBinaryHeap.new
    @map_to_idx.each do |v,idx|
      start == v ? heap.add(v,0) : heap.add(v, FIXNUM_MAX)
    end
    heap
  end
end

EX_GRAPH = WeightedGraph.new(EX_ADJ_LIST,EX_MAP_TO_IDX)
EX_GRAPH.prims('A')
