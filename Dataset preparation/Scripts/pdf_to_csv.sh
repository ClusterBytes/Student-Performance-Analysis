pdftotext $1 -raw -nopgbrk
t=`echo $1 | cut -d "." -f 1`
sed -i -f col_row.sed $t.txt
sed -i -f row_to_csv.sed $t.txt
rows=`grep -E [A-Z]{3}[0-9]{2}[A-Z]{2}[0-9]{3},[0-9]*\.[0-9]*,[0-9]*\.[0-9]*/[0-9]* $t.txt`
for row in $rows;do
	reg=`echo ${row} | cut -d "," -f 1`
	att=`echo ${row} | cut -d "," -f 2`
	int=`echo ${row} | cut -d "," -f 3 | cut -d "/" -f 1`
	out=`echo ${row} | cut -d "," -f 3 | cut -d "/" -f 2`
	Int=$(echo "scale=3; ($int*100)/$out" | bc)
	echo $reg,$att,$Int
done
rm $t.txt