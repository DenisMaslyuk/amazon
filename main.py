import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Xtremax_Test(unittest.TestCase):
    base_url = "https://www.amazon.com/"
    product_url = "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A1266092011%2Cn%3A172659&dc&qid=1574062578&rnid=1266092011&ref=sr_nr_n_13"


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_search_product(self):

        self.driver.get(self.base_url)

        # check if redirect to robot checker page, must input captcha manually
        if self.driver.title == "Robort Checker":
            captBtn = self.driver.find_element_by_xpath("//button[@type='submit']")
            captBtn.click()


        # move into television section
        hamburger_menu = self.driver.find_element_by_xpath("//a[@id='nav-hamburger-menu']")
        hamburger_menu.click()
        electronics = self.driver.find_element_by_xpath("//a[@data-ref-tag='nav_em_1_1_1_6']")
        electronics.click()
        television_video = self.driver.find_element_by_xpath("//div[@id='hmenu-content']/ul[5]/li[15]/a")
        television_video.click()
        televisions = self.driver.find_element_by_xpath("//li[@id='n/172659']/span/a/span")
        televisions.click()

        # check tv 32 inches and under
        tele32inches = self.driver.find_element_by_xpath("//li[@id='p_n_size_browse-bin/1232879011']/span/a/span")
        tele32inches.click()

        # filter under $150
        highPriceBox = self.driver.find_element_by_id("high-price")
        highPriceBox.clear()
        highPriceBox.send_keys("150")
        highPriceBox.send_keys(Keys.RETURN)

        # # sort by Price: High to Low
        sortSelectBtn = Select(self.driver.find_element_by_id("s-result-sort-select"))
        sortSelectBtn.select_by_visible_text("Price: High to Low")

        # click first product
        self.driver.find_element_by_xpath(
            "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[1]").click()

        # add to wishtlist
        self.driver.find_elements_by_id("add-to-cart-button")[0].click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_result'))