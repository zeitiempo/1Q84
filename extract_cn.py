# -*- coding: utf-8 -*-

import codecs
from bs4 import BeautifulSoup as bs

with open('1Q84+jp+cn.xml') as reader:
    xml=reader.read()

soup=bs(xml,"html.parser")
ps=soup.find_all("p")

fout=codecs.open("1Q84#cn.txt","w","utf-8")
for p in ps:
    sens=p.find_all("cn")
    fout.write("\t")
    for sen in sens:
        fout.write(sen.get_text())
    fout.write("\n\n")
fout.close()
