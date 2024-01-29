
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()


# class PythonOrgSearch(unittest.TestCase):
#     def SeleniumCall(site_name):
#         url = 'https://www.whoscored.com/Statistics'
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         # self.driver = webdriver.Chrome('chrome')
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get(site_name)
#         # driver.get(url)
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element(By.NAME, "q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         self.assertNotIn("No results found.", driver.page_source)
#
#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()