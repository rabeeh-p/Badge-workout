
# try:
#     5 / 0
# except:
#     print('is not possible')
# else:
#     print('success')
# finally:
#     print('finished')



# sample =(1,2,3,2)

# print(sample)
# print(type(sample))
# print(type(sample))
# print(set(sample))


# --------------------------------------- OOPS----------------------
# POLYMORPHISAM
# class Car:
#     def tier(self):
#         pass

# class Thar(Car):

#     def tier(self):
#         print('4 tier')
    

# thar_obj =Thar()
# thar_obj.tier()



# class Myclass:
#     name= 'python'
#     @classmethod
#     def sample(cls):
#         print(f"ehllo{cls.name}")


# Myclass.sample()

# -------------------------------------------  oops ended----------------------




# def sample():
#     yield 10
#     yield 20
#     yield 30

# new = sample()
# print(next(new))
# print(next(new))
# print(next(new))

# my_dict = {"a": 10, "b": 15, "c": 5}
# del my_dict[max(my_dict, key=my_dict.get)]

# print(my_dict)

# my_dict = {"a": 10, "b": 15, "c": 5,'a':6}

# resutl = {x: y for x, y in my_dict.items() if y != max(my_dict.values())}
# print(my_dict)
# print(resutl)




# name = 'madam'

# print(name == name[::-1])


# 54321
#  4321
#   321
#    21
#     1



# for i in range(5):
#     print(' ' * i, end='')

#     for j in range(5-i,0 ,-1):
#         print(j,end='')
#     print()


# for i in range(1,5):
    
#     for j in range(1,i):
#         print(j,end='')
#     print()



# n = 7  # Maximum number of stars in the first row
# for i in range(n, 0, -2):
#     # Print spaces
#     print(" " * ((n - i) // 2), end="")
#     # Print stars
#     print("*" * i)




# REVERSE STRING
# def sample(name):
#     return name[::-1]

# print(sample('hello'))


# PALLINDROM
# name= 'lol'
# def sample(name):
#     for i in range(len(name)):
#         if name[i] != name[len(name)-i-1]:
#             return False
#     return True

# print(sample(name))

# for i in range(5):
#     print("  " * i ,end='')

#     for j in range(5-i * 2):
#         print("* " ,end="")
    
#     print()

# name = {'a':10,'b': 20}
# name2 = {'c':10,'c': 20}

# # result = name + name2
# # name.update(name2)
# name.add({'d':2})
# print(name)


# numbers= [1,2,3,4]
# numbers2= [1,2,3,4]
# result = numbers + numbers2
# print(result)


# name = 'Lorem Ipsum is simply dummy'



# print(name.title())

# final = name.split()
# print(final)
# result = {}

# for i in final:
#     result[i] = len(i)

# print(result)

# result ={ x:len(x) for x in name.split()}
# print(result)

# numbers = [1,2,3,3,1,2,123,23,[12,12,1,[1,2,3],2],2,[[2]]]
# new =[]
# for i in numbers:
#     if i.isinstance(list):
#         for j in i :
#             new.append(j)
#     else:
#         new.append(i)

# print(new)

# def flatten_list(data):
#     flat_list = []
#     for item in data:
#         if isinstance(item, list):
#             flat_list.extend(flatten_list(item))  
#         else:
#             flat_list.append(item) 
#     return flat_list

# # Input list
# numbers = [1, 2, 3, 3, 1, 2, 123, 23, [12, 12, 1, [1, 2, 3], 2], 2, [[2]]]


# for i in range(5):

#     for k in range(i):
#         print(' ',end='')

#     for j in range(5-i):
#         print('* ',end='')
#     print()






