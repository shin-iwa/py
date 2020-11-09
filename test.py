d = {
    "apple":100,
     "banana":200,
     "kiwi":300
}

for k in d.values():
  print(k)

oldlist = [1,2,3,4,5,6,7]
newlist = []
for item in oldlist:
  if item % 2 == 0:
    newlist.append(item)
  else:
    newlist.append(1)

print(newlist)