cd ../../Dataset
echo 'Reg_No,Semester,Year,Dept,Subject,Attendance,Internal mark,Grade' > CSV-Single/1.csv
c=0
for i in `ls CSV`;do
	#i=`echo $1`
	name=`echo $i | cut -d "." -f 1`
	sem=`echo $name | cut -d "_" -f 1`
	year=`echo $name | cut -d "_" -f 2`
	dept=`echo $name | cut -d "_" -f 3`
	sub=`echo $name | cut -d "_" -f 4`
	
	for j in `cat CSV/$i`;do
		reg=`echo $j | cut -d "," -f 1`
		att=`echo $j | cut -d "," -f 2`
		int=`echo $j | cut -d "," -f 3`
		#grade='{'
		eligible=0
		
		if (( $(echo "$att >= 75" |bc -l) ));then
			scheme=19
			if (( ${#reg}==10 ));then
				if (( ${reg:3:2}<19 ));then
					scheme=15
				fi
			else
				if (( ${reg:4:2}<19 ));then
					scheme=15
				fi
			fi
			
			if (( scheme==15 ));then
				if (( $(echo "$int >= 45" | bc -l) ));then
					eligible=1
				fi
			else 
				eligible=1
			fi
		fi
		
		if (( eligible==1 ));then
			g=0
			for k in `grep $reg CSV-Finals/*`;do
				sc=`echo $k | grep ${sub}\([^,]*\) -o`
				if (( ${#sc}>0 ));then
					grade=`echo $sc | cut -d "(" -f 2 | cut -d ")" -f 1`
					#grade+='/'
					if [[ ${grade} != FE && ${grade} != I ]];then
						(( g++ ))
					fi
				fi
			done
			if (( g>1 ));then
				grade='F'
				g=1
			fi
			if (( g==1 ));then
				echo $reg,$sem,$year,$dept,$sub,$att,$int,$grade >> CSV-Single/1.csv
			fi
		fi
	done
	(( c++ ))
	echo completed ......$i.........$c/980
done