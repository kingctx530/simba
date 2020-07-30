import shutil
import time

from public_fun import PublicFun
from simba_settings.urls_update_source import UrlsUpdateSource


class UrlsUpdate(PublicFun, UrlsUpdateSource):
    def __init__(self):
        super(UrlsUpdate, self).__init__()
        UrlsUpdateSource.__init__(self)
        self.new_souce = []

    def update_urls(self):
        for i, s in enumerate(self.source):
            if 'from django.urls import path' == s.strip():
                for t in self.urls_import:
                    self.new_souce.append(t)
                self.new_souce.append("\r\n")
            elif ']' == s.strip():
                self.new_souce.append(s)
                for t in self.urls_patterns:
                    self.new_souce.append(t)
            else:
                self.new_souce.append(s)

        print("》》》 Update to urls.py 《《《")
        tmp_filename = "{}_urls.py".format(time.time())
        self.file_operation(tmp_filename, mode="w", data=self.new_souce)
        shutil.move(tmp_filename, self.last_filename)
        # for n in self.new_souce:
        #     print(n.strip())
