my_num = 7 # this is an integer variable
my_num_type = type(my_num)
print('Type of my_num is:', my_num_type, my_num)

my_num = True # this is a boolean variable
my_num_type = type(my_num)
print('Type of my_num is:', my_num_type, my_num)

my_num = '7' # this is a string variable
my_num_type = type(my_num)
print('Type of my_num is:', my_num_type, my_num)

my_num_as_num = int(my_num)
my_num_type = type(my_num_as_num)
print('Type of my_num is:', my_num_type, my_num_as_num)

my_num_as_num = float(my_num)
my_num_type = type(my_num_as_num)
print('Type of my_num is:', my_num_type, my_num_as_num)

my_num_as_str = str(my_num_as_num)
my_num_type = type(my_num_as_str)
print('Type of my_num is:', my_num_type, my_num_as_str)

print(str(3.999999999999999))
print(str(3.9999999999999999))

my_bool = 'False'
print('my bool type: ', bool(my_bool))
my_bool = 'True'
print('my bool type: ', bool(my_bool))
my_bool = ''
print('my bool type: ', bool(my_bool))
my_bool = 0
print('my bool type: ', bool(my_bool))
my_bool = 1
print('my bool type: ', bool(my_bool))
my_bool = -1
print('my bool type: ', bool(my_bool))
