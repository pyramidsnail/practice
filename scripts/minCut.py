import sys, os, re
import random

f=open("kargerMinCut.txt")
#f=open("test")
dic={}
for line in f.readlines():
    items=line.strip().split()
    dic[items[0]]=items[1:]

    

min=100000
for i in range(100000000):
    cdic=dic
    while len(cdic)>2:
	    sap=random.sample(cdic.keys(),2)
	    for key in cdic.keys():
	        if key!=sap[0] and key!=sap[1]:
                	for j in range(len(cdic[key])):
                    		if cdic[key][j]==sap[1]:
                        		cdic[key][j]=sap[0]
	            # for item in cdic[key]:
	            #     if item==sap[1]:
                #         	item=sap[0]

            cdic[sap[0]]=[x for x in cdic[sap[0]] if x!=sap[1]]
            cdic[sap[1]]=[x for x in cdic[sap[1]] if x!=sap[0]]
            cdic[sap[0]].append(cdic[sap[1]])
            del cdic[sap[1]]

    cut=len(cdic.itervalues().next())
    if cut<min:
        min=cut

print min
	    