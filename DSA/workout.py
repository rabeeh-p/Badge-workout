
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         pos = arr[i]
#         j = i-1
#         while j >=0 and  pos < arr[j]:
#             arr[j+ 1] = arr[j]
#             j -= 1
#         arr[j+1] = pos
#     return arr

# arr=[13,43,1,2,67,3]
# print(insertion_sort(arr))


# import random
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = random.choice(arr)
#         small = [x for x in arr if x < pivot]
#         greate = [x for x in arr if x > pivot]
#         return quick_sort(small) + [pivot] + quick_sort(greate)

# arr=[13,43,1,2,67,3]
# print(quick_sort(arr))





# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next= None

# class LinkdList:
#     def __init__(self):
#         self.head = None

#     def add_node(self,data):
#         new_data = Node(data)

#         if self.head is None:
#             self.head = new_data
#         else:
#             current = self.head

#             while current.next :
#                 current = current.next
            
#             current.next= new_data
         
#     def display(self):
#         current = self.head
#         if current is None:
#             print("The linked list is empty.")
#             return

#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")


# li= LinkdList()
# li.add_node(10)
# li.add_node(20)
# li.add_node(30)
# # li.add_node(40)

# # li.display()

