#Definition for a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#0. To Create a Binary Tree from a list
def createLevelOrder(root, arr, start, end):
    if start < end and arr[start] != None:

        root = TreeNode(arr[start])

        root.left  = createLevelOrder(root.left, arr, 2*start+1, end)
        root.right = createLevelOrder(root.right, arr, 2*start+2, end)
        
    return root


#1. PreOrder Traversal with recursion
def preOrder(root: TreeNode):
    if root is None:
        return
    
    print(root.val, end=", ")
    preOrder(root.left)
    preOrder(root.right)


#2. InOrder Traversal with recursion
def inOrder(root: TreeNode):
    if root is None:
        return

    inOrder(root.left)
    print(root.val, end=", ")
    inOrder(root.right)


#3. Post Order Traversal with recursion
def postOrder(root: TreeNode):
    if root is None:
        return

    postOrder(root.left)
    postOrder(root.right)    
    print(root.val, end=", ")


#4. Sum of all nodes
def sumOfAllNodes(root: TreeNode):
    if not root:
        return 0
    
    return root.val + sumOfAllNodes(root.left) + sumOfAllNodes(root.right)


#5. Get difference of values at Even & Odd level
def diffOddEvenLevel(root: TreeNode):
    if not root:
        return 0
    
    return root.val - diffOddEvenLevel(root.left) - diffOddEvenLevel(root.right)


#Driver - Testing
def main():
    print("\n Hello github")

    #Example 1
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = None
    root = createLevelOrder(root, arr, 0, len(arr))

    #Example 2
    #arr = [1, 2, 3, 4, 5, None, 7, 8, 9, None, 10, None, None, 11, 12]    
    #root = None    
    #root = createLevelOrder(root, arr, 0, len(arr))

    #print("\n preOrder")
    #preOrder(root)
    
    print("\n inOrder")
    inOrder(root)

    #print("\n postOrder")
    #postOrder(root)

    print("\n Sum of all nodes")
    print(sumOfAllNodes(root))

    print("\n Diff of odd and even")
    print(diffOddEvenLevel(root))
    
    print("\n \n End github")    

if __name__ == "__main__":
    main()


#Example Tree
#   arr = [1, 2, 3, 4, 5, 6, 7]
#
#
#           1
#       2        3
#    4    5   6     7


#   arr = [1, 2, 3, 4, 5, None, 7, 8, 9, None, 10, None, None, 11, 12]    
#
#
#               1
#         2           3
#      4    5      N      7
#     8 9  N 10   N N   11 12

