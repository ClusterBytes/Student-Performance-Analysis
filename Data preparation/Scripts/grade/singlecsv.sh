# cd refact_text_data
# for f in *;do
#     while IFS= read -r line
#     do
#         echo "$line" 

#     done < ../out.csv
# done

cd csv_rough
cat *csv > ../combined.csv
