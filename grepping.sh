# adding carriage returns
sed 's/last_payroll_date/\n/g' out > out2

# adding first names to firstnames
grep -o -P "first_name_eng.{0,20}" out2 > firstnames

#trimming leading junk
sed 's/first_name_eng":"//g' firstnames > firstnames2

#adding str=
sed 's/^/str=\"/g' firstnames2 > firstnames3
#adding echoing
sed 's/$/\" ; echo ${str%,*}/g' firstnames3 > firstnames4
chmod +x firstnames4

# TODO bug: max  length breaks the script when executed incorrectly
# adding second names to secondnames and doing the same as above
grep -o -P "last_name_eng.{0,21}" out2 > lastnames
sed 's/last_name_eng":"//g' lastnames > lastnames2
sed 's/^/str=\"/g' lastnames2 > lastnames3
sed 's/$/\" ; echo ${str%,*}/g' lastnames3 > lastnames4
chmod +x lastnames4

./firstnames4 > firstnames
./lastnames4 > lastnames
rm firstnames2 firstnames3 firstnames4 lastnames2 lastnames3 lastnames4
echo "ready"
