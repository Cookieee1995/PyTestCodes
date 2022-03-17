import pytest

@pytest.mark.skipif('sys.platform == "linux"',reason="不适合在 linux 中运行")
def test_skipif1():
    assert 1 == 2

@pytest.mark.skipif('sys.platform != "linux"')
def test_skipif2():
    assert 1 == 1
