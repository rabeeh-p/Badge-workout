
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None



# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         if self.head is None:
#             self.head  = Node(data)
#         else:
#             current = self.head
#             while current.next :
#                 current = current.next
#             current.next= Node(data)
    
#     def display (self):
#         current = self.head
#         while current :
#             print(current.data , end="=>")
#             current = current.next


# def array_to_linkdList(array):
#     linkedList_obj = LinkedList()
#     for i in array:
#         linkedList_obj.append(i) 
#     return linkedList_obj

# array = [1,2,3,4,5]
# hello_obj = array_to_linkdList(array)

# hello_obj.display()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def reverse_linked_list(head):
#     prev = None
#     current = head
    
#     while current is not None:
#         next_node = current.next   
#         current.next = prev        
#         prev = current             
#         current = next_node        
    
#     return prev   

# def print_linked_list(head):
#     current = head
#     while current is not None:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)

# print("Original linked list:")
# print_linked_list(head)

# reversed_head = reverse_linked_list(head)

# print("Reversed linked list:")
# print_linked_list(reversed_head)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

    
#     def append(self,data):
#         new_data = Node(data)

#         if self.head is None:
#             self.head = new_data
        
#         else:
#             current = self.head

#             while current.next :
#                 current = current.next
            
#             current.next = new_data
    
#     def display(self):
        
#         current = self.head

#         while current :
#             print(current.data , end=">")
#             current = current.next

#     def revers(self):
#         current = self.head
#         prev = None

#         while current :
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node

#         self.head = prev
        

# linkedList = LinkedList()
# linkedList.append(1)
# linkedList.append(2)
# linkedList.append(3)
# linkedList.append(4)

# # linkedList.display()
# linkedList.revers()
# linkedList.display()