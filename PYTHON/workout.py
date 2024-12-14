
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

for i in range(5):
    print("  " * i ,end='')

    for j in range(5-i * 2):
        print("* " ,end="")
    
    print()