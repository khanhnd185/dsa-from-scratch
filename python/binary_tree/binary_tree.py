from collections import deque
from typing import List

'''
Definition
'''
class Node(object):
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        if left: left.parent = self
        if right: right.parent = self


'''
Recursive functions
'''
def subtree_first(node : Node) -> Node:
    if node.left: return subtree_first(node.left)
    return node

def subtree_last(node : Node) -> Node:
    if node.right: return subtree_last(node.right)
    return node

def subtree_successor(node: Node) -> Node:
    if node.right: return subtree_first(node.right)
    while node.parent and node!=node.parent.left: node = node.parent
    return node.parent

def subtree_predecessor(node: Node) -> Node:
    if node.left: return subtree_last(node.left)
    while node.parent and node!=node.parent.right: node = node.parent
    return node.parent

def subtree_insert_after(node : Node, new: Node):
    if not node.right:
        node.right = new
        new.parent = node
    else:
        n = subtree_successor(node)
        n.left = new
        new.parent = n

def subtree_delete(node: Node):
    if node.left is None and node.right is None:
        if node.parent is None: return
        if   node.parent.right == node: node.parent.right = None
        elif node.parent.left  == node: node.parent.left  = None
        #node.parent = None
        return
    if node.left:
        pre = subtree_predecessor(node)
        node.val, pre.val = pre.val, node.val
        subtree_delete(pre)
    elif node.right:
        suc = subtree_successor(node)
        node.val, suc.val = suc.val, node.val
        subtree_delete(suc)

def subtree_sorted_find(node: Node, k):
    if node is None : return None
    if k <  node.val: return subtree_sorted_find(node.left, k)
    if k == node.val: return node
    if k >  node.val: return subtree_sorted_find(node.right, k)


def print_tree_inorder(root: Node):
    if not root: return
    print_tree_inorder(root.left)
    print(root.val, end=" ")
    print_tree_inorder(root.right)
    print()


def bst_from_sorted_array(l : list[int]) -> Node:
    if len(l)==0: return None
    start = 0
    end   = len(l)-1

    mid   = (end-start)//2
    root  = Node(val=l[mid])
    root.left  = bst_from_sorted_array(l[:mid])
    root.right = bst_from_sorted_array(l[mid+1:])
    return root


'''
Level-order traversal - BFS
'''
def print_tree_level_order(root: Node):
    if not root: return
    q = deque([root])
    while q:
        n = q.popleft()
        print(n.val, end=" ")
        if n.left : q.append(n.left)
        if n.right: q.append(n.right)
    print()

def get_tree_from_level_order(l):
    if not l: return None
    root = Node(val=l[0])
    q = deque([root])
    i = 1
    while q:
        n = q.popleft()
        if i<len(l) and l[i] is not None:
            n.left  = Node(val=l[i],parent=n)
            q.append(n.left)
        else:
            n.left  = None
        i +=1
        if i<len(l) and l[i] is not None:
            n.right = Node(val=l[i],parent=n)
            q.append(n.right)
        else:
            n.right = None
        i +=1
    return root

def get_level_order_value(root : Node) -> list[int]:
    if not root: return []
    ret = []
    q  = deque([root])
    while q:
        a = []
        l = len(q)
        for _ in range(l):
            node  = q.popleft()
            a.append(node.val)
            if node.left : q.append(node.left)
            if node.right: q.append(node.right)
        ret.append(a)
    return ret



'''
Examples
'''
def example1(tree : Node):
    root = get_tree_from_level_order(tree)
    print_tree_inorder(root)

def example2():
    n1 = Node(val=1)
    n3 = Node(val=3)
    n2 = Node(val=2,right=n3,left=n1)
    n6 = Node(val=6)
    root = Node(val=4,left=n2,right=n6)

    # In-order transver
    print(subtree_first(root).val)
    print(subtree_last(root).val)
    print(subtree_successor(n3).val)
    print(subtree_successor(n1).val)
    print(subtree_successor(n2).val)
    print(subtree_successor(root).val)

    # Insert a node
    n5 = Node(val=5)
    subtree_insert_after(root, n5)
    print_tree_inorder(root)

    # Insert another node
    n7 = Node(val=7)
    subtree_insert_after(n6, n7)
    print_tree_inorder(root)

    # Delete a node
    subtree_delete(n2)
    print_tree_inorder(root)



if __name__ == "__main__":
    for tree in [
        [4,2,6,1,3],
        [1,0,48,None,None,12,49],
        [236,104,701,None,227,None,911],
        [543,384,652,None,445,None,699],
    ]:
        example1(tree)
        print()

    example2()
