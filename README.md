# unitplus
Enhancement for unittest


![Languate - Python](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - License](https://img.shields.io/pypi/l/unitplus)
![PyPI](https://img.shields.io/pypi/v/unitplus)
![PyPI - Downloads](https://img.shields.io/pypi/dm/unitplus)


## Install
```shell
pip install unitplus
```

## Simple Use

### Register and Login
```python
from python_yapi import YApi
yapi = YApi(base_url='http://localhost:3000')

username, email, password = 'Kevin', 'kevin@126.com', 'abc123'

yapi.register(username, email, password)  # return a dict
yapi.login( email, password) # return a dict
```


### Simple Use
#### Write TestCase
```python
from unitplus import TestCase, test


class TestDemo(TestCase):
    priority = 'p1'
    status = 'ready'
    owner = 'superhin'
    iteration = 'v0.1.0'
    tags = ['demo']

    @test(title='test demo a', priority='p2')
    def test_a(self):
        self.logger.info('a demo test case')

    @test(title='test ddt with data',data=['a', 'b', 'c'])
    def test_b(self, item):
        self.logger.info('item =', item)
```

### Use TesPlan  to run tests
```python
from unitplus import TestPlan


class TestPlanDemo(TestPlan):
    # test names for suite
    tests = [
        'cases.testdemo',
    ]

    # filter tests by attributes
    filter = {
        'priorities': ['p0', 'p1'],
        'status': ['ready'],
        'tags': ['demo'],  # include tags
        'exclude_tags': ['post'],
        'exclude_names': [
            'cases.test_case3.TestA.test_get03',
            'cases.test_case4.TestA.test_get02',
        ]

    }


if __name__ == '__main__':
    # run suite , supporting multiple threads
    TestPlanDemo().run(verbosity=3)
```
