#!/usr/bin/env python

"""Tests for `unitplus` package."""



from unitplus import TestCase, test


class TestDemo(TestCase):
    priority = 'p1'
    status = 'ready'
    owner = 'superhin'
    iteration = 'v0.1.0'

    @test(title='test demo a', priority='p2')
    def test_a(self):
        self.logger.info('a demo test case')

    @test(title='test ddt with data',data=['a', 'b', 'c'])
    def test_b(self, item):
        self.logger.info('item =', item)


from unitplus import TestPlan


