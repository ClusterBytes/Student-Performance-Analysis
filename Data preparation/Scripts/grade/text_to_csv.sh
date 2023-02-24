cd refact_text_data

for f in *;do
    cp $f ../csv_rough/${f%????}.csv 
done