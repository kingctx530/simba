import os
import shutil
import time

from simba_settings.routing_update_source import RoutingUpdateSource
from public_fun import PublicFun
class RoutingUpdate(PublicFun, RoutingUpdateSource):
    def __init__(self):
        super(RoutingUpdate, self).__init__()
        RoutingUpdateSource.__init__(self)
        self.new_souce = []

    def update_routing(self,file_path):
        self.new_souce.append(self.example_data)
        self.file_operation(file_path,mode="w",data=self.new_souce)