for i in `ls PDF`;do
	for j in `ls PDF/$i`;do
		for k in `ls PDF/${i}/${j}`;do
			for l in `ls PDF/${i}/${j}/${k} | grep .*\.pdf`;do
				txt=`echo $l | cut -d "." -f 1`
				echo $l
				./pdf_to_csv.sh PDF/${i}/${j}/${k}/$l > CSV/${i}_${j}_${k}_${txt}.csv
				echo completed
 			done
			echo completed ....$k
		done
		echo completed ...........$j
	done
	echo completed ...................$i
done
echo All set
