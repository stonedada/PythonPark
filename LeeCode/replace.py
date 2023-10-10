a = ['b', 'd', 'f']
s = "A%sC%sE"
for i in a:
    if s.find('%s') != -1:
        s = s.replace('%s', i, 1)
    else:
        s += i
print(s)

a = [1, 2, 4, 4, 56, 5]
for index, num in enumerate(a):
    print(index, num)
