from lib import dawet, bakwan, mietektek
import time

#make object from import class
meet        = mietektek.Mietektek()
sending     = bakwan.Bakwan()
getNilai    = dawet.Dawet("2019Proyek2")
getWa       = dawet.Dawet("datamahasiswa")

#get data wa_ortu, npm, name, meet
wanumortu   = getWa.getData("1184047", "wa_ortu", 0)
wanumpem    = getWa.getData("1184047", "wa_pembimbing", 0)
npmnum      = getWa.getData("1184047", "npm", 0)
name        = getWa.getData("1184047", "nama", 0)

#set data for running
meet_for_guidance = "pertemuan1"
guidance_meet = meet.Bimbingan(meet_for_guidance)
getValue    = getNilai.getData("1184047", meet_for_guidance, 0)

if getValue == "0":
    #sending message
    sending.sendNumber(wanumortu, "Anak anda dengan npm : " + npmnum + " " + name + " *BELUM* melaksanakan bimbingan! pada " + "*" + guidance_meet + "*")
    time.sleep(1)
    sending.sendNumber(wanumpem, "Anak bimbingan anda dengan npm : " + npmnum + " " + name + " *BELUM* melaksanakan bimbingan! pada " + "*" + guidance_meet + "*")

else:
    #sending message
    sending.sendNumber(wanumortu, "Anak anda dengan npm : " + npmnum + " " + name + " telah melaksanakan bimbingan! pada " + "*" + guidance_meet + "*")
    time.sleep(1)
    sending.sendNumber(wanumpem, "Anak bimbingan anda dengan npm : " + npmnum + " " + name + " telah melaksanakan bimbingan! pada " + "*" + guidance_meet + "*")