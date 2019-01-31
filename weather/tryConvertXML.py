import xmltodict
import json
import os

fileName = ""

def fillFileName():
    global fileName
    print ("(In this folder, there is weather.xml file alreadyt to test) ")
    fileName = input("Input File Name (doesn't have to include .xml) : "  )

while(True):
    try :
        fillFileName()
        os.startfile("{0}.xml".format(fileName))

        break
    except:
        print("Wrong File Name or File Couldn't be opened")
        
    
with open('{0}.xml'.format(fileName)) as fd:
    doc = dict(xmltodict.parse(fd.read(),xml_attribs=True,attr_prefix = ""))["current"]


with open('result.json', 'w') as fp:
     json.dump(doc, fp, indent = 4)

input("----ENTER TO OPEN JSON FILE----")

     
# OPEN THE FILE
try :
    os.startfile("result.json")
    print("CONVERT DONE")
except :
    print("There's sth wrong trying to open json file")

                 

