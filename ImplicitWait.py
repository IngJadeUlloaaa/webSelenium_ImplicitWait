import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This is a class that sets up a webdriver for Microsoft Edge using the unittest module in Python.
class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')

    def test_using_unittest(self):
        """
        This function uses the unittest library to test the ability of a driver to find a dynamic element
        on the Google homepage.
        """
        driver = self.driver
        driver.implicitly_wait(5) # wait for 5seconds
        driver.get('https://www.google.com')
        myDynamicElement = driver.find_element(By.NAME, 'q')
if __name__ == '__main__':
    unittest.main()