import os
from unittest import TestCase

from simba_settings.urls_update import UrlsUpdate


class TestUrlsUpdate(TestCase):
    cPath = os.getcwd()

    def setUp(self) -> None:
        self.su = UrlsUpdate()
        self.su.file_operation(os.path.join(self.cPath, "tt", "mytest", "mytest", "urls.py"))

    def test_insert_data(self):
        self.su.update_urls()

    def tearDown(self) -> None:
        del self.su
