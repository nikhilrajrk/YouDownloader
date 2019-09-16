import tkinter as tk
import requests
from bs4 import BeautifulSoup

app = tk.Tk()
app.geometry("400x200")
#This Function Used to Display GUI Frame
def main():
    global e1
    #Just Display YouTube Downloader
    l1 = tk.Label(app, text='YouTube Downloader', font=("Helvetica", 16))
    l1.pack()
    #Just Display Enter Url:
    l2 = tk.Label(app, text='Enter URL : ', font=("Helvetica", 10))
    l2.pack()
    #Entry Box
    e1 = tk.Entry(app, bd=3)
    e1.pack()
    #Display Click Button
    b1 = tk.Button(app, text='Click', cursor='hand2', command=Downloader)
    b1.pack()

#This Function Used to Download the Youtube Videos
def Downloader():
    youtube_link = e1.get().replace(':', '%3A').replace('/', '%2F').replace('?', '%3F').replace('=', '%3D')
    bit_url = 'https://bitdownloader.com/download?video='+youtube_link

    r = requests.get(bit_url).content
    soup = BeautifulSoup(r, 'lxml')

    video_name = soup.find('span', {"class":"title"}).text + '.mp4'
    download_link = soup.find('a', {'download':video_name}).get('href')
    r = requests.get(download_link).content
    name = video_name.replace('|', '')

    file = open(name, 'wb')
    file.write(r)
    print('Downloaded..')

main()
app.mainloop()
