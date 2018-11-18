from unittest import TestCase

import roxentools
import tempfile
import os


class TestInterfaceCall(TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.conf_empty = os.path.join(self.test_dir, "empty.conf")
        with open(self.conf_empty, 'w') as conf:
            conf.write("")
        self.conf_valid = os.path.join(self.test_dir, "valid.conf")
        with open(self.conf_valid, 'w') as conf:
            conf.write('{"username":"user","password":"pass"}')

    def test_config_nonexistant(self):
        passed = False
        try:
            s = roxentools.interface_call(conf_file='iwontexist.conf')
        except IOError:
            passed = True
        self.assertTrue(passed)

    def test_config_empty(self):
        passed = False
        try:
            s = roxentools.interface_call(conf_file=self.conf_empty)
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError was not raised")

    def test_config_invalid(self):

        try:
            s = roxentools.interface_call(conf_file=self.conf_valid)
        except:
            pass
        else:
            raise AssertionError("Shoud have failed to connect to localhost with user:pass")

