import os
import subprocess
import sys
from argparse import ArgumentParser
from subprocess import PIPE

from loguru import logger

from simba_settings.asgi_update import AsgiUpdate
from simba_settings.routing_update import RoutingUpdate
from simba_settings.settings_update import SettingsUpdate
from simba_settings.urls_update import UrlsUpdate


class Simba:
    def __init__(self):
        self.django_cmd = 'django-admin'
        self.parser = ArgumentParser()

    def new_project(self, *args):
        current_path = os.getcwd()
        project_name = getattr(*args, "name")
        assert project_name, "NOT GET PROJECT... (-n `project name`)"
        project_path = getattr(*args, "path")
        project_channels = getattr(*args, "channels")
        if project_path is None:
            project_path = "."
        else:
            if not os.path.exists(project_path):
                os.makedirs(project_path, exist_ok=True)
            os.chdir(project_path)
        self.new_pt = '{} startproject {}'.format(self.django_cmd, project_name)

        pn = subprocess.Popen(self.new_pt,
                              shell=True,
                              stdout=PIPE,
                              stderr=PIPE,
                              stdin=PIPE)
        while True:
            line = pn.stdout.readline()
            err_line = pn.stderr.readline()
            if err_line:
                logger.info(f"NEW PROJECT ERR >>> {err_line.decode()}")
                break
            if not line:
                break

        assert os.path.exists(project_name), "CREATE PROJECT ERR!...."
        os.chdir(current_path)
        self.ul = UrlsUpdate()
        file_path = os.path.join(project_path, project_name, project_name, "urls.py")
        self.ul.file_operation(file_path)
        self.ul.update_urls(project_name)

        self.su = SettingsUpdate()
        file_path = os.path.join(project_path, project_name, project_name, "settings.py")
        self.su.file_operation(file_path)
        self.su.update_settings(channels=project_channels)
        self.su.auto_building_folder()
        self.su.copy_app()

        self.rt = RoutingUpdate()
        file_path = os.path.join(project_path, project_name, project_name, "routing.py")
        self.rt.update_routing(file_path)

        self.asgi = AsgiUpdate()
        file_path = os.path.join(project_path, project_name, project_name, "asgi.py")
        self.asgi.update_asgi(file_path,project_name)




parser = ArgumentParser(description="Calamus & Glider's Django auto generate tool")
parser.add_argument("newproject", nargs=1, help="create Django project's base structure")
parser.add_argument("-n", "--name", help="Django project name", dest="name", default="default")
parser.add_argument("-p", "--path", help="Django project path", dest="path", required=False)
parser.add_argument("-c", "--channels", help="Add channels settings", action='store_true', dest="channels",
                    required=False)

parser.add_argument("--delproject", nargs=2, help="delete Django project's base structure")

args = parser.parse_args()
cgd = Simba()

if args.newproject:
    if args.channels is None:
        logger.info("《《《 Generate Basic Django Project 「{}」》》》".format(args.name))
    else:
        logger.info("《《《 Generate Channels Django Project 「{}」》》》".format(args.name))
    cgd.new_project(args)

if args.delproject:
    logger.info(f"delproject positional arg:{args.delproject}")
