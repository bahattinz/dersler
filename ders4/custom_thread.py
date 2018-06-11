import threading
import time
import datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os

class CustomThread(threading.Thread):
    def __init__(self, title, time):
        super(CustomThread,self).__init__()
        self.title=title
        self.time=time

    def run(self):
        for i in range(5):
            time.sleep(self.time)
            print("{} {} {}".format(self.title,i+1,datetime.datetime.now()))

class CustomThread2(threading.Thread):
    def __init__(self, link):
        super(CustomThread2,self).__init__()
        self.link = link
    def run(self):
            for i in range(5):
                url=urlopen(Request(url=self.link,headers={"User-Agent": "Mozilla"}))
                html_content = url.read()
                parsed_data = BeautifulSoup(html_content,"html.parser")
                value = parsed_data.find("span",id="last_last").get_text()
                value = float(value.replace(",","."))
                read_time = datetime.datetime.now().time().strftime("%H:%M:%S")
                self.create_csv(value=value, read_time=read_time)
                time.sleep(3)

    def create_csv(self, value, read_time):
        import csv
        data = {"value":value,"time":read_time}
        file_name = "dolar.csv"
        file_exists = os.path.isfile(file_name)
        with open(file_name,"a") as f:
            fieldnames = list(data.keys())
            wr = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                wr.writeheader()

            wr.writerow(data)
            f.close()
