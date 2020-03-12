#!/bin/bash
# This script polls the schedule and obtains the export output
# Executed by cronjob

source CALL_PARAMETERS
TODAY=$(date +%Y-%m-%d)
FIRSTDAY=$(date +%Y-%m)"-01"

#gotohomepage
curl 'https://'$URL1'/' -H 'authority: '$URL1 -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8,uk;q=0.7,ru;q=0.6' -c cook.txt --compressed

#login
curl 'https://'$URL2'/schedule/sign_in' -H 'Accept: application/json, text/plain, */*' -H 'Referer: https://'$URL1'/sign-in' -H 'Origin: https://'$URL1 -H 'X-CSRF-Token: undefined' -H 'X-Key-Inflection: camel' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"email":"'$USER'","password":"'$PASS'"}' -c cook.txt --compressed

#goto first fetch page
curl 'https://'$URL2'/schedule/schedule?q%5Buser_profile_legacy_department_id_eq%5D=4&tz=Europe%2FKiev&date='$FIRSTDAY'&mode=month' -H 'Accept: application/json, text/plain, */*' -H 'Referer: https://'$URL1'/home?searchDate='$FIRSTDAY'&prevSearchDate='$TODAY'&tz=Europe%2FKiev&viewMode=month&legacyDeptId=4' -H 'Origin: https://'$URL1 -H 'X-Key-Inflection: camel' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'Content-Type: application/json;charset=utf-8' -c cook.txt --compressed

#switching to day
curl 'https://'$URL2'/schedule/schedule?q%5Buser_profile_legacy_department_id_eq%5D=4&tz=Europe%2FKiev&date='$TODAY'&mode=day' -H 'Accept: application/json, text/plain, */*' -H 'Referer: https://'$URL1'/home?searchDate='$TODAY'&prevSearchDate='$TODAY'&tz=Europe%2FKiev&viewMode=day&legacyDeptId=4' -H 'Origin: https://'$URL1 -H 'X-Key-Inflection: camel' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'Content-Type: application/json;charset=utf-8' -c cook.txt --compressed

#exporting
curl 'https://'$URL2'/schedule/schedule/export?q%5Buser_profile_legacy_department_id_eq%5D=4&tz=Europe%2FKiev&date='$TODAY'&mode=day&format=xlsx&shifts_format=timestamps&include_tracker=true' -H 'authority: '$URL2 -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'referer: https://'$URL1'/home?searchDate='$TODAY'&prevSearchDate='$TODAY'&tz=Europe%2FKiev&viewMode=day&legacyDeptId=4' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8,uk;q=0.7,ru;q=0.6' -b cook.txt -c cook.txt --compressed > kh.xlsx

#switching to dn
curl 'https://'$URL2'/schedule/schedule?q%5Buser_profile_legacy_department_id_eq%5D=53&tz=Europe%2FKiev&date='$TODAY'&mode=day' -H 'Accept: application/json, text/plain, */*' -H 'Referer: https://'$URL1'/home?searchDate='$TODAY'&prevSearchDate='$TODAY'&tz=Europe%2FKiev&viewMode=day&legacyDeptId=53' -H 'Origin: https://'$URL1 -H 'X-Key-Inflection: camel' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'Content-Type: application/json;charset=utf-8' -c cook.txt --compressed

#exporting
curl 'https://'$URL2'/schedule/schedule/export?q%5Buser_profile_legacy_department_id_eq%5D=53&tz=Europe%2FKiev&date='$TODAY'&mode=day&format=xlsx&shifts_format=timestamps&include_tracker=true' -H 'authority: '$URL2 -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'referer: https://'$URL1'/home?searchDate='$TODAY'&prevSearchDate='$TODAY'&tz=Europe%2FKiev&viewMode=day&legacyDeptId=53' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8,uk;q=0.7,ru;q=0.6' -b cook.txt --compressed > dn.xlsx

#rm cookies
rm cook.txt
