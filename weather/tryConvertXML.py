import xmltodict
import json
import os

fileName = input("Input File Name (doesn't have to include .xml): ")

with open('{0}.xml'.format(fileName)) as fd:
    doc = dict(xmltodict.parse(fd.read(),xml_attribs=True,attr_prefix = ""))["current"]


with open('result.json', 'w') as fp:
     json.dump(doc, fp, indent = 4)
     
# OPEN THE FILE
os.startfile("result.json")

                 

