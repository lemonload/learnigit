from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://wwww.baidu.com/"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTsetRunner")
        driver.find_element_by_id("kw").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":

    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    #定义报告存放路径
    fp = open('./result.html','wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况:')

    runner.run(testunit)
    fp.close()