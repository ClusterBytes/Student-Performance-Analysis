#!/usr/bin/env bash
echo "recieved $1" 
position=$(python3 find_column.py $1)
echo "position $position"
python3 seperate_sub.py $1 $position
read -p "Do you want to remove empty rows? (yes/no): " response

if [[ "$response" =~ ^(yes|y)$ ]]; then
    filt=true
else
    filt=false
fi

if $filt;then
    echo "removing empty rows"
    awk -F',' '$2 != "0.0" || $3 != "0.0" || $4 != "0.0" || $5 != "F"' $1.csv > filtered_$1.csv
    
fi

python3 encode_sub.py $1 $position $filt
python3 train_sub.py $1 $position
find -type f -name "*.csv" | grep -v "trained" | xargs rm

libreoffice "trained_$1.csv"
