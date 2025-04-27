#!/bin/bash
path1="./sonam"
cd $path1
 echo "#####creating new directory#####"
mkdir backup
echo "####Created New Direction Now Cpying txt file####"
path2="./backup"
for f in  "$path1"; do
    cp -v  "$f" $path2
    echo "File copied"
done
echo "####now renaming the files with date stamp####"
timestamp=$(date "+%YY-%MM-%DD")
mv $f $f.$timestamp
