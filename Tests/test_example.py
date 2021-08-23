import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HackernewsSearchTest(unittest.TestCase):


    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )
            

    def test_hackernews_search_for_testdrivernio(self):
        self.browser.get('https://news.ycombinator.com')
        search_box = self.browser.find_element_by_name('q')
        search_box.send_keys('testdriven.io')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn('testdriven.io', self.browser.page_source)

    def test_hackernews_search_for_selenium(self):
        self.browser.get('https://news.ycombinator.com')
        search_box = self.browser.find_element_by_name('q')
        search_box.send_keys('selenium')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('selenium', self.browser.page_source)

    def test_hackernews_search_for_testdriven(self):
        self.browser.get('https://news.ycombinator.com')
        search_box = self.browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('testdriven', self.browser.page_source)

    def test_hackernews_search_with_no_results(self):
        self.browser.get('https://news.ycombinator.com')
        search_box = self.browser.find_element_by_name('q')
        search_box.send_keys('?*^^%')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertNotIn('<em>', self.browser.page_source)


    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()


"""
Notes: 
- Original source obtained from : https://testdriven.io/blog/distributed-testing-with-selenium-grid/
- Versions of Selenium/Hub images; look under tag tab
    - https://hub.docker.com/r/selenium/hub/tags?page=1&ordering=last_updated
"""
