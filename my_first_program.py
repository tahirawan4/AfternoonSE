number = 15
number2 = 'This is a string having a number 7 in it.'

print(number)
print(number2)


def add(num1, num2):
    return num1+num2

print(add(3,5))


numbers_list = ['one', 'two', 'three']

for index in range(len(numbers_list)):
    print(numbers_list[index])



student_name = ['name1','name2','name3']
student_roll_number = ['1','2','3']


for index in range(len(student_name)):
    print(student_roll_number[index])
    print(student_name[index])
#    print('Roll Number: %s, Name: %s' % (student_roll_number[index],student_name[index]))


students_dict = {'1':{'name':'name1','cgpa':'2.91'},'2':{'name':'Name2','cgpa':'3.99'}}

student_info = students_dict.get('2') # {'name':'name1','cgpa':'2.91'}
print(student_info.get('cgpa'))


print(students_dict.keys())
