# Dictionary: key-value pair - {key: value}
students_dict = {
    'student1': 'Joeri',
    'student2': 'Ally',
    'student3': 'Shivastav',
    'student4': 'Kadeer',
    'student5': 'Laurent',
    'student6': 'Bruno',
    'ages': [35, 24, 24, 23, 34, 19]
}

print(students_dict)
print(students_dict['student1'])

keys_students = list(students_dict)
print(keys_students)
# print(students_dict[0]) --> KeyError
print(list(students_dict)[0])

value_students = list(students_dict.values())
print(value_students[0])
print(students_dict['ages'][0])


sample_dict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
history = sample_dict['class']['student']['marks']['history']
print(history)


students_dict['student6'] = 'Tooshar'
print(students_dict)

students_dict['instructor'] = 'Damien'
print(students_dict)

del students_dict['student4']
print(students_dict)

for student in students_dict:
    if students_dict[student] == 'Joeri':
        print(f'{students_dict[student]} is present.')
        break
    else:
        print(student, students_dict[student])


print(students_dict.keys())
print(students_dict.values())
print(students_dict.items())

new_instructor = {'New Instructor': 'Nirmal'}
students_dict.update(new_instructor)
print(students_dict)


for key, val in students_dict.items():
    print(f'{key} is {val}')

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for i in keys_to_remove:
    del sample_dict[i]

print(sample_dict)