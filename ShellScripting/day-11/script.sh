awk -F',' '{
    for (i=1;i<=NF;i++){
        if($i ~ /^[a-z]+@[a-z]+\.[a-z]+$/ )
            print $i
    }
}' email.txt

-F',' : set comma as a field seperator
NF: Number of fields in current line
$i each field

pattrn then file name