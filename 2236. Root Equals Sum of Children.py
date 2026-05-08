class Solution(object):
    def checkTree(self, root):
        root_val = root.val
        left_val = root.left.val
        right_val = root.right.val
        
        return root_val == (right_val + left_val)