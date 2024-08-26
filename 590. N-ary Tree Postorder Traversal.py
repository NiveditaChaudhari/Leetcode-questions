from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def print_tree(node:'Node'):
            if node is None:
                return
            for child in node.children:
                print_tree(child)
            res.append(node.val)
        print_tree(root)
        return res
