cat github-urls.txt | while read url; do git clone $url; done

find -name '*.svg' | while read path; do convert $path ${path/.svg/.png}; done

echo "collecting files ..."
for i in */; do pushd $i >/dev/null; prefix=$(git remote get-url origin|sed 's,https://github.com/,https://raw.githubusercontent.com/,g'); find */ -name '*.svg' | while read path; do test -e "${path/.svg/.png}" && echo $prefix/master/$path $prefix; done; popd >/dev/null; done |
grep -Ev '\.min\.' > urls.txt
echo "hashing ..."
for i in */; do pushd $i >/dev/null; prefix=$(git remote get-url origin|sed 's,https://github.com/,https://raw.githubusercontent.com/,g'); find */ -name '*.svg' | while read path; do test -e "${path/.svg/.png}" && echo $i/${path/.svg/.png}; done; popd >/dev/null; done|
grep -vE '\.min\.' | xargs python3 ~/Downloads/imagehash/hashimage.py > hashes.txt

for j in 2 3 4 5 6 7 8 9 10 11 12
do
echo "${j} ..."
paste urls.txt hashes.txt | grep -v '0000000000000000 0000000000000000 0000000000000000' |
awk '{print $1,$2,$'$((j+2))'}' > urlhashes.txt
sort -k3,3 urlhashes.txt | uniq -f 2 -D | awk '{print $3}' | uniq | 
while read k; do 
{ echo "<h1>Cluster $k</h1>"; awk '($3 == "'$k'"){print "<a href=\""$2"\"><img loading=\"lazy\" src=\""$1"\" width=\"64\" /></a> "}' urlhashes.txt; }
done > index${j}.html
done
