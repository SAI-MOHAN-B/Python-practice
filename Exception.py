# Raise an Exception
# x = -5
# if x < 0:
#     raise Exception('X should be negative')

# It is a good practice to specify the type of Exception you want to catch
# Therefore we can have the Possible Errors
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print('Only Zero Numbers are added here', e)
except TypeError as e:
    print('A type Error Occurred:', e)
else:
    print('Everything is ok')
