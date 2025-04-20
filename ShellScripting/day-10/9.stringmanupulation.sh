string="Hello, World!"
## Sub String
echo ${string:7:6}
## Pattern Replacement
echo ${string//World/Sonam Soni}

## awk 
## powerful text processing tool which used to maunuplate string
#gsub (substitution)
#sed (Stream Editor)

echo $string | awk '{gsub(/World/, "Users"); print}'

echo $string | sed 's/World/Users/g'