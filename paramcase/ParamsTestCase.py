import unittest

class ParamsTestCase(unittest.TestCase):
    parent_suite = None

    def __init__(self, name='runTest', _params=None, _parent_suite=None):
        super().__init__(methodName=name)
        self.parent_suite=_parent_suite



