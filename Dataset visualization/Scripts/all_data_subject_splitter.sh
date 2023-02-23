for i in `cut -d "," -f 5 ./../../1.csv | sort | uniq | head -n -1`;do
	echo $i ${i}
done