"""
LeetCode 2196. Create Binary Tree From Descriptions

Difficulty: Medium

Approach:
- Use a hashmap to create/reuse TreeNode objects.
- Track all child nodes in a set.
- Connect parent and child according to isLeft.
- The root is the only node that never appears as a child.

Time Complexity: O(n)
Space Complexity: O(n)

Concepts:
- Hash Map
- Tree Construction
- Set
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            children.add(child)

            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for value in nodes:
            if value not in children:
                return nodes[value]
