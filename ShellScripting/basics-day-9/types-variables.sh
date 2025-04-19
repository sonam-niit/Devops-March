greeting="Good Morning" #user defined variables

echo "User Defined $greeting"
echo "Environment variable: $HOME" #predefined by System

## Special Variables
# $0 giving Script Name
# $# giving No of Arguments you have passed
# $@ show all arguments
# $? showing status of exit
# $1,$2,$3 to access individual arguments

echo "Script Name: $0"
echo "No of Arguments: $#"
echo "All Arguments: $@"
echo "Exit Status: $?"
echo "First Argument: $1"
echo "Second Argument: $2"
echo "Third Argument: $3"