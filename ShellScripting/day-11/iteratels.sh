name="sonam" #global variable
#Access command result
for file in $(ls); do
    echo "$file" ## Good Approach
    echo $file  # suggested approach
done

## Access file data
for data in $(cat emails.txt); do
    echo "$data"
done