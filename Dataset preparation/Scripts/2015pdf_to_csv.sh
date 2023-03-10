pdftotext $1 -raw -nopgbrk
txt=`echo $1 | sed -e "s/.pdf/.txt/g"`
n=`wc -l ${txt} | cut -d " " -f 1`
for(( l=1;l<=n;l++ ));do
	f=`sed -e ${l}p ${txt} -n`
	if [[ $f =~ "Register Number" ]];then
		unset subs
		declare -a subs
		#echo f=$f
		for(( i=3;i<13;i++ ));do
			subs+=(`echo $f | cut -d " " -f $i`)
			#echo $
			#echo ${subs[$((i-3))]}
		done
		#echo ${subs[@]}
	fi
	if [[ $f =~ [A-Z]{3}[0-9]{2}[A-Z]{2}[0-9]{3} ]];then
		#echo Here f=$f
		for(( i=1;i<11;i++ ));do
			if (( i==1 ));then
				echo -n `echo $f | cut -d " " -f $i`
			else
				echo -n ,${subs[$((i-2))]}\(
				echo -n `echo $f | cut -d " " -f $i`
				echo -n ')'
			fi
		done
		echo ''
	fi
done
rm ${txt}