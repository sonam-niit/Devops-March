# list (ordered, mutable, allows duplicates)
# maintains order
# you can change it (mutate)
# it allows duplicate values

my_list=[1,2,3,4,5,6,7]
print(my_list) #print entire list
print("element at index 1: ",my_list[1])
my_list.append(8) # add new item
my_list[3]=34 # change value
print(my_list) #print entire list
my_list.insert(0,20) # insert at any index
print(my_list) 
