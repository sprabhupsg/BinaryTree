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

#6. Get Number of Nodes in a Binary Tree
def countNodes(root: TreeNode):
    if not root:
        return 0
    
    return 1 + countNodes(root.left) + countNodes(root.right)

#7. Get number of Leaf Nodes in Binary Tree
def countLeafNodes(root: TreeNode):
    if not root:
        return 0

    if root.left is None and root.right is None:
        return 1
    
    return countLeafNodes(root.left) + countLeafNodes(root.right)

#8. Get Height of a Binary Tree
def heightOfTree(root: TreeNode):
    if not root:
        return 0

    return max(heightOfTree(root.left), heightOfTree(root.right))+1

#9. Print elements at given level in Binary Tree
def printAtLevel(root: TreeNode, level):
    if root is None:
        return

    if level == 1:
        print(root.val, end=", ")
        return

    printAtLevel(root.left, level-1)
    printAtLevel(root.right, level-1)

#10. Print elements in Level order Recursion
def printAllLevel(root: TreeNode):
    if not root:
        return 0

    height = heightOfTree(root)
    for i in range(height):
        printAtLevel(root, i+1)
        print("\n")

#Driver - Testing
def main():
    print("\n##### Hello Binary Tree #####")

    #Example 1
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = None
    root = createLevelOrder(root, arr, 0, len(arr))

    #Example 2
    #arr = [1, 2, 3, 4, 5, None, 7, 8, 9, None, 10, None, None, 11, 12]    
    #root = None    
    #root = createLevelOrder(root, arr, 0, len(arr))

    print("\n===== 1. PreOrder =====")
    preOrder(root)
    
    print("\n\n===== 2. InOrder =====")
    inOrder(root)

    print("\n\n===== 3. PostOrder =====")
    postOrder(root)

    print("\n\n===== 4. Sum of all nodes =====")
    print(sumOfAllNodes(root))

    print("\n===== 5. Get difference of values at Even & Odd level =====")
    print(diffOddEvenLevel(root))

    print("\n===== 6. Get Number of Nodes in a Binary Tree =====")
    print(countNodes(root))

    print("\n===== 7. Get number of Leaf Nodes in Binary Tree =====")
    print(countLeafNodes(root))

    print("\n===== 8. Get Height of a Binary Tree =====")
    print(heightOfTree(root))

    print("\n===== 9. Print elements at given level in Binary Tree =====")
    printAtLevel(root, 2)

    print("\n===== 10. Print elements in Level order Recursion =====")
    printAllLevel(root)
    
    print("\n \n##### End of Binary Tree #####")    

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
