class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value < node.value:
                if node.left == None:
                    node.left = Node(value)
                else:
                    self.insert(node.left, value)
            else:
                if node.right == None:
                    node.right = Node(value)
                else:
                    self.insert(node.right, value)

    # in order traversal - left, root, right
    def inOrder (self, node):
        if (node != None):
            self.inOrder (node.left)
            print (node.value)
            self.inOrder (node.right)   


    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right)) <= 1



def balanced_bst_from_array(arr):
    a = sorted(arr)
    mid_val = len(arr) // 2
    n = Node(arr[mid_val])
    n.left = balanced_bst_from_array(arr[:mid_val])
    n.right = balanced_bst_from_array(arr[mid_val+1:])

    return n
    
# Find the closest value of a given target value in a given non-empty Binary Search Tree (BST) of unique values.
def closest_node_to_target(root, target):

    child = root.left if target < root.val else root.right
    if not child:
        return root.val

    x = closest_node_to_target(child, target)
    return min(abs(root.val - target), abs(x - target))

# Merge 2 binary trees. sum value at each node
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 and not t2:
        return None
    
    if not t1:
        return t2
        
    if not t2:
        return t1
        
    root = TreeNode(t1.val + t2.val)
    root.left = self.mergeTrees(t1.left, t2.left)
    root.right = self.mergeTrees(t1.right, t2.right)
    
    return root
        

def main():
    t = Tree()
    t.insert(t.root, 1)
    t.insert(t.root, 2)
    t.insert(t.root, 3)
    #t.insert(t.root, 0)

    t.inOrder(t.root)
    print(t.isBalanced(t.root))

if __name__ == "__main__":
    main()