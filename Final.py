# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys


class downloader(object):

    def __init__(self):
        print('Please input chapters website')
        self.target = input()
        print('Please input chapters website and delete any after last "/"')
        self.server = input()
        self.names = []
        self.urls = []
        self.nums = 0


    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = "gb18030"
        html = req.text
        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all('table',bgcolor="#d4d0c8")
        a_bf = BeautifulSoup(str(div[0]), "html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a[:])
        for each in a[:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))


    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = "gb18030"
        html = req.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('td', width="820",align="left",bgcolor="#FFFFFF")
        texts = texts[0].text.replace('\xa0'*5,'\r\n\n')
        return texts


    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='gb18030') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('Start downloading：' + '\r')
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'Book.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("Processing:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('Finished')