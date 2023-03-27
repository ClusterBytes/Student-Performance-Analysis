#!/bin/bash
echo "hoo"

while read line; do
    key=$(echo $line | cut -d ' ' -f 1)
    value=$(echo $line | cut -d ' ' -f 3)  
    data=$(echo $data | jq --arg k "$key" --arg v "$value" '. + { ($k): [ $v ] }')
done < 2019.txt