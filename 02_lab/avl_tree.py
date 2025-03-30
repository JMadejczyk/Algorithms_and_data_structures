class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class Avl_tree():
    def __init__(self):
        self.root = None
    
    def left_rotate(self, node):
        B = node.right
        Y = B.left
        
        B.left = node
        node.right = Y
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))
        
        return B 
    
    def right_rotate(self, node):
        A = node.left
        Y = A.right
        
        A.right = node
        node.left = Y
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        A.height = 1 + max(self.get_height(A.right), self.get_height(A.left))
        
        return A
        
    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Update balance factor
        bf = self.get_balance(root)
        
        if bf > 1 and value < root.left.value:
            return self.right_rotate(root)
        
        if bf < -1 and value > root.right.value:
            return self.left_rotate(root)
        
        if bf > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if bf < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
        
    def delete(self, root, value):
        if not root:
            return root
        
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        
        if not root:
            return root
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Update balance factor
        bf = self.get_balance(root)
        
        if bf > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        
        if bf < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        
        if bf > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if bf < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)
    
    def print_all(self, node):
        if node:
            self.print_all(node.left)
            print(node.value, end=' ')
            self.print_all(node.right)
            
    def search(self, value):
        curr = self.root
        while curr is not None and value != curr.value:
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return curr
    def update(self, old_value, new_value):
        node_to_update = self.search(old_value)
        if node_to_update is not None:
            node_to_update.value = new_value
            self.root = self.delete(self.root, old_value)
            self.root = self.insert(self.root, new_value)
        else:
            print(f"Node with value {old_value} not found.")
    
avl = Avl_tree()
avl.root = avl.insert(avl.root, 10)
avl.root = avl.insert(avl.root, 20)
avl.root = avl.insert(avl.root, 30)
avl.root = avl.insert(avl.root, 40)
avl.root = avl.insert(avl.root, 50)
avl.root = avl.insert(avl.root, 25)

print("print_all traversal of the AVL tree is:")
avl.print_all(avl.root)

print("\nDeleting 10")
avl.root = avl.delete(avl.root, 10)
print("print_all traversal after deletion:")
avl.print_all(avl.root)
print("\nDeleting 20")
avl.root = avl.delete(avl.root, 20)
print("print_all traversal after deletion:")
avl.print_all(avl.root)

avl.update(30, 35)
print("\nprint_all traversal after update:")
avl.print_all(avl.root)
print("\nSearching for 35:")
node = avl.search(35)
if node:
    print(f"Node with value {node.value} found.")
else:
    print("Node not found.")
print("\nSearching for 100:")
node = avl.search(100)
if node:
    print(f"Node with value {node.value} found.")
else:
    print("Node not found.")
