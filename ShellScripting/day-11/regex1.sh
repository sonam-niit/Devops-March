ip=192.168.1.1
# Check if the IP address is valid
if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
    echo "Valid IP address"
else
    echo "Invalid IP address"
fi

String="My Number is 121345873 should match with some pattern 872832"
# Check if the string contains a number

if [[ $String =~ [0-9]{8} ]]; then
    echo "String contains 8 digits in row"
else
    echo "No Match Found"
fi