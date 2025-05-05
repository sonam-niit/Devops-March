#Creating String
str1 = 'Hello'
str2 = "World"
str3 = '''
        This is My
        Multiline String.
        '''
# String Concatenation
greeting = str1 + " " + str2
print(greeting)
print(str3) # Multiline String

print(f"{str1} {str2}") #f String 
## Repeat string
print((str1+" ") * 3)

 ## Accessing String Characters
print(str1[0]) #element at 0 index
print(str1[-1]) #element at last index

# Slicing String
print(str1[0:3]) #Hel
print(str1[2:]) #llo

# String length
print('Length of Str1: ',len(str1))

# Changing Case
print('UpperCase: ',str1.upper())
print('LowerCase: ',str1.lower())

## Searching
print("lo" in str1) # either True / False
print(str1.find("lo")) # give the staring index

## Replace
new_str = str1.replace("H","W")
print(new_str)

## Split and Join
statement = "My name is sonam and I am a Devops engg"
words = statement.split()
print(words)
print("-".join(words))

#Striping Whitespaces
print("     hello     ".strip())

## Checking with Start and End value
print("Python".startswith("Py"))
print("Python".endswith("on"))