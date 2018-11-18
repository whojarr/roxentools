from unittest import TestCase

import roxentools


class TestServerVersion(TestCase):
    def test_is_string(self):
        s = roxentools.server_version()
        try:
            self.assertTrue(isinstance(s, basestring))
        except:
            self.assertTrue(isinstance(s, str))