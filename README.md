# (project1) Txt to mp3

* 專案參考來源: [link](https://skjhcreator.blogspot.com/2022/07/python-txtmp3.html?fbclid=IwAR1fgBKyxDHYiJ47ZmKoOWxB15-tApJkwPF1qas-dB76n3IyQ5uZ4_SungU)
  * 參考來源程是在不同作業系統會有問題，已經修改成可以符合不同作業系統。

* gTTS install : [link](https://pypi.org/project/gTTS/)

~~~bash
$ pip install gTTS
~~~

* 把中文字放在 Txt.txt 執行後生成一個 mp3 file, 內容為念出整篇文字音檔。
  * Txt.txt 內容可任意修改。


## 學習重點

* 使用 github 下載專案
  * .gitignore <--- 檔案內容用法
    * [參考資料](https://gitbook.tw/chapters/using-git/ignore) 

* 安裝套件
  * 建議使用虛擬環境 [參考資料]( https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env)
    * 打包程執行檔時檔案較小。
    * 安裝個模組不會互相干擾。 
* requirements.txt 
  * 可以知道此專案的安裝模組與版本。
  * [參考資料](https://blog.longwin.com.tw/2019/03/python-pip-requirements-txt-management-package-2019/)


~~~bash
# 導出（生成）
$ pip freeze > requirements.txt

# 導入（安裝）
$ pip3 install -r requirements.txt 
~~~





# (project2) read uart port 

* 讀取資料結構須為 '*' 開頭，'!' 結尾。

* pyserial install: [link](https://pypi.org/project/pyserial/)

~~~bash
# pip install pyserial
~~~

* 關鍵字：分析字串切入點。
  * 可由此處開始解析字串

## 學習重點

* 讀取 uart port 基本寫法。
* 任何資料結構皆可。





# (project3) read uart port  (readline)

* 讀取資料結構須為 '*' 開頭，'!' 結尾。

* 用於當資料結尾有 '\n' 時。

## 學習重點

* 同上，若是傳送訊息為結尾有'\n' 時，可簡化程式。

