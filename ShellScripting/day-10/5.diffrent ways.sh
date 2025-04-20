read -p "enter your age: " age
read -p "Are you a citizen? (yes/no): " citizen


if [[ $age -ge 18 && $citizen = "yes" ]] ; then
        echo " You are eligible for vote "
else
        echo " You are not eligible "
fi

# you can go for complex operations
if [ $age -ge 18 -a $citizen = "yes" ] ; then
        echo " You are eligible for vote "
else
        echo " You are not eligible "
fi
