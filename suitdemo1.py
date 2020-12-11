import unittest
import os
# from TestCalc import TestCalcAdd
# from TestCalc import TestCalcAcc
# from TestCalc import TestCalcAbb
# from TestCalc import TestCalcAee
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
# suite.addTest(TestCalcAdd("testAdd"))
# suite.addTest(TestCalcAcc("testAcc"))
# suite.addTest(TestCalcAbb("testAbb"))
# suite.addTest(TestCalcAee("testAee"))
loader = unittest.defaultTestLoader
cases = loader.discover(os.getcwd() + "\\test", pattern="*.py")
suite.addTest(cases)
f = open("计算器测试.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "计算器的测试报告",
    description = "这是计算器加减乘除功能的测试",
    verbosity = 1
)

htmlrunner.run(suite)
