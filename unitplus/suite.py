import unittest
from concurrent.futures import ThreadPoolExecutor, as_completed


def is_testsuite(test):
    return isinstance(test, unittest.TestSuite)
def run(self, result, debug=False):
    topLevel = False
    if getattr(result, '_testRunEntered', False) is False:
        result._testRunEntered = topLevel = True

    # 如果结果中result有threads, 创建一个线程池 --------------------------
    if hasattr(result, 'threads') and result.threads is not None:
        pool = ThreadPoolExecutor()
    else:
        pool = None

    # ----------------------------------------------------------------

    for index, test in enumerate(self):
        if result.shouldStop:
            break

        if not is_testsuite(test):
            self._tearDownPreviousClass(test, result)
            self._handleModuleFixture(test, result)
            self._handleClassSetUp(test, result)
            result._previousTestClass = test.__class__

            if (getattr(test.__class__, '_classSetupFailed', False) or
                    getattr(result, '_moduleSetUpFailed', False)):
                continue

        if not debug:
            # 如果设置了线程池, 在线程池中运行，并把异步任务放到result对象的tasks列表中
            if pool is not None:
                result.tasks.append(pool.submit(test, result))
            else:
                test(result)
        else:
            # 如果设置了线程池, 在线程池中运行，并把异步任务放到result对象的tasks列表中
            if pool is not None:
                result.tasks.append(pool.submit(test.debug))
            else:
                test.debug()

        if self._cleanup:
            self._removeTestAtIndex(index)

    if topLevel:
        self._tearDownPreviousClass(None, result)
        self._handleModuleTearDown(result)
        result._testRunEntered = False
    return result
