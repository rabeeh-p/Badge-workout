# new file created

# for i in range(5):
#     print(i*i)


# rows = 5
# for i in range(1, rows + 1):
#     print("*" * i)



# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Print the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()
