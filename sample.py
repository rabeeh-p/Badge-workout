
# numbers = [64, 34, 25, 12, 22, 11, 90]


# def merge_sort(arr):

#     if len(arr) >=1 :
        
      
#         mid = len(arr) // 2

#         left = arr[:mid]
#         right = arr[mid:]

#         return merge_sort(left) + mid + merge_sort(right)
    

# print(merge_sort(numbers))
    
num = 1

for i in range(5):
    for j in range(i):
        print(num, end='')
        num += 1

    print()


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)
# dict1.add(dict2)
# print(dict1)




# number = [1,2,3,4,5]

# result = list(map(lambda x : x**2 , number))

# print(result)

# number = [1,2,4,5]

# big = max(number)
# print(big)

# missing= []
# for i in range(1,big+1):
#     if i not in number:
#         missing.append(i)
# print(missing)




# from django.db import models

# class Teacher(models.Model):
#     name = models.CharField(max_length=100)

# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     teacher = models.ForeignKey(Teacher, related_name='courses', on_delete=models.CASCADE)

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     courses = models.ManyToManyField(Course, related_name='students')


# obj= Course.objects.filter(teacher__name= 'john')

# python_obj = Student.objects.prefetch_related('students').filter(title= 'python')

