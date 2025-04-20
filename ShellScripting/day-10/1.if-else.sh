# read -p "enter first number" num1
echo "enter first number"
read num1
echo "enter second number"
read num2

if [ $num1 -ge $num2 ]; then
    echo "$num1 is greater"
else
    echo "$num2 is greater"
fi