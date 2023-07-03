import time

import pytest
from PageObject.loginpage import Login
from PageObject.dashboardpage import Massage
from Utilities.logfile import LogClass


@pytest.mark.usefixtures("setup")
class Test_login(LogClass):
    def test_001(self):
        """Login with correct credential"""
        log = self.get_the_logs()
        lg = Login(self.driver)
        wel = Massage(self.driver)

        log.info("This is the test 001")
        log.info("Test case started")

        log.info("Entered username")
        lg.input_username(username)

        log.info("Entered password")
        lg.input_password(password)
        self.driver.save_screenshot('Screenshots\\test_cred_001.png')
        time.sleep(5)
        log.info("clicked on login button")
        lg.login()
        time.sleep(5)

        try:
            if "Search Facebook" in wel.msg():
                assert True
                log.info("Test case passed")
                self.driver.save_screenshot('Screenshots\\test_pass_001.png')
                time.sleep(5)
            else:
                self.driver.save_screenshot("Screenshots\\test_fail_001.png")
                log.critical("Test case failed")
                assert False

        except:
            log.info("test case 001 failed due to element not found")
            log.critical("Test Case 001 fail")


    def test_002(self):
        """Login with invalid credential"""
        log1 = self.get_the_logs1()
        lg = Login(self.driver)

        log1.info("This is test 002")
        log1.info("Test case started")

        log1.info("Entered correct username")
        lg.input_username(username)

        log1.info("Entered Wrong password")
        lg.input_password(password)

        log1.info("Clicked on login button")
        lg.login()
        time.sleep(5)

        try:
            if "The password that you've entered is incorrect. Forgotten password?" in lg.invalid_msg():
                assert True
                time.sleep(5)
                self.driver.save_screenshot("Screenshots\\test_pass_002.png")
                log1.info("test case passed")
            else:
                self.driver.save_screenshot("Screenshots\\test_fail_002.png")
                log1.critical("Test case failed")
                assert False

        except:
            log1.info("Test Case 002 failed due to element not found")
            log1.critical("Test Case 002 fail")

