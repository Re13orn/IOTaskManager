class ThreadManager:
    def __init__(self):
        self.threads = {}

    def start_thread(self, name, task_class, interval=1):
        if name in self.threads and self.threads[name].is_alive():
            print(f"Thread {name} is already running.")
            return

        print(f"Starting thread {name}...")
        thread = task_class(name, interval)
        self.threads[name] = thread
        thread.start()

    def stop_thread(self, name):
        if name in self.threads and self.threads[name].is_alive():
            print(f"Stopping thread {name}...")
            self.threads[name].stop()
            self.threads[name].join()
            del self.threads[name]
            print(f"Thread {name} stopped.")
        else:
            print(f"Thread {name} is not running.")

    def stop_all_threads(self):
        for name, thread in self.threads.items():
            if thread.is_alive():
                print(f"Stopping thread {name}...")
                thread.stop()
                thread.join()
                print(f"Thread {name} stopped.")
        self.threads.clear()

    def list_running_threads(self):
        return [name for name, thread in self.threads.items() if thread.is_alive()]