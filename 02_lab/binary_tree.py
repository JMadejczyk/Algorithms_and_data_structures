class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_search_tree():
    def __init__(self):
        self.root = None
        
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if root.data == data:
            return root
        if root.data < data:
            root.right = self.insert(root.right, data)
        else:
            root.left = self.insert(root.left, data)
        return root

    def print_all(self, root):
        if root:
            self.print_all(root.left)
            print(root.data, end=" ")
            self.print_all(root.right)
            
    def search(self, root, data):
        if root is None or root.data == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        return self.search(root.left, data)
    
    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root
    
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
test = Binary_search_tree()
print("Binary search tree:")
print("\nInserting 5 elements:")
test.root = test.insert(test.root, 109)
test.root = test.insert(test.root, 25)
test.root = test.insert(test.root, 123)
test.root = test.insert(test.root, 44)
test.root = test.insert(test.root, 5)

print("\nAfter insertion:")
test.print_all(test.root)

print("\n\nSearching for node with value 123")
node_with_searched_value = test.search(test.root, 123)
print("Value of searched node:")
print(node_with_searched_value.data if node_with_searched_value else "Not found")

print("\nSearching for node with value 1")
node_with_searched_value = test.search(test.root, 1)
print(node_with_searched_value.data if node_with_searched_value else "Not found")

print("\nDeleting node with value 109:")
test.root = test.delete(test.root, 109)
print("After deletion:")
test.print_all(test.root)
print()
