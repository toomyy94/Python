list = [1, 2, 3, 4, 5, 6]
print(list)

print(list[-1:])

list[len(list)-1] = 5
print(list)

list.append(7)
print(list)


print(list[:4])
print(list[2:5])

list.insert(0, 0)
print(list)

list.pop()
print(list)

print(list[:-1])