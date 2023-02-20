#bin/bash/env

cd s2pdf

for f in *; do
    echo "file name -> $f"
    tr -d '\n'  <$f> ../refact_text_data/out.txt;
    sed 's/KSD/\n&/g' ../refact_text_data/out.txt >../refact_text_data/p.txt;
    sed -E -e 's/APJ.*|ELECT.*|COMP.*|CIVIL.*|INFO.*|Exam.*|BTech.*//' ../refact_text_data/p.txt >../refact_text_data/k.txt;
    sed 's/./&,/10' ../refact_text_data/k.txt>../refact_text_data/$f
    sed -i '1d' ../refact_text_data/$f
    echo "refactored->$f"
done
rm ../refact_text_data/out.txt ../refact_text_data/p.txt ../refact_text_data/k.txt