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
                # print('Appending {}'.format(node.val))
                traversal.append(node.val)

            if not lvisited:
                # print('Descending left')
                stack[0][1] = True

                stack.insert(0, [ node.left, False, False ])
            elif not rvisited:
                # print('Descending right')
                stack[0][2] = True

                stack.insert(0, [ node.right, False, False ])
            else:
                # print('Both visited, ascending')
                del(stack[0])

        return traversal
