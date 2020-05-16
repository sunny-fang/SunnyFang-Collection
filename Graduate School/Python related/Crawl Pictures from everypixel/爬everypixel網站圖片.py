#%%
# 爬蟲網址 : https://www.everypixel.com/search?q=+Wood+grain&stocks_type=free
# 爬第一頁
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
os.getcwd()
os.chdir('C:\\Users\\方永騰\\Desktop\\翔\\DIGI\\專案\\Everypixel\\wood_grain\\page1')

url = 'https://www.everypixel.com/search?q=+Wood+grain&stocks_type=free'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
select = soup.select('img.thumb__img')
a = len(select)
for i in range(a):
    picurl = select[i]['src']
    pic = requests.get(picurl)
    pic2 = pic.content
    pic_out = open('pic'+str(i)+'.jpg','wb')    # img1.png為預存檔的圖片名稱
    pic_out.write(pic2)                # 將get圖片存入img1.png
    pic_out.close()

a = len(select)

#%%
# 爬2-8頁
import requests
from bs4 import BeautifulSoup
import os
os.getcwd()
os.chdir('C:\\Users\\方永騰\\Desktop\\翔\\DIGI\\專案\\Everypixel\\wood_grain\\page2-8')

x = 2
while x <= 8:
    url = 'https://www.everypixel.com/search?q=%2BWood%2Bgrain&stocks_type=free&page=' + str(x)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    select = soup.select('img.thumb__img')
    a = len(select)
    for i in range(a):
        picurl = select[i]['src']
        pic = requests.get(picurl)
        pic2 = pic.content
        pic_out = open('pic'+str(x)+'-'+str(i)+'.jpg','wb')    # img1.png為預存檔的圖片名稱
        pic_out.write(pic2)                # 將get圖片存入img1.png
        pic_out.close()
    x = x+1


#%%
# 爬stone texture page1-20
import requests
from bs4 import BeautifulSoup
import os

os.getcwd()
os.chdir('C:\\Users\\方永騰\\Desktop\\翔\\DIGI\\專案\\Everypixel\\stone texture\\page1-20')

x = 1
while x <= 20:
    url = 'https://www.everypixel.com/search?q=stone%2Btexture&stocks_type=free&page=' + str(x)
    r = requests.get(url, verify = False)        # 加上verify = False，代表request忽略對SSL的驗證
    soup = BeautifulSoup(r.text, 'html.parser')
    select = soup.select('img.thumb__img')
    a = len(select)
    for i in range(a):
        picurl = select[i]['src']
        try : 
            pic = requests.get(picurl)
        except Exception : 
            pass            
        pic2 = pic.content
        pic_out = open('pic'+str(x)+'-'+str(i)+'.jpg','wb')    # img1.png為預存檔的圖片名稱
        pic_out.write(pic2)                # 將get圖片存入img1.png
        pic_out.close()
    x = x+1

