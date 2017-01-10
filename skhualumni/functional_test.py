from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('홈 화면', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
