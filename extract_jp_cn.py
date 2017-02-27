# -*- coding: utf-8 -*-

import codecs
from bs4 import BeautifulSoup as bs

with open('1Q84+jp+cn.xml') as reader:
    xml=reader.read()

soup=bs(xml,"html.parser")
ps=soup.find_all("p")

fout=codecs.open("1Q84#jp#cn.txt","w","utf-8")
for p in ps:
    #fout.write(p["id"]+":\n")
    sens=p.find_all()
    for sen in sens:
        fout.write("\t["+sen["id"]+"]:"+sen.get_text()+"\n")
    fout.write("\n")
fout.close()
