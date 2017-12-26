# Implementation of basic binary search tree with insert, find, find_min, find_max, find_successor, and delete

class Node:

    def __init__(self, val, parent=None, l_child=None, r_child=None):
        self.val = val
        self.parent = parent
        self.l_child = l_child
        self.r_child = r_child

    def __repr__(self):
        return '[{0}]'.format(self.val)

    def has_l_child(self):
        return self.l_child != None

    def has_r_child(self):
        return self.r_child != None

    def is_l_child(self):
        return self.parent != None and self.parent.l_child == self

    def is_r_child(self):
        return self.parent != None and self.parent.r_child == self

    def is_root(self):
        return self.parent is None

    def has_both_children(self):
        return self.l_child and self.r_child

    def has_any_children(self):
        return self.l_child or self.r_child



class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __repr__(self):
        return '              {0}   \n          /          \ \n        {1}          {2}'.format(self.root,self.root.l_child, self.root.r_child)

    def set_root(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            pass

    def insert(self, val):
        if self.root is None:
            self.set_root(val)
        else:
            self.insert_node(self.root, val)
        self.size += 1

    def insert_node(self, cur_node, val):
        if val <= cur_node.val:
            if cur_node.l_child:
                self.insert_node(cur_node.l_child, val)
            else:
                cur_node.l_child = Node(val, parent=cur_node)
        elif val > cur_node.val:
            if cur_node.r_child:
                self.insert_node(cur_node.r_child, val)
            else:
                cur_node.r_child = Node(val, parent=cur_node)

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, cur_node, val):
        if cur_node is None:
            return False
        elif val == cur_node.val:
            return cur_node
        elif val < cur_node.val:
            return self.find_node(cur_node.l_child, val)
        else:
            return self.find_node(cur_node.r_child, val)

    def find_min(self):
        min_node = self.find_min_node(self.root)
        return min_node.val

    def find_min_node(self, cur_node):
        if cur_node.l_child is None:
            return cur_node
        else:
            return self.find_min_node(cur_node.l_child)

    def find_max(self):
        max_node = self.find_max_node(self.root)
        return max_node.val

    def find_max_node(self, cur_node):
        if cur_node.r_child is None:
            return cur_node
        else:
            return self.find_max_node(cur_node.r_child)

    def find_successor(self, val):
        if self.find(val):
            cur = self.find(val)
            return self.find_successor_node(cur)
        else:
            raise 'Val not in BST'

    def find_successor_node(self, cur_node):
        if self.find_max_node(self.root) is cur_node:
            return None
        elif cur_node.has_r_child():
            return self.find_min_node(cur_node.r_child)
        else:
            while cur_node.is_r_child():
                cur_node = cur_node.parent
            return cur_node.parent

    def delete(self, val):
        if self.find(val):
            node = self.find(val)
            self.delete_node(node)
            self.size -= 1
        else:
            raise 'Val not in BST'

    def delete_node(self, node):
        #no children
        if not node.has_any_children():
            if node.is_l_child():
                node.parent.l_child = None
            elif node.is_r_child():
                node.parent.r_child = None
        #one child
        elif node.has_any_children() and not node.has_both_children():
            if node.is_l_child():
                if node.has_l_child():
                    node.parent.l_child = node.l_child
                else:
                    node.parent.l_child = node.r_child
            elif node.is_r_child():
                if node.has_l_child():
                    node.parent.r_child = node.l_child
                else:
                    node.parent.r_child = node.r_child
        #two children
        else:
            succ = self.find_successor_node(node)
            node.val, succ.val = succ.val, node.val
            self.delete_node(succ)

#example for use in interactive mode.
b = BST()
q = [12,44,23,14,55,77,88,45,1]
for i in q:
    b.insert(i)
