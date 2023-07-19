import logging
import unittest
from functools import wraps

try:
    from loguru import logger
except ImportError:
    logger = logging.getLogger(__name__)

DATA_ATTR = 'data'


def setattr_if_not_none(func, name, value):
    if value is not None:
        setattr(func, name, value)


def copy_attr_if_not_none(method, obj):
    for key, value in method.__dict__.items():
        if not key.startswith('__') and value is not None:
            setattr(obj, key, value)


def make_test(method, index, value: list):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        return method(self, *value)

    wrapper.__doc__ = f'{method.__doc__}_{index}_{value}' if method.__doc__ else None
    wrapper.__name__ = f'{method.__name__}_{index}_{value}'

    delattr(wrapper, DATA_ATTR)
    return wrapper


class TestCaseType(type):
    def __new__(cls, name, bases, attrs):
        klass = super().__new__(cls, name, bases, attrs)
        for name, method in attrs.items():
            if hasattr(method, DATA_ATTR):
                for index, value in enumerate(getattr(method, DATA_ATTR)):
                    new_method = make_test(method, index, value)
                    setattr(klass, new_method.__name__, new_method)
                delattr(klass, name)
        return klass


def test(title=None, priority=None, status=None, tags=None, owner=None, iteration=None, data=None, **kwargs):
    def decorator(method):
        kwargs.update(
            {'__doc__': title,
             'priority': priority,
             'status': status,
             'tags': tags,
             'owner': owner,
             'iteration': iteration,
             DATA_ATTR: data
             })

        for key, value in kwargs.items():
            setattr_if_not_none(method, key, value)
        return method

    return decorator


class TestCase(unittest.TestCase, metaclass=TestCaseType):
    priority = None
    status = None
    tags = None
    owner = None
    iteration = None

    logger = logger

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        copy_attr_if_not_none(getattr(self, methodName), self)
