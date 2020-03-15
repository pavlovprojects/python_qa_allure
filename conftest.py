import pytest
from selenium import webdriver

@pytest.fixture
def browser(request):
    bro = webdriver.Chrome()
    request.addfinalizer(bro.quit)
    return bro

@pytest.fixture
def remote(request):
    bro = webdriver.Chrome()
    request.addfinalizer(bro.quit)
    return bro