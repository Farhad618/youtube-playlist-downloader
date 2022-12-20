#!usr/bin/env bash

file="templink.txt"
i=1
while read -r line; do
    IFS="="
    
    read -ra arr <<< "$line"
    h=`hURL -us ${arr[-1]}`

    wget -O "$h.mp4" "$line"
    i=`expr $i + 1`
done <$file 
