dsdir='./../../Dataset'
total=`wc -l ${dsdir}/CSV-Single/2_no_unwanted_grades.csv | cut -d ' ' -f 1` 
k=0
for i in `tail -n +2 ${dsdir}/CSV-Single/2_no_unwanted_grades.csv`;do
	sub=`echo $i | cut -d ',' -f 5`
	echo $i >> ${dsdir}/CSV-Subject/${sub}.csv
	(( k++ ))
	if(( k%1000==0 ));then
		echo $k/$total
	fi
done

