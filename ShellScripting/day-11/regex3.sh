# check some field 

email="sonam_soni@pw.skills.live"
# Check if the string contains a number

if [[ $email =~ ^[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "Valid email"
else
    echo "Invalid email"
fi