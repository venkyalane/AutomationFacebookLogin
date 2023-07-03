import pytest
from selenium import webdriver


@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Firefox()
    request.cls.driver.get("https://www.facebook.com/")
    yield
    request.cls.driver.quit()
