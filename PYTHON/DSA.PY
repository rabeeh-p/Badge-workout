
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head  = Node(data)
        else:
            current = self.head
            while current.next :
                current = current.next
            current.next= Node(data)
    
    def display (self):
        current = self.head
        while current :
            print(current.data , end="=>")
            current = current.next


def array_to_linkdList(array):
    linkedList_obj = LinkedList()
    for i in array:
        linkedList_obj.append(i)
    return linkedList_obj

array = [1,2,3,4,5]
hello_obj = array_to_linkdList(array)

hello_obj.display()