import pytest

'''
by default
function - run once per test
class - run once per class of tests
module - run once per module
session - run once per session
'''

@pytest.fixture(scope="session")
def fixture_1():
    print('run-fixture-1')
    return 1

def test_example1(fixture_1):
    print('run-example-1')
    num = fixture_1
    assert num == 1

def test_example2(fixture_1):
    print('run-example-2')
    num = fixture_1
    assert num == 1

# @pytest.mark.slow
# def test_example():
#     print("test1")
#     assert 1 == 1 

# def test_example1():
#     assert 1 == 1