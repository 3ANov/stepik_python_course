def foo():
    assert 1==2

try:
    #ArithmeticError, AssertionError, ZeroDivisionError
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")