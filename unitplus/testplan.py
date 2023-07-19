import unittest

from .filter import Filter
from .runner import TestRunner


class TestPlan:
    tests = []
    filter: dict = None

    def __init__(self):
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames(self.tests)
        filter = Filter(suite, **self.filter)

        self.suite = filter.result

    def run(self, verbosity=1, threads=None):
        # runner = unittest.TextTestRunner(verbosity=verbosity)
        runner = TestRunner(verbosity=verbosity)
        runner.run(self.suite, threads=threads)


