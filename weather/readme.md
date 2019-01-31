# CONVERT XML TO JSON
This file will convert weather XML from given issue

## Method To run Weather XML : After going to source of folder weather 
befor going to the step pls run this command
```
pip install xmltodict
```
- Terminal & Cmd : 
```
python tryConvertXML.py
```
and Then it will ask to fill the fileName you want to convert, fill weather if want to test default
```
Input File Name (doesn't have to include .xml) : weather
```

## Usage
```python
import xmltodict
# changing xml to dict form
obj xmltodict.parse(xml)
import json
# serialize obj to be json format
json.dump(obj)

import os
# If you want to open file from script
os.startfile("fileName")
```

## Info
In this folder , there will be exmple of xml file to be ready to try
and after you run this code you will automatically see the json will be opened automatically
