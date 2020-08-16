letters = list('abcdefghijklmnopqrstuvwxyz')
print(letters)

#start index is inclusive, end index is not inclusive
selected = letters[2:5]
print(selected)

# get every other letter
every_other = letters[0:len(letters):2]
print(every_other)
every_other = letters[::2]
print(every_other)
every_other = letters[1:len(letters):2]
print(every_other)
every_other = letters[1::2]
print(every_other)
every_other = letters[4:len(letters):5]
print(every_other)
every_other = letters[8:len(letters):100]
print(every_other)

## Slice & Reverse
every_other = letters[::-1]
print(every_other)
