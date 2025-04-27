# cannot chnage the value after creation (immutable)
# order is preserved
# duplicates are allowed
# written with round brackets

my_tuple = (1,2,3,4,5,2)
print(my_tuple)
print("element at index 2: ",my_tuple[2])
print("element at index -1: ",my_tuple[-2])
# my_tuple[0]=10
#throw error of assignment