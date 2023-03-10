#/bin/bash
for i in `ls`;do
	cd $i
	for j in `ls`;do
		cd $j
		for k in `ls`;do
			cd $k
			ls *.pdf > files.txt
			n=`wc -l files.txt | cut -d " " -f 1`
			for(( l=1;l<=n;l++ ));do
				f=`sed -e ${l}p files.txt -n`
				filename=`pdftotext "$f" - -raw -f 1 -l 1 | grep -o 'Course Name'.* | cut -d " " -f 4 | cut -d "-" -f 1`
				batch=`pdftotext "$f" - -raw -f 1 -l 1 | grep -o 'Batch : '[0-9]* | cut -d " " -f 3`
				mv -T "$f" ${filename}_${batch}.pdf
 			done
			rm files.txt
			cd ..
		done
		cd ..
	done
	cd ..
done
echo \nCompleted