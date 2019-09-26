# esdawet 
Retriving and Sending Whatsapp Using BAKWAN and DAWET

# Installation
```sh
pip install -r requirements.txt 
```

# How to use
to using this program : 
```python
from lib import dawet, bakwan  
import time  
  
sending     = bakwan.Bakwan()  
getNilai    = dawet.Dawet("2019Proyek2")  
getWa       = dawet.Dawet("datamahasiswa")  
  
#get data wa_ortu, npm, name  
wanumortu   	= getWa.getData("row name", "column name", 0)  
wanumpem    	= getWa.getData("row name", "column name", 0)  
npmnum      	= getWa.getData("row name", "column name", 0)  
name        	= getWa.getData("row name", "column name", 0) 
truemessage 	= "Anak anda dengan npm : " + npmnum + " " + name + " belum melaksanakan bimbingan!" 
falsemessage	= "Anak anda dengan npm : " + npmnum + " " + name + " telah melaksanakan bimbingan!"
  
if getNilai.getData("row name", "column name", 0) == "0":  
    #sending message  
    sending.sendNumber(wanumortu, truemessage)  
    time.sleep(1)  
    sending.sendNumber(wanumpem, truemessage)  
else:  
    #sending message  
    sending.sendNumber(wanumortu, falsemessage)  
    time.sleep(1)  
    sending.sendNumber(wanumpem, falsemessage)
```

# NOTE!!
1. add your **client_secret.json** for google spreadsheet api
2. create **lib** directory then create **__init__.py** file in **lib** directory, then put **bakwan.py** and **dawet.py** to **lib** directory