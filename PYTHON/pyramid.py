
# for i in range(5):
#     print("*" * i)
#     print()



# def dec(fun):
#     def wrapper():
#         print('first')
#         fun()
#         print('second')
#     return wrapper

# @dec
# def sample():
#     print("hello")
# sample()

# import copy
# numbers= [1,2,3,[10,20]]

# second_list = copy.deepcopy(numbers)
# second_list[3][0]= 100

# print(numbers)
# print(second_list,'second')


# square = lambda x : x ** 2
# print(square(5))

# pyramid
# for i in range(5):
#     for j in range(5-i):
#         print(' ',end='')
    
#     for k in range(2 * i-1):
#         print("*",end='')
#     print()



# for i in range(5):
#     print(f"{i}"* i)



# for i in range(5):
#     for k in range(5 - i):
#         print(' ', end="")
    
#     for j in range(2 * i - 1):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     print("*"* i)

# num = None
# if not num:
#     print('is true')




# print('hello')


# sample = {'a':10,'b':20,'c':30}
# result = {x:y for x , y in sample.items() if y != max(sample.values())}
# print(result)

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end='')
#     print()



# def is_prime(num):  
#     is_prime_flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime_flag = False
#             break
#     return is_prime_flag

# print(is_prime(7))


# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fac(n-1)
# print(fac(5))


# def revers_string(item):
#     return item[::-1]

# print(revers_string('rabeeh'))


# def largest_value(arr):
#     big= arr[0]
#     for i in arr:
#         if i > big:
#             big = i
#     return big

# arr=[1,2,3,4,5]
# print(largest_value(arr))


# def is_pallindrom(item):
#     return item == item[::-1]

# print(is_pallindrom('lloll'))



# def count(arr):
#     frequency = {}
#     for i in arr:
#         if i not in frequency:
#             frequency[i] = 1
#         else:
#             frequency[i] += 1
#     return frequency

# arr= [1,2,3,1,2,5,6,7]
# print(count(arr))



# def sorting(item):
#     for i in range(len(item)):
#         for j in range(i+1, len(item)):
#             if item[i] > item[j]:
#                 item[i],item[j] = item[j],item[i]
#     return item

# arr= [5,4,3,2,1]
# print(sorting(arr))





for i in range(5):
    for j in range(i):
        print(' ',end='')
    for k in range(5-i):
        print("* ", end='')
    print()


name = {'a': 10, 'b': 20, 'c':30}

result = {x:y for x,y in name.items() if y != max(name.values())}
print(result)