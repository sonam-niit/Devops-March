#Declaration
declare -A capitals
# Key-value pair assign
capitals[India]="New Delhi"
capitals[France]="Paris"
capitals[Japan]="Tokyo"
## Access
echo "Capital of Japan is ${capitals[Japan]}" 
## iterate directly with values
# ${capitals[@]} expands values directly
for capital in "${capitals[@]}"; do 
    echo "$capital"
done
## Iterate with keys
## ! expands keys 
for country in "${!capitals[@]}"; do 
    echo "Capital of $country is ${capitals[$country]}"
done



