echo "recieved $1" 
position=$(python3 find_column.py $1)
echo "position $position"
python3 seperate_sub.py $1 $position
awk -F',' '$2 != "0.0" || $3 != "0.0" || $4 != "0.0" || $5 != "F"' $1.csv > filtered_$1.csv
echo "removed the zeros"
python3 encode_sub.py $1 $position
python3 train_sub.py $1 $position
find -type f -name "*.csv" | grep -v "trained" | xargs rm

libreoffice "trained_$1.csv"
