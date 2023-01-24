import pytest

import calc


def setup_function():
    print("This is for setup")


@pytest.fixture()
def my_fixture1():
    data = 7
    yield data
    data = 0


@pytest.fixture(params=["param1", "param2"])
def my_fixture2(request):
    data = request.param
    yield data
    data = None


def test_add1():
    assert calc.add(1, 2) == 3


def test_add2(my_fixture1):
    assert calc.add(my_fixture1, 2) == 9


def test_list(my_fixture2):
    if my_fixture2 == "param1":
        assert "param1" in my_fixture2
    elif my_fixture2 == "param2":
        assert "param2" in my_fixture2


@pytest.mark.skip("This test will be skipped")
def test_false():
    assert False


@pytest.mark.skipif(3 > 1, reason="This test is not avaliable")
def test_true():
    assert True


def test_skip():
    if True:
        pytest.skip("This test will be skipped")


@pytest.mark.multiply
def test_multiply1():
    assert calc.multiply(2, 3) == 6


@pytest.mark.multiply
def test_multiply2():
    assert calc.multiply(3, 4) == 12


def teardown_function():
    print("This is for teardown")
