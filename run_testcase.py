#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'Snow Zhang'

import unittest
import os
import time
from HTMLTestRunner_PY3 import HTMLTestRunner

# test_dir = './'
test_dir = r'F:\study\Pycharm\mty_auto\test_case'
discvoer = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
# discvoer = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
test_report_path = os.path.abspath('.')+'\\test_report'
now = time.strftime("%Y-%m-%d_%H_%M_%S")

if __name__ == '__main__':
    # 输出结果到HTML
    filename = test_report_path + "\\" + now + '_result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title="运营控制台测试报告", description="自动用例执行情况")
        runner.run(discvoer)
