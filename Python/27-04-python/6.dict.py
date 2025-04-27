# written in {}
# store values in key value pair
# key must be unique, values canbe duplicated

my_dict={"name":"sonam soni","age":"35","city":"mumbai"}
print(my_dict)
print("Name: ",my_dict["name"])
my_dict['manager']="test manager" # add new
# for loop
for key in my_dict:
    print(key,": ",my_dict[key])
my_dict.pop('age')
print(my_dict)
my_dict.popitem() # removes last pair
print(my_dict)
