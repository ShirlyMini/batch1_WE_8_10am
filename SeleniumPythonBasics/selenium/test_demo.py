import pytest

@pytest.fixture()
def setup():
    print("this is setup method")
    yield
    print("this is teardown method")

def testMethod1(setup):
    print("This is test method1")

def testMethod2(setup):
    print("This is test method2")