import pytest
from selenium import webdriver
#import configparser

# config = configparser.ConfigParser()
# config.read("Utilities/user.ini")

@pytest.fixture
def setup(request):
    # request.cls.driver = webdriver.Chrome()
    request.cls.driver = webdriver.Firefox()
    request.cls.driver.get("https://www.facebook.com/")
    yield
    request.cls.driver.quit()
