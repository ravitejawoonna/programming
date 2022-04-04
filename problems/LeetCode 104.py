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
        