class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) +"->",end=" ")
        inorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

def postorder(root):
    if root:
        postorder(root.right)
        postorder(root.left)
        print(str(root.val)+"->",end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nPostorder traversal ")
postorder(root) 

def preorder(root):
    if root:
        print(str(root.val)+"->",end=" ")
        preorder(root.left)
        preorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\npreorder traversal ")
preorder(root)
