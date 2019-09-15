# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []

        stack = [ [ root, False, False ] ]
        
        while stack:
            node = stack[0][0]

            if node is None:
                # print('None, ascending')
                del(stack[0])
                continue

            lvisited = stack[0][1]
            rvisited = stack[0][2]

            if node.val is not None and not (lvisited or rvisited):
                # 1st time visited: traversing value
                traversal.append(node.val)

            if not lvisited:
                # Left node now visited, mark so
                stack[0][1] = True

                if node.left is not None:
                    # Descending into the left node
                    stack.insert(0, [ node.left, False, False ])
                else:
                    # Going to descent into the right node on the next iteration
                    continue
            elif not rvisited:
                # Right node now visited, mark so
                stack[0][2] = True
                
                if node.right is not None:
                    # Descending into the right node
                    stack.insert(0, [ node.right, False, False ])
                else:
                    # Ascending
                    del(stack[0])
                    continue
            else:
                # Both visited, ascending
                del(stack[0])

        return traversal
