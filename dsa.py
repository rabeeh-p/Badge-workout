
# class HashTable:
#     def __init__(self,size=2):
#         self.size= size
#         self.table = [[] for _ in range(self.size)]

#     def hash_table(self,key):
#         return hash(key) % self.size

    
#     def insert(self,key,value):
#         index = self.hash_table(key)

#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[index].append([key,value])

    
#     def display(self):
#         for i ,bucket in enumerate(self.table):
#             print(f'Bucket {i}: {bucket}')

#     def remove_data(self,key):
#         index = self.hash_table(key)

#         for pair in self.table[index]:
#             if pair[0] == key:
#                 self.table[index].remove(pair)
#                 return True
#         return False

    
# hash_obj = HashTable()
# hash_obj.insert('apple',10)
# hash_obj.insert('orange',20)
# hash_obj.insert('pineple',30)
# hash_obj.insert('carrot',30)

# hash_obj.remove_data('carrot')
# hash_obj.display()
        




# DATE AND TIME

# from datetime import datetime, timedelta
# n_days = 5
# current = datetime.now() + timedelta(days=n_days)
# print(current)


# swap = lambda s: s[-1] + s[1:-1] + s[0] if len(s) > 1 else s
# print(swap("rabeeh"))


# import random
# print(random.randint(0, 100))



# lst = [[1, 2], [3, 4,2,2,2], [5]]
# flat = [item for sublist in lst for item in sublist]
# print(flat)

