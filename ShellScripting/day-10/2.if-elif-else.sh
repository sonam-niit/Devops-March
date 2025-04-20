read -p "enter your age: " age
read -p "Aye you a citizen? (yes/no): " citizen

if [ "$age" -ge 18 ] && [ "$citizen" = "yes" ]; then
    echo "You are eligible for vote"
elif [ "$age" -lt 18 ]; then
    echo "You are underage and not eligible for vote"
else 
    echo "You must be a citizen to vote"
fi