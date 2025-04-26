#array Declaration
names=("alex" "john" "catty" "bob" "devid")

#Access elements
echo "First ele: ${names[0]}" #first element
echo "Third Element: ${names[4]}" #third element

##Access length
echo "Total Names: ${#names[@]}"

#Change Array Elements
names[1]="John Doe"
echo "changed ele: ${names[1]}"
# Access All

for name in "${names[@]}"; do 
    echo "$name"
done
## iterate and store all values in one variable and lastly print variable
## after completing the loop
result=''
for name in "${names[@]}"; do 
    result+="$name ,"
done
echo "$result"