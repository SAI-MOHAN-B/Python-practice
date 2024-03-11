from collections import Counter, namedtuple, OrderedDict

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
S = Student('mohan', '23', '1995')
print(S)

#  Ordered Dict
ord_dict = OrderedDict()
ord_dict['a'] = 2
ord_dict['b'] = 3
print(ord_dict)