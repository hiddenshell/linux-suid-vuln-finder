import requests
import os
import time
import sys
import subprocess
import bs4

gtfobins_url = 'https://gtfobins.github.io/gtfobins/'
find_cmd = 'find / -perm -u=s -type f 2>/dev/null'

print("Running SUID Vuln Finder")
def find_vuln(target):
    respose = requests.get(gtfobins_url+target).content

    if '<h2 id="suid" class="function-name">' in respose.decode():
        return bs4.BeautifulSoup(respose, 'html.parser').find_all('ul', class_='examples')[0].pre.text


# ###for automate 

# find_result = subprocess.run(find_cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
# results = find_result.stdout

### for manual
file_path = open('suid.txt','r')
results = file_path.read()


results = results.split('\n')
for result in results:
	result = result.split('/')[-1]
	vuln_result = find_vuln(result)
	if vuln_result:
		print(f'SUID Vuln Found in: {result}') 
		print(vuln_result)
		print()
	