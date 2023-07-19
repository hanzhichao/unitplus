=====
Usage
=====

To use unitplus in a project::

    import unitplus

To use testplan in a project::

    from testbase.testplan import TestPlan


    class MyTestPlan(TestPlan):
        tests = [
            'cases',
        ]
        filter = {
            'priorities': ['p0', 'p1'],
            'status': ['ready'],
            'tags': ['demo'],
            'exclude_tags': ['post'],
            'exclude_names': [
                'cases.test_case3.TestA.test_get03',
                'cases.test_case4.TestA.test_get02',
            ]

        }


    if __name__ == '__main__':
        MyTestPlan().run(verbosity=3, threads=2)


