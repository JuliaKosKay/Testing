import unittest
from selenium import webdriver


class PracticeSeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_menu_navigation(self):
        driver = self.driver
        driver.get("http://www.practiceselenium.com/")

        # Навигация по меню
        driver.find_element_by_link_text("Check Out").click()
        self.assertEqual(driver.current_url, "http://www.practiceselenium.com/check-out.html")

        driver.back()

        driver.find_element_by_link_text("Menu").click()
        self.assertEqual(driver.current_url, "http://www.practiceselenium.com/menu.html")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()