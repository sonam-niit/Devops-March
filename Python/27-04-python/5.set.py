# unordered (no index)
# mutable (we can add/remove)
# no duplicates
# written in curly brackets

my_set = {1,2,3,4,5,6,2,4}
print(my_set)
my_set.add(10)
print('after add 10: ',my_set)
my_set.remove(3)
print('after remove 3: ',my_set)
print('remove last: ',my_set.pop(), "removed")
print(my_set)