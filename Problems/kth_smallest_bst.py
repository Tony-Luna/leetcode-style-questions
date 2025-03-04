# Script: kth_smallest_bst.py
"""
Question: Kth Smallest Element in a BST
Given the root of a binary search tree (BST) and an integer `k`, 
return the kth smallest element in the BST.
Example:
    Input: BST represented as [3,1,4,null,2] and k = 1
    Output: 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    # Use in-order traversal to get elements in sorted order.
    stack = []
    current = root
    count = 0
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right
    
    return -1  # In case k is out of bounds.

# Helper function to insert nodes into the BST (for testing purposes).
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

if __name__ == "__main__":
    # Construct BST from list representation [3,1,4,null,2]
    values = [3, 1, 4, 2]  # Using these values to create the BST.
    root = None
    for v in values:
        root = insert_into_bst(root, v)
    k = 1
    result = kth_smallest(root, k)
    print("Kth smallest element in BST:", result)
