import os
import threading
import time
import sys


class Watchcat(object):

    def __init__(self, verbose=False, *files):
        self.files = []
        self.mod_times = {}
        self._watching_thread = None
        self._watching_work = False
        self.verbose = verbose

        if files:
            self.add_files(*files)

    def run_watching(self):
        self._watching_work = True
        self._watching_thread = threading.Thread(target=self._watch_till_stop)
        self._watching_thread.start()

        try:
            while self._watching_work:
                time.sleep(.1)
        except KeyboardInterrupt:
            self.stop_watching()

    def _watch_till_stop(self):
        while self._watching_work:
            self.watch_changes()
            time.sleep(1)

    def stop_watching(self):
        if self._watching_thread and self._watching_thread.isAlive():
            self._watching_work = False
            self._watching_thread.join()

    def watch_changes(self):
        for file in self.files:
            try:
                last_mod_time = os.stat(file).st_mtime
            except OSError:
                time.sleep(1)
                last_mod_time = os.stat(file).st_mtime

            if file not in self.mod_times.keys():
                self.mod_times[file] = last_mod_time
                continue

            if last_mod_time > self.mod_times[file]:
                if self.verbose:
                    print("File changed: {}".format(os.path.realpath(file)))
                self.mod_times[file] = last_mod_time

    def add_files(self, *files):
        dirs = [os.path.realpath(x) for x in files if os.path.isdir(x)]
        files = [os.path.realpath(x) for x in files if os.path.isfile(x)]
        for i in dirs:
            files += self.get_files_in_dir(i)
        self.files = files
        self.watch_changes()

    def get_files_in_dir(self, dirname):
        z = os.listdir(dirname)
        files = [dirname + '/' + x for x in z if os.path.isfile(dirname + '/' + x)]
        dirs = [dirname + '/' + x for x in z if os.path.isdir(dirname + '/' + x)]
        for i in dirs:
            files += self.get_files_in_dir(i)
        return files
