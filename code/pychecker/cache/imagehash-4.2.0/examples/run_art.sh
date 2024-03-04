
for j in 2 3 4 5 6 7 8 9 10 11
do
echo "${j} ..."
paste urls.txt hashes.txt |
grep -v '0000000000000000 0000000000000000 0000000000000000' | 
awk '{ print $1,$'$((j+1))'}' > hashesfull.txt

<hashesfull.txt sort -k2,2 | uniq -f 1 -D | awk '{print $2}' | uniq | 
while read k; do 
{ echo "<h1>Cluster $k</h1>"; awk '($2 == "'"$k"'"){print $1}' hashesfull.txt | 
while read path; do echo "<a href='${path}'><img src='${path}' /></a>"; done
}
done > art${j}.html
done
