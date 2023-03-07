cd ../../Dataset/CSV-Subject
for year in `ls`;do
cd $year
	for sem in `ls`;do
	cd $sem
		for dept in `ls`;do
		cd $dept
			
			rm norm* 2> /dev/null
			
		cd ..
		done
	cd ..
	done
cd ..
done