import numpy as np
from ..compiler import compile
from ..types import (arraytype, float32)

from .support import testcase, main, assertTrue

def array_sum_1(ary):
    return ary.sum()

def array_sum_2(ary):
    return np.sum(ary)

def array_prod_1(ary):
    return ary.prod()

def array_prod_2(ary):
    return np.prod(ary)

@testcase
def test_array_sum_1():
    cfunc = compile(array_sum_1, float32, [arraytype(float32, 1, 'C')])
    a = np.arange(10, dtype=np.float32)
    assertTrue(np.allclose(cfunc(a), a.sum()))

@testcase
def test_array_sum_2():
    cfunc = compile(array_sum_2, float32, [arraytype(float32, 1, 'C')])
    a = np.arange(10, dtype=np.float32)
    assertTrue(np.allclose(cfunc(a), np.sum(a)))

@testcase
def test_array_sum_3():
    cfunc = compile(array_sum_2, float32, [arraytype(float32, 2, 'C')])
    a = np.arange(10, dtype=np.float32).reshape(2, 5)
    assertTrue(np.allclose(cfunc(a), np.sum(a)))

@testcase
def test_array_prod_1():
    cfunc = compile(array_prod_1, float32, [arraytype(float32, 1, 'C')])
    a = np.arange(10, dtype=np.float32)
    assertTrue(np.allclose(cfunc(a), a.prod()))

@testcase
def test_array_prod_2():
    cfunc = compile(array_prod_2, float32, [arraytype(float32, 1, 'C')])
    a = np.arange(10, dtype=np.float32)
    assertTrue(np.allclose(cfunc(a), a.prod()))

if __name__ == '__main__':
    main()

