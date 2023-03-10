dsdir='./../../Dataset'
total=`wc -l ${dsdir}/CSV-Single/2_no_unwanted_grades.csv | cut -d ' ' -f 1` 
k=0
cd ${dsdir}
for i in `tail -n +2 CSV-Single/2_no_unwanted_grades.csv`;do
	sem=`echo $i | cut -d ',' -f 2`
	year=`echo $i | cut -d ',' -f 3`
	dept=`echo $i | cut -d ',' -f 4`
	sub=`echo $i | cut -d ',' -f 5`
	
	if(( k==0 ));then
		cd CSV-Subject
	fi
		mkdir ${year} 2> /dev/null
		cd $year
			mkdir ${sem} 2> /dev/null
			cd $sem
				mkdir ${dept} 2> /dev/null
				cd $dept
					
					echo $i >> ${sub}.csv
					cd ..
				cd ..
			cd ..
			

	
	if(( k%1000==0 ));then
		echo $k/$total
	fi
	(( k++ ))
done

