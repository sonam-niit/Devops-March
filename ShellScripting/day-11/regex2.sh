String="387-654-3212"
# Check if the string contains a number

if [[ $String =~ ^[7-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
    echo "Mobile Pattern Found"
else
    echo "No Match Found"
fi