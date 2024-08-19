# unitplus

![Languate - Python](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - License](https://img.shields.io/pypi/l/unitplus)
![PyPI](https://img.shields.io/pypi/v/unitplus)
![PyPI - Downloads](https://img.shields.io/pypi/dm/unitplus)

Enhancement for unittest by adding status, priority, tags, owner properties for testcases and filters.


## Install
```shell
pip install unitplus
```

### Simple Use
#### Write TestCase
```python
import unitplus


class TestDemo(unitplus.TestCase):
    priority = 'p1'
    status = 'ready'
    owner = 'superhin'
    iteration = 'v0.1.0'
    tags = ['demo']

    @unitplus.test(title='test demo a', priority='p2')
    def test_a(self):
        self.logger.info('a demo test case')

    @unitplus.test(title='test ddt with data',data=['a', 'b', 'c'])
    def test_b(self, item):
        self.logger.info('item =', item)

if __name__ == '__main__':
    unitplus.main()
```

### Use TesPlan  to run tests
```python
import unitplus


class TestPlanDemo(unitplus.TestPlan):
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
