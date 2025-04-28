
# import datetime
# from datetime import datetime,timedelta

# today = datetime.today()
# print(today)

# n = 10

# future = today + timedelta(days=n)
# print(future)



# def sample():
#     yield 10
#     yield 20


# new= sample()

# print(next(new))
# print(next(new))


arr = [4,3,7,9,2]
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1]=  arr[j+1], arr[j]
    return arr

print(bubble_sort(arr))











# arr = [4,3,7,9,2]
# def bubble_sort(arr):

#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1]=  arr[j+1], arr[j]
#     return arr

# print(bubble_sort(arr))






