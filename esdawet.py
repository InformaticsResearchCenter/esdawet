from lib import dawet, bakwan
import time

sending     = bakwan.Bakwan()
getNilai    = dawet.Dawet("2019Proyek2")
getWa       = dawet.Dawet("datamahasiswa")

#get data wa_ortu, npm, name
wanumortu   = getWa.getData("1184047", "wa_ortu", 0)
wanumpem    = getWa.getData("1184047", "wa_pembimbing", 0)
npmnum      = getWa.getData("1184047", "npm", 0)
name        = getWa.getData("1184047", "nama", 0)

if getNilai.getData("1184047", "pertemuan8", 0) == "0":
    #sending message
    sending.sendNumber(wanumortu, "Anak anda dengan npm : " + npmnum + " " + name + " *BELUM* melaksanakan bimbingan!")
    time.sleep(1)
    sending.sendNumber(wanumpem, "Anak anda dengan npm : " + npmnum + " " + name + " *BELUM* melaksanakan bimbingan!")


else:
    #sending message
    sending.sendNumber(wanumortu, "Anak anda dengan npm : " + npmnum + " " + name + " telah melaksanakan bimbingan!")
    time.sleep(1)
    sending.sendNumber(wanumpem, "Anak anda dengan npm : " + npmnum + " " + name + " telah melaksanakan bimbingan!")