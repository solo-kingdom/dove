from unittest import TestCase

from conf.config import load


class Test(TestCase):
    def test_database(self):
        print(load())
