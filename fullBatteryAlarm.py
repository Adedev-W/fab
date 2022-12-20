import json
import os
import time
from time import sleep
def battery():
        batterystatus = os.popen("termux-battery-status", "r", 1)
        resultBattery= batterystatus.read()
        resultLdec = resultBattery
        Rdecode = resultLdec.replace("\n","")
        Rjson = json.loads(Rdecode)
        Ra = Rjson["health"]
        Rb = Rjson["percentage"]
        Rc = Rjson["plugged"]
        Rd = Rjson["status"]
        Re = Rjson["temperature"]
        banner = f"""
        \nBerdasarkan data, baterai anda dalam kondisi {Ra},
        dengan persentase sebesar {Rb}, serta keadaan {Rc}, status {Rd}, dan temperatur suhu {Re}
        """
        RbInt = int(Rb)
        return RbInt, Rd
banner = """                                                           
         
        --Tool for full battery alarm--
        -- By AdeSaputra     --
        -------------------------------

Note :  Made using python and
        assisted by Termux-API.

 = Options =
  Set Alarm - Masukkan waktu (milidetik)
  Preview Alarm - Lewati jika ingin pratinjau alarm

"""
print(banner)
waktu = int(input("Masukkan delay (milidetik): ") or "1")
while True:
        sleep(waktu)
        Rbi, Rj = battery()
        Rbit = int(Rbi)
        if Rbi == '85':
                batterystatus = os.popen("termux-media-player play anotherlove.mp3", "r", 1)
                time.sleep(195)
        elif Rbit > 85 and Rbit < 100:
                batterystatus = os.popen("termux-media-player play anotherlove.mp3", "r", 1)
                time.sleep(195)
        elif Rbit < 20 and Rj == "DISCHARGING":
                batterystatus = os.popen("termux-media-player play anotherlove.mp3", "r", 1)
                time.sleep(195)
        else:
                print("Maaf baterai masih dibawah 85%, silahkan isi daya untuk mengaktifkan fitur")
