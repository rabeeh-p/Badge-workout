# new file created

# for i in range(5):
#     print(i*i)


# rows = 5
# for i in range(1, rows + 1):
#     print("*" * i)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()




class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, _) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return True
        return False

    def __str__(self):
        return str(self.table)






# names= ['rabeeh',23]

# for i , k in enumerate(names):
#     print(i,k)


# matrix3d = [
#     [[1, 2], [3, 4]],
#     [[5, 6], [7]],
#     [[8]]
# ]

# def flatten(arr):
#     result = []
#     for i in arr:
#         if isinstance(i, list):
#             result.extend(flatten(i))
#         else:
#             result.append(i)
#     return result

# print(flatten(matrix3d))




