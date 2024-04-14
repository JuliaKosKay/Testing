import pytest
@pytest.fixture

def set_up():
    print('Authorization successfully complete')
    yield #return gen
    print('exit')

@pytest.fixture(scope = 'module')

def setup():
    print('Start')
    yield #return gen
    print('end')
