import threading
import time

class IOTask(threading.Thread):
    def __init__(self, name, interval=1):
        super().__init__()
        self.name = name
        self.interval = interval
        self._stop_event = threading.Event()
        self.daemon = True

    def run(self):
        while not self._stop_event.is_set():
            print(f"{self.name} is performing I/O task...")
            time.sleep(self.interval)

    def stop(self):
        self._stop_event.set()

