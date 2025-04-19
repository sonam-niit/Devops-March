firstName="Sonam"
lastName="Soni"
#String Concatenation
echo "Welcome $firstName $lastName"
#Arithmetic Operations
num1=10
num2=3
sum="$(($num1+$num2))"
echo  "Result: $sum"
echo  "Result: $(($num1-$num2))"
# take input from user
read -p "Enter Your Name: " user_name
echo "Hello, $user_name"