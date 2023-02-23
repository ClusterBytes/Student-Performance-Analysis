for f in `ls ../../Dataset/CSV-Subject/*.csv`;do
	echo f $f
	year=`head -1 $f | cut -d "," -f 3`
	echo year $year
	scheme=2019
	if (( year < 2019 ));then
		scheme=2015
	fi
	mv -f -t ../../Dataset/CSV-Subject/${scheme} $f
done