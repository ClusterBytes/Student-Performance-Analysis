# sed -e 's/.*Register\(.*\)Register.*/\1/' 2015_common.txt

for var in 12
do
    # reg_pos=`grep -hnr  "Register"  2015_common.txt  |cut -d : -f 1  |head -n$var`
    num=$(($var+1))
    next_reg_position=`grep -hnr  "Register"  2015_common.txt  |cut -d : -f 1  |head -n$(($var+1))`
    echo $next_reg_position
    # for i in $reg_pos
    # do       
    #     echo $i
    # done
done