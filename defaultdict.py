from collections import defaultdict

emp = {'aras': 'blr',
       'chiddhu': 'blr',
       'anand': 'chennai',
       'suresh': 'warrington',
       'anantha': 'warrington',
       'selvam': 'mumbai'}
employees = dict()

for name, city in emp.items():
    if city in employees.keys():
        employees[city].append(name)
    else:
        employees[city] = [name]
print(employees)
