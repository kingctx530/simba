import shutil
import time

from loguru import logger

from public_fun import PublicFun
from simba_settings.urls_update_source import UrlsUpdateSource


class UrlsUpdate(PublicFun, UrlsUpdateSource):
    def __init__(self):
        super(UrlsUpdate, self).__init__()
        UrlsUpdateSource.__init__(self)
        self.new_souce = []

    def update_urls(self,project_name):
        for i, s in enumerate(self.source):
            if 'from django.urls import path' == s.strip():
                for t in self.urls_import:
                    self.new_souce.append(t)
                self.new_souce.append("\r\n")
            elif ']' == s.strip():
                self.new_souce.append(s)
                for t in self.urls_patterns:
                    self.new_souce.append(t)

                self.new_souce.append("\n")  #空格

                for t in self.system_info:
                    info = None
                    if ".site_header" in t:
                        info = f'{project_name} Admin'
                    elif ".site_title" in t:
                        info = f'{project_name} Admin Dashboard'
                    elif ".index_title" in t:
                        info = f'Welcome to {project_name} Dashboard'
                    if info:
                        self.new_souce.append("{}\n".format(t.replace('<_REPLACE_DATA>',info).strip()))
                    else:
                        self.new_souce.append(t)
            else:
                self.new_souce.append(s)

        logger.info("》》》 Update to urls.py 《《《")
        tmp_filename = "{}_urls.py".format(time.time())
        self.file_operation(tmp_filename, mode="w", data=self.new_souce)
        shutil.move(tmp_filename, self.last_filename)
        # for n in self.new_souce:
        #     print(n.strip())
