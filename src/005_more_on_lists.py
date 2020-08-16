my_favs = ['Balaji', 'Gubli', 'Adhithya', 'Surya', 'Pranav', 'Madhav', 'Maya', 'Manasa']
print(my_favs)

my_favs.append('Vani')
print(my_favs)

my_favs.insert(5, 'Padma')
print(my_favs)

del_indx = 0
del my_favs[del_indx]
print(my_favs)
print(my_favs[del_indx])

del_indx = len(my_favs)-1
del my_favs[del_indx]
print(my_favs)

end=my_favs.pop()
print(my_favs)
print(end)

third=my_favs.pop(3)
print(my_favs)
print(third)

my_favs[2] = 'Thulasi'
print(my_favs)
