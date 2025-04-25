class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def delete(self, index):
        if self.head is None:
            return

        if index == 0:
            if self.head is None:
                return
            self.head = self.head.next
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    def display(self):
        print("HEAD->")
        current_node = self.head
        while current_node:
            print(current_node.data, "->")
            current_node = current_node.next
        print("TAIL")
    
    def sizeOf(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

Llist = LinkedList()
print("A new Linked List has been created.\n")
pick = 0
size = 0
while(pick != 4):
    size = Llist.sizeOf()
    pick = int(input("Choose your functions\n1-Insert 2-Delete 3-Display 4-Exit : "))
    if(pick == 1):
        data = int(input("Enter the data you want to insert : "))
        print("Enter the index you want to insert at (0 -",size,"): ")
        ind = int(input())
        Llist.insert(data,ind)
        print("Data Added : ")
        Llist.display()
    elif(pick == 2):
        print("Enter the index you want to delete from (0 -",size-1,"): ")
        ind = int(input())
        Llist.delete(ind)
        print("Data Deleted : ")
        Llist.display()
    elif(pick == 3):
        print("The Linked list is : ")
        Llist.display()
    else:
        print("Exit Successful")
