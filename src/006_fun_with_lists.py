my_favs = ['Gubli', 'Maya', 'Manasa', 'Vani', 'Padma', 'Bhuvana', 'Naveena', 'Regina', 'Kavitha']
my_nums = [6,2,9,4,8,1,7]

# In place Sort and Reverse function... cannot undo the operation... original will be lost
#
#print(my_favs)
#my_favs.sort()
#print(my_favs)
#my_favs.reverse()
#print(my_favs)
#
#print(my_nums)
#my_nums.sort()
#print(my_nums)
#my_nums.reverse()
#print(my_nums)

my_sorts = sorted(my_favs)
print(my_favs)
print(my_sorts)
my_sorts = sorted(my_favs, reverse=True)
print(my_sorts)
my_rev = list(reversed(my_favs))
print(my_rev)

my_sorts = sorted(my_nums)
print(my_nums)
print(my_sorts)
my_sorts = sorted(my_nums, reverse=True)
print(my_sorts)
my_rev = list(reversed(my_nums))
print(my_rev)
