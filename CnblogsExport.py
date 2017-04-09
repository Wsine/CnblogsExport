#!/usr/bin/env python3

from selenium import webdriver
from time import sleep
import json

class CnblogsExport(object):
    """
    An Exportor for cnblogs.com
    """

    def __init__(self, config):
        """
        Return a CnblogsExport object with user name and passowrd for login
        """
        self.userInfo = config['userInfo']
        self.outputDir = config['outputDir']
        self.driver = self.get_web_driver(config['webDriver'])
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_web_driver(self, webDriver):
        if webDriver == 'Chrome':
            return webdriver.Chrome()
        elif webDriver == 'Edge':
            return webdriver.Edge()
        elif webDriver == 'Firefox':
            return webdriver.Firefox()
        elif webDriver == 'Safari':
            return webdriver.Safari()
        else:
            return webdriver.Chrome()

    def login(self):
        self.driver.get('https://passport.cnblogs.com/user/signin')
        self.driver.find_element_by_id('input1').send_keys(self.userInfo['username'])
        self.driver.find_element_by_id('input2').send_keys(self.userInfo['password'])
        self.driver.find_element_by_id('signin').click()
        sleep(2)
        welcome = self.driver.find_element_by_id('lnk_current_user')
        assert self.userInfo['username'] in welcome.text

    def get_all_categoryIds(self):
        self.driver.get('https://i.cnblogs.com/categories')
        text = self.driver.find_element_by_tag_name('body').text
        return json.loads(text)

    def run(self):
        self.login()
        print(self.get_all_categoryIds())

