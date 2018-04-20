require './prims.rb'

## Implementation of Dijkstra's algorithm for single source shortest paths.
## This implementation relies on an underlying BinaryMinHeap data structure (not a Fibonnaci heap)
## And it returns two hashes, a distance hash and predecessor hash.

## Time analysis:

## Theta(v) inserts into Heap. Each is lg v.
## Theta(v) extract min operations. Each is lg v.
## Theta(e) decrease key operations. Each is lg v.

## Theta(2(v * lg v) + e * lg v) => Theta(v*lgv + e*lgv)


## Assumes non-negative cycles.
module Dijkstra
  def dijkstra(start)
    heap = initialize_heap(start)
    distance_map = {}
    predecessor_map = {}

    min = heap.extract_min.key
    distance_map[min] = 0
    predecessor_map[min] = nil

    until heap.empty?
      edges = self.adj_list[self.map_to_idx[min]]
      edges.each do |edge|
        key, weight = edge
        new_val = weight + distance_map[min]
        if heap.contains?(key) && heap.get_val(key) > new_val
          heap.decrease_val(key,new_val)
          predecessor_map[key] = min
        end
      end
      min = heap.extract_min
      distance_map[min.key] = min.val
      min = min.key
    end
    [distance_map,predecessor_map]
  end
end

WeightedGraph.class_eval { include Dijkstra }
