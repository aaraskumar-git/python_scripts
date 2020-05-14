import collections

person = collections.namedtuple('person', ['name', 'age', 'salary'])
p1 = person('aras', 23, 400)
print(p1)