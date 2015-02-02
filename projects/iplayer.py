from lxml import html, etree
import requests
from bs4 import BeautifulSoup
import re, os

page = requests.get('http://www.iplayerconverter.co.uk/r/7/aod/default.aspx')
soup = BeautifulSoup(page.text)
# for item in soup.find_all('tr'):
#     soup.item = BeautifulSoup(item.string)
#     nouk = soup.item.find_all('stream-nonuk-audio_streaming_wma_low_nonuk')
#     print nouk
    

# nouk = tree.xpath('//table/tbody/tr')
# print soup.body.table.tr
titlelist=[]
count = 0
titles = soup.find_all('td')
for title in titles:
    if count%4 == 0:
        titlelist.append(title.string)
    count += 1
        

linklist=[]
links = soup.find_all('a')
for link in links:
    if re.search('stream-nonuk-audio_streaming_wma_low_nonuk',link.get('href')):
        # print link.get('href')
        linklist.append(link.get('href'))

for i in xrange(len(titlelist)):
    filename = titlelist[i].lstrip('u\'').rstrip('\'')
    if not os.path.exists(filename+'.wma'):
        source = requests.get(linklist[i])
        sourceSoup = BeautifulSoup(source.text)
        sourceLink = sourceSoup.find('ref').get('href')
        cmd = 'mimms '+sourceLink+''+filename
        os.system(cmd)
            
