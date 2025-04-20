# enhanced loop which using range directly
for i in {1..5}; do
    echo "Number $i"
done
## using C style
for ((i=1; i<=5; i++)); do
    echo "Count: $i"
done
## using C style odd numbers
for ((i=1; i<=10; i+=2)); do
    echo "Count: $i"
done
## print even numbers using seq command
for i in $(seq 2 2 20); do
    echo "Number $i"
done
