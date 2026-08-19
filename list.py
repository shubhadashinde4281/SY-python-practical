list=[1,2,3,4]
print(list)

print(list[1])

list[0]=5
print(list)

list.append(6)
print(list)

list.insert(0,7)
print(list)

list.extend([7,8,9,"a","b","c"])
print(list)

list.remove(2)
print(list)

list.pop(9)
print(list)

del list[3]
print(list)

print(len(list))


if 1 in list:
    print("Element is present")

else:
    print("Element is absent")

for i in list:
    print(i)


print(list.count(3))

print(list.index(7))

list2=[7,8,9]

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

newlist=list2.copy()
print(newlist)

list.clear()
print(list)




