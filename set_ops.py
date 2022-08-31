my_set = {"Jan", "Feb", "Feb", 1}

print(type(my_set))
print(len(my_set))
my_set.remove("Jan")
print(len(my_set))

my_set.add("March")
my_set.add("April")

print(my_set)
my_set.pop()
print(my_set)
