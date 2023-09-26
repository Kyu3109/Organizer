import os

# Verifica se tem a pasta.
Destiny = '/storage/emulated/0/Download/mídias'

# Variavel para caso não houver nenhum arquivo para mover.
nada = "Nᴀ̃ᴏ ᴛᴇᴍ ɴᴇɴʜᴜᴍ ᴀʀǫᴜɪᴠᴏ ᴘᴀʀᴀ ᴍᴏᴠᴇʀ :3"

if os.path.exists(Destiny):
   print(" _  __")
   print("| |/ /")
   print("| ' /  _   _  _   _")
   print("|  <  | | | || | | |")
   print("| . \ | |_| || |_| |")
   print("|_|\_\ \__, | \__,_|")
   print("        __/ |")
   print("       |___/")


# Cria pastas caso não houver pastas criadas
else:
    os.system('mkdir mídias &&  cd mídias && mkdir imagens && mkdir vídeos && mkdir zip && mkdir apk')
    print("as pastas foram criadas com sucessi")

print("-"*30)

# Pasta principal.
list = '/storage/emulated/0/Download'

# Guarda os arquivos.
files_list = [os.path.join(list, files)

# Lista os arquivos.
for files in os.listdir(list)
    if files.endswith(('.jpg', '.zip', '.jpeg', '.png', '.apk', '.mp4'))]

# Move arquivos de imagens png/jpg/jpeg.
for files in files_list:
    if files.endswith('.png'):
       print("𝐌𝐨𝐯𝐞𝐧𝐝𝐨 𝐚𝐫𝐪𝐮𝐢𝐯𝐨𝐬 𝐩𝐧𝐠")
       os.system("mv *.png /storage/emulated/0/Download/mídias/imagens")
       break

else:
    print("𝐍𝐚𝐨 𝐭𝐞𝐦 𝐧𝐞𝐧𝐡𝐮𝐦 𝐚𝐫𝐪𝐮𝐢𝐯𝐨 .𝐩𝐧𝐠 𝐩𝐚𝐫𝐚 𝐦𝐨𝐯𝐞𝐫")

for files in files_list:
    if files.endswith('.jpg'):
       print("𝐌𝐨𝐯𝐞𝐧𝐝𝐨 𝐚𝐫𝐪𝐮𝐢𝐯𝐨𝐬 𝐣𝐩𝐠")
       os.system("mv *.jpg /storage/emulated/0/Download/mídias/imagens")
       break
else:
    print("𝐍𝐚𝐨 𝐭𝐞𝐦 𝐧𝐞𝐧𝐡𝐮𝐦 𝐚𝐫𝐪𝐮𝐢𝐯𝐨 .𝐣𝐩𝐠 𝐩𝐚𝐫𝐚 𝐦𝐨𝐯𝐞𝐫")

for files in files_list:
    if files.endswith('.jpeg'):
       print("𝐌𝐨𝐯𝐞𝐧𝐝𝐨 𝐚𝐫𝐪𝐮𝐢𝐯𝐨𝐬 𝐣𝐩𝐞𝐠")
       os.system("mv *.jpeg /storage/emulated/0/Download/mídias/imagens")
       break
else:
    print("𝐍𝐚𝐨 𝐭𝐞𝐦 𝐧𝐞𝐧𝐡𝐮𝐦 𝐚𝐫𝐪𝐮𝐢𝐯𝐨 .𝐣𝐩𝐞𝐠 𝐩𝐚𝐫𝐚 𝐦𝐨𝐯𝐞𝐫")

# Move arquivos zip.
for files in files_list:
    if files.endswith('.zip'):
       print("𝐌𝐨𝐯𝐞𝐧𝐝𝐨 𝐚𝐫𝐪𝐮𝐢𝐯𝐨𝐬 𝐳𝐢𝐩")
       os.system("mv *.zip /storage/emulated/0/Download/mídias/zip")
       break
else:
    print("𝐍𝐚𝐨 𝐭𝐞𝐦 𝐧𝐞𝐧𝐡𝐮𝐦 𝐚𝐫𝐪𝐮𝐢𝐯𝐨 .𝐳𝐢𝐩 𝐩𝐚𝐫𝐚 𝐦𝐨𝐯𝐞𝐫")

# Move arquivos de vídeos mp4.
for files in files_list:
    if files.endswith('.mp4'):
       print("𝐌𝐨𝐯𝐞𝐧𝐝𝐨 𝐚𝐫𝐪𝐮𝐢𝐯𝐨𝐬 𝐦𝐩4")
       os.system("mv *.mp4 /storage/emulated/0/Download/mídias/vídeos")
       break
else:
    print("𝐍𝐚𝐨 𝐭𝐞𝐦 𝐧𝐞𝐧𝐡𝐮𝐦 𝐚𝐫𝐪𝐮𝐢𝐯𝐨 .𝐦𝐩4 𝐩𝐚𝐫𝐚 𝐦𝐨𝐯𝐞𝐫")

# Move arquivos de aplicações apk.
for files in files_list:
    if files.endswith('.apk'):
       print("𝐌𝐨𝐯𝐞𝐧𝐝𝐨 𝐚𝐫𝐪𝐮𝐢𝐯𝐨𝐬 𝐚𝐩𝐤")
       os.system("mv *.apk /storage/emulated/0/Download/mídias/apk")
       break

else:
    print("𝐍𝐚𝐨 𝐭𝐞𝐦 𝐧𝐞𝐧𝐡𝐮𝐦 𝐚𝐫𝐪𝐮𝐢𝐯𝐨 .𝐚𝐩𝐤 𝐩𝐚𝐫𝐚 𝐦𝐨𝐯𝐞𝐫")

# Caso a tarefa seja concluída ou não tenha nenhum arquivo para mover.
if files_list:
   print("tarefa concluída")

else:
    print(nada)
