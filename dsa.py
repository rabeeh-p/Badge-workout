
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

# # class HashTable:
# #     def __init__(self,size=10):
# #         self.size= size
# #         self.table= [[] for _ in range(self.size)]
        
# #     def hash_function(self,key):
# #         return hash(key) % self.size
        
# #     def insert(self,key,value):
# #         index = self.hash_function(key)
        
# #         for pair in self.table[index]:
# #             if pair[0] == key:
# #                 pair[1] = value
# #                 return
# #         self.table[index].append([key,value])
        
    
# #     def display(self):
# #         for i , k in enumerate(self.table):
# #             print(f" {i}: {k}")
            

# # obj = HashTable()
# # obj.insert('apple',10)
# # obj.insert('apple',20)
# # obj.insert('orange',10)

# # obj.display()


# # def binary_search(arr,target):
    
# #     if not arr:
# #         return -1
        
# #     mid = len(arr) // 2
    
# #     if arr[mid] == target:
# #         return mid
# #     elif arr[mid] < target:
# #         result = binary_search(arr[mid+1:],target)
# #         return mid + 1 + result if result != -1 else -1
# #     else:
# #         return binary_search(arr[:mid],target)

# # arr= [1,2,3,4,5,6,7,8,9,10]

# # print(binary_search(arr,9))




# def checking(word1,word2):
    
#     name1= word1.replace(' ','').lower()
#     name2= word2.replace(' ','').lower()
#     return sorted(name1) == sorted(name2)
    
    
# print(checking('Listen','Silent'))



# result = lambda a,b: a+b

# print(result(10,20))



# for i in range(2, 100):
#     for k in range(2, i):
#         if i % k == 0:
#             break  # Not a prime number
#     else:
#         print(i)  # Prime number












# from itertools import permutations

# perms = [''.join(p) for p in permutations("rab")]
# print(perms)







from itertools import permutations

result = [ ''.join(p) for p in permutations('rab')]


print(result)






def sample():
    print('hello')

sample()
