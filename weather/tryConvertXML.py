import xmltodict
import json
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree import ElementTree
import io
import os

xml = """<?xml version="1.0" encoding="UTF-8"?>
<current>
  <city id="2643741" name="City of London">
    <coord lon="-0.09" lat="51.51" />
    <country>GB</country>
    <sun rise="2015-06-30T03:46:57" set="2015-06-30T20:21:12" />
  </city>
  <temperature value="72.34" min="66.2" max="79.88" unit="fahrenheit" />
  <humidity value="43" unit="%" />
  <pressure value="1020" unit="hPa" />
  <wind>
    <speed value="7.78" name="Moderate breeze" />
    <direction value="140" code="SE" name="SouthEast" />
  </wind>
  <clouds value="0" name="clear sky" />
  <visibility value="10000" />
  <precipitation mode="no" />
  <weather number="800" value="Sky is Clear" icon="01d" />
  <lastupdate value="2015-06-30T08:36:14" />
</current>"""


#o = xmltodict.parse(datasource)
#Js = json.dumps(o)jsonx,
#root = ElementTree.fromstring("<root><a>1</a></root>")
#ElementTree.dump(root)


with open('xml.xml') as fd:
    doc = dict(xmltodict.parse(fd.read(),xml_attribs=True,attr_prefix = ""))["current"]

# get attribute or not

with open('result.json', 'w') as fp:
     json.dump(doc, fp, indent = 4)
     
# OPEN THE FILE
os.startfile("result.json")



#tree = ET.parse("xml.xml")
#root = tree.getroot()
#print(root[0])


                 

