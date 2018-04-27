import unittest

class ParamsTestSuite(unittest.TestSuite):
    params = {}
    
    def __init__(self, tests=(),  _params=None):
        super().__init__(self)
        self.suite_params=_params

    def addTest(self, test):
        super(ParamsTestSuite, self).addTest(test)
        if hasattr(test,'parent_suite'):
            test.parent_suite = self