#!/usr/bin/env bash

cd pdf_data
for f in *; do
    echo "Folder -> $f"
    cd $f
    for name in *;do
        echo "file name->$name"
        pwd
        pdftotext -raw -nopgbrk $name ../../text_data/$f"_"${name::-4}.txt
        sed -i '$ d' ../../text_data/$f"_"${name::-4}.txt 

    done
    cd ..

done