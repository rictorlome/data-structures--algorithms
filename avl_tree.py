#Implementation of AVL trees, which rebalance after insertion and delete.
#Much of this code is copied from OCW 6.006 Notes
#The delete_node function seems to be buggy. It resurrects dead nodes, and it cannot delete the min.
#The size attribute of the tree is also not protected against these bugs, and it continues to decrement even though the nodes remain in place

import binary_search_tree

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_node_height(node):
    node.height = max(height(node.l_child), height(node.r_child)) + 1


class AVL(binary_search_tree.BST):
    #not used because rebalance does the same thing.
    def update_heights_to_root(self, cur_node):
        while cur_node is not self.root:
            update_node_height(cur_node)
            cur_node = cur_node.parent
        #update root too
        update_node_height(cur_node)

    def insert_node(self, cur_node, val):
        binary_search_tree.BST.insert_node(self, cur_node, val)
        self.rebalance(cur_node)

    def delete_node(self, node):
        binary_search_tree.BST.delete_node(self, node)
        self.rebalance(node.parent)

    #copied from ocw6.006 notes.
    def left_rotate(self, x):
        #store variable for r_child
        y = x.r_child
        #node's parent is now parent of node's r_child
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.l_child is x:
                y.parent.l_child = y
            elif y.parent.r_child is x:
                y.parent.r_child = y
        x.r_child = y.l_child
        if x.r_child is not None:
            x.r_child.parent = x
        y.l_child = x
        x.parent = y
        update_node_height(x)
        update_node_height(y)

    def right_rotate(self, x):
        y = x.l_child
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.l_child is x:
                y.parent.l_child = y
            elif y.parent.r_child is x:
                y.parent.r_child = y
        x.l_child = y.r_child
        if x.l_child is not None:
            x.l_child.parent = x
        y.r_child = x
        x.parent = y
        update_node_height(x)
        update_node_height(y)

    def rebalance(self, node):
        while node is not None:
            update_node_height(node)
            if height(node.l_child) >= 2 + height(node.r_child):
                if height(node.l_child.l_child) >= height(node.l_child.r_child):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.l_child)
                    self.right_rotate(node)
            elif height(node.r_child) >= 2 + height(node.l_child):
                if height(node.r_child.r_child) >= height(node.r_child.l_child):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.r_child)
                    self.left_rotate(node)
            node = node.parent


#example for use in interactive mode.
b = AVL()
q = [12,44,23,14,55,77,88,45,1]
for i in q:
    b.insert(i)
