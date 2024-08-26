from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def print_tree(node: Optional[TreeNode]):
            if node is None:
                return 
            print_tree(node.left)
            print_tree(node.right)
            res.append(node.val)
        print_tree(root)
        return res
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:  
        if not nodes:  
            return None  

        root = TreeNode(nodes[0])  
        queue = [root]  
        index = 1  

        while queue and index < len(nodes):  
            node = queue.pop(0)  
            if index < len(nodes) and nodes[index] is not None:  
                node.left = TreeNode(nodes[index])  
                queue.append(node.left)  
            index += 1  
            
            if index < len(nodes) and nodes[index] is not None:  
                node.right = TreeNode(nodes[index])  
                queue.append(node.right)  
            index += 1  

        return root  


input_data = [1, None, 2, 3]  
root = build_tree(input_data)  

 
solution = Solution()  
result = solution.postorderTraversal(root)  
print(result)