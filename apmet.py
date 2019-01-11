import elasticsearch
from bson.json_util import dumps
es = elasticsearch.Elasticsearch() 
import urllib2, re, bs4
from bson.json_util import dumps
soup = bs4.BeautifulSoup(urllib2.urlopen("http://localhost/server-status"),"lxml")
dla=soup.find("dl").find_next("dl")
count=6
ls=[]
mydict={}
for dict_ex in dla.find_all("dt"):
	ptr=dict_ex.text.split(":",1)
	#dict_met = zip(ptr)
	mydict.update(dict([ptr]))
	count=count-1;
	if(count<1):
		break


fdict={}
fdict["servstat"]=mydict	
print(dumps(fdict))
print("\n")
es.index(index='posts', doc_type='blog', id=1,body=dumps(fdict))
print(dumps(es.get(index='posts', doc_type='blog', id=1)))
