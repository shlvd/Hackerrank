#sed -n '10p' file.txt
i=0
while read line
do
    i=$(($i+1))
    if [ $i -eq 10 ]; then
        echo $line
        break
    fi
done < file.txt
