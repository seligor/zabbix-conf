#!/usr/bin/python3
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re

f=open(r'/usr/lib/zabbix/externalscripts/st_site_check/ActualVersion.txt',"wb")
ufr = requests.get('https://falcongaze.com/download/p-HlWXkcN9Ae1YXuA/securetower/ActualVersion.txt', verify=False)
f.write(ufr.content)
f.close()
pattern = re.compile('(\d\.\d\.\d{3,4})')
for i, line in enumerate(open('/usr/lib/zabbix/externalscripts/st_site_check/ActualVersion.txt')):
    for match in re.finditer(pattern, line):
        actver = str(match.group(1))

print(actver)
