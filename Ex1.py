from modules import module_d

st_dict = {
    'name': 'Serena Bozheku',
    'school': 'AUBG',
    'grades': [95.56, 79.99, 100.00]
}

print(st_dict)

grade = input('Enter all the grades separated by ",": ')

grades = list(map(float, grade.split(",")))

for k in grade:
    module_d.add_grade(st_dict, k)

print(st_dict)