import threading
import time
import requests
import re
import urllib3


# 禁用不必要的警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ReqTest(threading.Thread):
    def __init__(self, name, interval=1):
        super().__init__()
        self.name = name
        self.interval = interval
        self._stop_event = threading.Event()
        self.daemon = True

    def run(self):
        while not self._stop_event.is_set():
            print(f"{self.name} is performing new task...")
            url = "https://www.baidu.com"
            
            try:
                req = requests.get(url=url, verify=False)
                req.encoding = "utf-8"
                print(req.status_code)
                match = "<title>(.*?)</title>"
                title = re.findall(match, req.text)
                print(title)
            except Exception as e:
                print(e)
            time.sleep(self.interval)


    def stop(self):
        self._stop_event.set()