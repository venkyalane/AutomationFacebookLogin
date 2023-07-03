from selenium.webdriver.common.by import By


class Massage:
    def __init__(self, driver):
        self.driver = driver
        self.text_msg_xpath = "//input[@placeholder='Search Facebook']"

    def msg(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Search Facebook']").get_attribute("placeholder")

