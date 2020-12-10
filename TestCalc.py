import unittest
from jiafa import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    [1,2,3],
    [2,3,5]
]
@ddt
class TestCalcAdd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,s,t,y):
        a = s
        b = t
        p = y
        calc = Calc()

        sum = calc.add(a,b)
        self.assertEqual(p,sum)

data2 = [
    [3,1,2],
    [3,3,0]
]
@ddt
class TestCalcAcc(unittest.TestCase):
    @data(*data2)
    @unpack
    def testAcc(self,q,w,l):
        c = q
        d = w
        o = l
        calc = Calc()

        sum = calc.acc(c,d)
        self.assertEqual(o,sum)

data3 = [
    [1,2,2],
    [2,3,6]
]
@ddt
class TestCalcAbb(unittest.TestCase):
    @data(*data3)
    @unpack
    def testAbb(self,n,k,j):
        e = n
        f = k
        m = j
        calc = Calc()

        sum = calc.abb(e,f)
        self.assertEqual(m,sum)


data4 = [
    [4,2,2],
    [6,3,2]
]
@ddt
class TestCalcAee(unittest.TestCase):
    @data(*data4)
    @unpack
    def testAee(self,z,zz,zzz):
        g = z
        h = zz
        r = zzz
        calc = Calc()

        sum = calc.aee(g,h)
        self.assertEqual(r,sum)
