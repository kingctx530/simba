import os
import shutil
import time

from loguru import logger

from simba_settings.asgi_update_source import AsgiUpdateSource
from public_fun import PublicFun

class AsgiUpdate(PublicFun, AsgiUpdateSource):
    def __init__(self):
        super(AsgiUpdate, self).__init__()
        AsgiUpdateSource.__init__(self)
        self.new_souce = []

    def update_asgi(self,file_path,project_name):
        self.new_souce.append(self.example_data.replace("<_REPLACE_DATA>",project_name))
        logger.info("》》》 Update to asgi.py 《《《")
        self.file_operation(file_path, mode="w", data=self.new_souce)

