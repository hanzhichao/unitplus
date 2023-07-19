import unittest


def is_testsuite(test):
    return isinstance(test, unittest.TestSuite)


class Filter:
    def __init__(self, suite, priorities=None, iterations=None, owners=None, status=None, tags=None,
                 exclude_tags=None, exclude_names=None):
        self._tests = self.get_tests(suite)

        if isinstance(priorities, list):
            self.filter_by_priorities(priorities)

        if isinstance(iterations, list):
            self.filter_by_iterations(iterations)

        if isinstance(owners, list):
            self.filter_by_owners(owners)

        if isinstance(status, list):
            self.filter_by_status(status)

        if isinstance(tags, list):
            self.filter_by_status(tags)

        if isinstance(exclude_tags, list):
            self.filter_by_exclude_tags(exclude_tags)

        if isinstance(exclude_names, list):
            self.filter_by_exclude_names(exclude_names)

    @property
    def result(self):
        return unittest.TestSuite(self._tests)

    def get_tests(self, test) -> list:
        if not is_testsuite(test):
            return [test]

        tests = []
        for item in test:
            tests.extend(self.get_tests(item))
        return tests

    def filter_by_priorities(self, priorities):
        tests = []
        for test in self._tests:
            if hasattr(test, 'priority') and test.priority in priorities:
                tests.append(test)
        self._tests = tests

    def filter_by_iterations(self, iterations):
        tests = []
        for test in self._tests:
            if hasattr(test, 'iteration') and test.iteration in iterations:
                tests.append(test)
        self._tests = tests

    def filter_by_owners(self, owners):
        self._tests = list(filter(lambda test: test.owner in owners, self._tests))

    def filter_by_status(self, status):
        self._tests = list(filter(lambda test: test.status in status, self._tests))

    def filter_by_tags(self, tags):

        tests = []
        for test in self._tests:
            for tag in tags:
                if tag not in test.tags:
                    break
            else:
                tests.append(test)

        self._tests = tests

    def filter_by_exclude_tags(self, exclude_tags):
        tests = []
        for test in self._tests:
            for tag in exclude_tags:
                if tag in test.tags:
                    break
            else:
                tests.append(test)
        self._tests = tests

    def filter_by_exclude_names(self, exclude_names):
        exclude_tests = unittest.TestLoader().loadTestsFromNames(exclude_names)
        tests = []
        for test in self._tests:
            if test not in exclude_tests:
                tests.append(test)
        self._tests = tests
