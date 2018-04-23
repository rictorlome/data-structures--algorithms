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
    ## This initializes start to 0 and all other nodes to infinity
    heap = initialize_heap(start)
    distance_map = {start => 0}
    predecessor_map = {start => nil}
    until heap.empty?
      min = heap.extract_min
      distance_map[min.key] = min.val
      edges = self.adj_list[self.map_to_idx[min.key]]
      edges.each do |edge|
        key, weight = edge
        new_val = weight + distance_map[min.key]
        if heap.contains?(key) && heap.get_val(key) > new_val
          heap.decrease_val(key,new_val)
          predecessor_map[key] = min.key
        end
      end
    end
    [distance_map,predecessor_map]
  end
end

WeightedGraph.class_eval { include Dijkstra }
