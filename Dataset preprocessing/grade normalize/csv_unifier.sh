echo 'Reg_No,Semester,Year,Dept,Subject,Attendance,Internal mark,Grade' > ../../Dataset/CSV-Single/3_grade_normalized.csv
cd ../../Dataset/CSV-Subject
for year in `ls`;do
cd $year
	for sem in `ls`;do
	cd $sem
		for dept in `ls`;do
		cd $dept
			
			echo "$year $sem $dept"
			
			if(( year<2019 ));then
				cat norm* >> ../../../../CSV-Single/3_grade_normalized.csv
			else
				cat * >> ../../../../CSV-Single/3_grade_normalized.csv
			fi
			
		cd ..
		done
	cd ..
	done
cd ..
done