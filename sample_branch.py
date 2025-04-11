

# def hello():
#     return print('hello world')


# hello()



class HashTable:

    def __init__(self,size= 2):
        self.size = size
        # self.table = [[] for  _ in range(self.size)]
        self.table =[None] * self.size 

    

    def hash_function(self,key):
        return hash(key) % self.size
    

    # def insert(self,key,value):
    #     index = self.has_function(key)
    #     for pair in self.table[index]:
    #         if pair[0] == key:
    #             pair[0] = value
    #             return
            
    #     self.table[index].append([key,value])

#     def insert(self, key, value):
#         index = self.hash_function(key)

#         while self.table[index] is not None:
#             stored_key, _ = self.table[index]
#             if stored_key == key:  
#                 self.table[index] = (key, value)
#                 return
#             index = (index + 1) % self.size  

#         # Insert new key-value pair
#         self.table[index] = (key, value)

#     def display(self):
#         for i, bucket in enumerate(self.table):
#             print(f'{i}== {bucket}')

# obj = HashTable()

# obj.insert('apple',10)
# obj.insert('oragne',20)
# # obj.insert('pinappl',30)
# obj.display()
                
# class HashTable:
#     def __init__(self, size=2):
#         self.size = size
#         self.table = [None] * self.size  # Initialize with None for linear probing

#     def hash_function(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self.hash_function(key)

#         # Linear probing: Find the next available slot
#         while self.table[index] is not None:
#             stored_key, _ = self.table[index]
#             if stored_key == key:  # If key already exists, update value
#                 self.table[index] = (key, value)
#                 return
#             index = (index + 1) % self.size  # Move to next slot

#         # Insert new key-value pair
#         self.table[index] = (key, value)

#     def display(self):
#         for i, bucket in enumerate(self.table):
#             print(f'{i} == {bucket}')

# # Example Usage
# obj = HashTable()

# obj.insert('apple', 10)
# obj.insert('orange', 20)

# obj.display()



# class HashTable:
#     def __init__(self,size=5):

#         self.size = size
#         # self.table = [None] * size

#         self.table= [[] for _ in range(size)]

    
#     def hash_function(self,key):
#         return hash(key) % self.size
    
#     def insert(self,key,value):

#         index = self.hash_function(key)

#         for i in self.table[index]:
#             if i[0] == key:
#                 i[0] = value
#                 return
        
#         self.table[index].append([key,value])


#     def display(self):
#         for i,k in enumerate(self.table):

#             print(f'{i} => {k}')
        

# obj = HashTable()
# obj.insert('apple',10)
# obj.insert('orange',10)

# obj.display()



# add = lambda x,b: x+ b
# print(add(5,5))



# sqquare = [x*x for x in range(1,5)]
# print(sqquare)

# word = 'hello world'
# reversed_words= ' '.join([w[::-1] for w in word.split()])
# print(reversed_words)




