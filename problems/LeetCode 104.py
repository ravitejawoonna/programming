from collections import deque
from dec_caltime import time_dec

@time_dec
def maxDepth(root):
    if root == None:
        return 0
    
    return max(
        maxDepth(root.left)+1, maxDepth(root.right)+1
    )
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#faster
def maxDepth_DFS(root):
    if root == None:
        return 0
    q = deque([root])
    level =0
    while q:
        
        for i in range(len(q)):
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level +=1
    return level

                