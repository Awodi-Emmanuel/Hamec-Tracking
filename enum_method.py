# python program to illusterate enumerate function

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print("Return type:", type(obj1))
print(tuple(enumerate(l1, 3)))
# changing start index to 2 from 0
print(list(enumerate(s1, 2)))
