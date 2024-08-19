"""Top-level package for unitplus."""

__author__ = """Han Zhichao"""
__email__ = 'superhin@126.com'
__version__ = '0.1.1'

import unittest

from .case import TestCase, test
from .testplan import TestPlan
from .runner import TestRunner

main = unittest.main