class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    
    def print_all(self):
        curr = self.head
        while curr:
            if curr.next:
                print(curr.data, end=" <=> ")
            else:
                print(curr.data)
            curr = curr.next
                    
    def insert(self, data, index):
        new_node = Node(data)
        curr = self.head
        for _ in range(index):
            if curr.next:
                curr = curr.next
            else:
                curr.next = new_node
                return
        if index == 0:
            next = self.head
            self.head = new_node
            new_node.next = next
            new_node.next.prev = new_node
            return
        prev = curr.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = curr
        curr.prev = new_node
        
    def delete(self, index):
        curr = self.head
        for _ in range(index):
            if not curr.next:
                print(f"No element with index {index}")
                return
            curr = curr.next
        if curr == self.head:
            self.head = curr.next
        elif curr.next:
            prev = curr.prev
            prev.next = curr.next
            next = curr.next
            next.prev = curr.prev
        else:
            prev = curr.prev
            prev.next = None
        return
    
    def info_all(self):
        curr = self.head
        index = 0
        while curr:
            print(f'{index} - Previous: {curr.prev.data if curr.prev else None}')
            print(f'{index} - Current: {curr.data}')
            print(f'{index} - Next: {curr.next.data if curr.next else None}')
            curr = curr.next
            index += 1

    def print_index(self, index):
        curr = self.head
        for _ in range(index):
            if not curr.next:
                print(f"No element with index {index}")
                return
            curr = curr.next
        print(curr.data)

test_list = DoubleLinkedList()
print('1. Append 5 elements: ')
test_list.append("Cukiereczek")
test_list.append("Jajeczko")
test_list.append("Majonezik")
test_list.append("Alabaster")
test_list.append("Jedwab")
test_list.append("Pierniczek")
test_list.print_all()

print('\n2. Print element with index 3: ')
test_list.print_index(3)

print('\n3. Delete element with index 4 then delete el. with index 3:')
test_list.delete(4)
test_list.delete(3)
test_list.print_all()

print('\n4. Insert element at index 0, then insert element at index 3: ')
test_list.insert("Samochodzik", 0)
test_list.insert("Autobusik", 3)
test_list.print_all()

print('\n5. Delete element with index 5 then with index 1: ')
test_list.delete(5)
test_list.delete(1)
test_list.print_all()

print('\n6. Check integrity of double linked list: ')
test_list.info_all()