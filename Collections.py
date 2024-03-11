from collections import Counter,namedtuple
a = [12, 13, 13, 12, 14]
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.items())
print(my_counter.values())
print("Collections")

# Named Tuple
Student = namedtuple('Student',['name','age','DOB'])
print(Student)
S = Student('mohan','23','1995')
print(S)