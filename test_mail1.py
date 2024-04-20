import pytest
@pytest.fixture

def setup():
    print('Authorization successfully complete')
    yield #return gen
    print('exit')

def test_send_mail1(setup): #collecting ... collected 1 item
    #1 passed in 0.01s
    print('Message have been sent')

def test_send_mail2(setup):
    print('Message have been sent')

'''
pytest -v every command testing + %
Test_mail.py::test_send_mail1 PASSED [ 50%] 

-s without percent complete
Test_mail.py Authorization successfully complete
Message have been sent

-s - v 
Test_mail.py::test_send_mail1 Authorization successfully complete
Message have been sent
PASSED
'''
