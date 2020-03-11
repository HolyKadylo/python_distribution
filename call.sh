#!/bin/bash
# This script polls the schedule and obtains the export output
# Executed by cronjob

source CALL_PARAMETERS
TODAY=$(date +%Y-%m-%d)
FIRSTDAY=$(date +%Y-%m)"-01"

#login
curl $URL1 -c cook.txt -H 'Accept: application/json, text/plain, */*' -H 'Referer: '$URL2 -H 'Origin: '$URL3 -H 'X-CSRF-Token: undefined' -H 'X-Key-Inflection: camel' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"email":"'$USER'","password":"'$PASS'"}' --compressed

#get month
curl $URL4$FIRSTDAY$URL5 -H 'authority: '$URL6 -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'referer: '$URL7$FIRSTDAY$URL8$TODAY$URL9 -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8,uk;q=0.7,ru;q=0.6' -b cook.txt --compressed > out.xlsx

#rm cookies
rm cook.txt
