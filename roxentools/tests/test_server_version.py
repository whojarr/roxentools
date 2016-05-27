from unittest import TestCase

import roxentools


class TestServerVersion(TestCase):
    def test_is_string(self):
        s = roxentools.server_version()
        self.assertTrue(isinstance(s, basestring))
