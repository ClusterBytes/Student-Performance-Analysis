dsdir='./../../Dataset'
file="${dsdir}/CSV-Single/2_no_unwanted_grades.csv"
j=0
for i in `cat ${dsdir}/CSV-Single/1.csv`;do
	if (( j==0 ));then
		echo 'Reg_No,Semester,Year,Dept,Subject,Attendance,Internal mark,Grade' > ${file}
	elif (( j>1 ));then
		grade=`echo $i | cut -d "," -f 8`
		if [[ ${grade} != Absent && ${grade} != Debarred && ${grade} != Withheld && ${grade} != 'Withheld*' && ${grade} != FE ]];then
			if [[ ${grade} == 'O[S]' || ${grade} == 'O' ]];then
				echo `echo $i | grep .*, -o`S >> ${file}
			else 
				echo $i >> ${file}
			fi
		fi
	fi
	if (( j%1000==0 ));then
		echo $j
	fi
	(( j++ ))
done;