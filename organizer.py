import os

Destiny = '/storage/emulated/0/Download/mídias'

error = 'não tem arquivos'
space = ' '
arquivos = 'arquivos'
sucess = 'com sucesso:3'
ZIP = 'zip'
MP4 = 'mp4'
PNG = 'png'
JPG = 'jpg'
JPEG = 'jpeg'
APK = 'apk'

if os.path.exists(Destiny):
   print(" _  __")
   print("| |/ /")
   print("| ' /  _   _  _   _")
   print("|  <  | | | || | | |")
   print("| . \ | |_| || |_| |")
   print("|_|\_\ \__, | \__,_|")
   print("        __/ |")
   print("       |___/")



else:
    os.system('mkdir mídias &&  cd mídias && mkdir imagens && mkdir vídeos && mkdir zip && mkdir apk')

list = '/storage/emulated/0/Download'

files_list = [os.path.join(list, files)

for files in os.listdir(list)
    if files.endswith(('.jpg', '.zip', '.jpeg', '.png', '.apk', '.mp4'))]

if files_list:
   os.system("mv *.png /storage/emulated/0/Download/mídias/imagens")
   print(arquivos + space + PNG + space + sucess)

else:
    print(error + space + PNG)

if files_list:
   os.system("mv *.apk /storage/emulated/0/Download/mídias/apk")
   print(arquivos + space + APK + space + sucess)

else:
    print(error + space + APK)

if files_list:
   os.system("mv *.jpg /storage/emulated/0/Download/mídias/imagens")
   print(arquivos + space + APK + space + sucess)

else:
    print(error + space + JPG)

if files_list:
   os.system("mv *.jpeg /storage/emulated/0/Download/mídias/imagens")
   print(arquivos + space + JPEG + space + sucess)

else:
    print(error + space + JPEG)

if files_list:
   os.system("mv *.mp4 /storage/emulated/0/Download/mídias/vídeos")
   print(arquivos + space + MP4 + space + sucess)

else:
    print(error + space + MP4)

if files_list:
   os.system("mv *.zip /storage/emulated/0/Download/mídias/zip")
   print(arquivos + space + MP4 + space + sucess)

else:
    print(error + space + ZIP)

