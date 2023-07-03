from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.text_username_xpath = "//input[@id='email']"
        self.text_password_xpath = "//input[@id='pass']"
        self.button_login_xpath = "//button[@name='login']"
        self.invalid_text_xpath = "//body/div[@id='u_0_0_FZ']/div[@id='globalContainer']/div[@id='content']/div[" \
                                  "1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]"

    def input_username(self, username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def invalid_msg(self):
        self.driver.find_element(By.XPATH, self.invalid_text_xpath)

