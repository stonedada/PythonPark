res = 0
mxnum = 1
s = "abbcbe"
index = 1
step = 0
while index <= len(s):
    if index == len(s):
        index = 0
    print(index)
    if s[index] == s[index-1]:
        mxnum += 1
    else:
        mxnum = 1
    res = max(mxnum, res)
    if res >= len(s) or step > 2*len(s):
        break
    index += 1
    step += 1
print(res)
