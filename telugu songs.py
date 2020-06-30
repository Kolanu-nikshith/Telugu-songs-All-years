from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import os.path
import errno


try:
	os.mkdir(os.path.join('E:\\',"years"))
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass

for q in range(2000,2021):
	req = Request('https://naasongs.fm/'+str(q)+'-telugu-all-album-songs/', headers={'User-Agent': 'Mozilla/5.0'})
	resp = urlopen(req).read()
	lines=[]

	bsObj = BeautifulSoup(resp,features="html.parser");
	for x in bsObj.findAll('p'):
	    for i in x.findAll('a',href=True):
	    	lines.append(i.get('href'))

#	fi = ""+str(q)+"m.txt"
#	lines = open(fi, "r").readlines()
	
	print("*********Downloading "+str(q)+" year songs*********")
	try:
		os.mkdir(os.path.join('E:\\years\\',str(q)))
	except OSError as exc:
	    if exc.errno != errno.EEXIST:
	        raise
	    pass

	for line in lines:
		try:
			req = Request(line, headers={'User-Agent': 'Mozilla/5.0'})
			resp = urlopen(req).read()
			bsObj = BeautifulSoup(resp,features="html.parser");

			fold =  bsObj.select('h1.pst_title')[0].text.strip().rsplit(' ', 1)[0]		

			try:
				os.mkdir(os.path.join('E:\\years\\'+str(q),fold))
			except OSError as exc:
			    if exc.errno != errno.EEXIST:
			        raise
			    pass

			for link in bsObj.findAll('a', {'class': 'dlink anim'}):
			    url=link['href']
			    r = requests.get(url, allow_redirects=True)
			    name=url.rsplit('/', 1)[1].replace("%20"," ")
			    filepath="E:\\years\\"+str(q)+"\\"+fold+"\\"+name
			    open(filepath, 'wb').write(r.content)
			    print(fold+">"+name+" downloaded")

		except Exception as e:
			print(e)



