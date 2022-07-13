from gtts import gTTS
import os

mp3_path = str(os.path.abspath(os.getcwd())) + os.sep + 'mp3' + os.sep

if not os.path.isdir(mp3_path):
    os.mkdir(mp3_path)

i = 0
merge_file = list()
# 一行一行地讀取Txt.txt，轉成 001.mp3 002.mp3 003.mp3 ...
TxtFileName = 'Txt.txt'
with open(TxtFileName) as f:
    for line in f.readlines():
        i = i+1
        myobj = gTTS(text=line, lang='zh', slow=False)
        myobj.save('{0}/{1}.mp3'.format(mp3_path, str(i).zfill(3)))
        merge_file.append(mp3_path + str(i).zfill(3) + '.mp3')

merge_file_mp3 = list()
# mp3資料夾內mp3 合併成 merge.mp3
for j in merge_file:
    with open(j, 'rb') as f:
        merge_file_mp3.append(f.read())

with open('merge.mp3', 'wb') as f:
    for j in merge_file_mp3:
        f.write(j)
