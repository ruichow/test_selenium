# coding=utf-8
import os
import time
import unittest
import xml.dom.minidom
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

from public.common.log import Log
from public.pages import loginPage

log = Log()

# 获取当前路径的父路径
PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),"..",p))


#打开xml文件
dom = xml.dom.minidom.parse(PATH("data\\url.xml"))

#得到元素对象
root = dom.documentElement


class AddChanPing(unittest.TestCase):
    '''添加产品'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 获取xml元素对象
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.driver.implicitly_wait(30)  # 智能等待时间
        self.logger = Log()
        self.logger.info("################# START ##############")
        self.driver.maximize_window()
        self.verificationErrors = []  # 错误日志收集

    def test_addchanping(self):
        driver = self.driver
        driver.get(self.base_url)

        # 调用登录函数
        loginPage.test_login(self, "admin", "admin1234")
        sleep(3)

        # 点击产品
        driver.find_element_by_link_text("产品").click()
        log.info("点击按钮：link_text=产品")

        """
        try:
            adb = driver.find_element_by_xpath("//*[@id='block11']/div[1]/nav/li[1]/a").text
            if adb == ' 添加产品':
                driver.find_element_by_xpath("//*[@id='block11']/div[1]/nav/li[1]/a").click()
            else:
                print("呵呵")
        except:
            print("叫爸爸")
        
        try:
            driver.find_element_by_xpath("//*[@id='block11']/div[1]/nav/li[1]/a")
            a = True
            if a == True:
                print("哈哈，我是真的")
            else:
                print("哈哈，我是假的")
        except:
            time.sleep(1)
         """
        # 点击添加产品下拉框选择点击产品（抛异常）
        try:
            tianjiachanping=driver.find_element_by_link_text("添加产品").text

            if tianjiachanping=="添加产品":
                driver.find_element_by_link_text("添加产品").click()
                log.info("下拉框：class_name=btn-group")
            else:
                print("此元素不叫添加产品")
        except:
            log.info("此元素不存在")

        # 获取当前时间用于参数设置
        now_time = time.strftime("%H-%M-%S")
        print(now_time)

        # 输入产品名称（判断产品名称输入框是否存在）
        try:
            driver.find_element_by_id("name")
            b=True
            if b==True:
                driver.find_element_by_id("name").clear()
                driver.find_element_by_id("name").send_keys(u"禅道项目" + now_time)
                text = "禅道项目" + now_time
                print(text)
                log.info("输入产品名称：禅道项目")
            else:
                log.info("找不到产品名称输入框")
        except:
            log.info("产品名称元素不存在")


        # 输入产品代号（循环）
        k=1
        while k<100:
            k=k+1
            if now_time==20-54-20:
                driver.find_element_by_id("code").clear()
                driver.find_element_by_id("code").send_keys(now_time)
                log.info("产品代号：now_time")
            else:
                log.info("产品代号不符合要求")

        # 选择产品线
        driver.find_element_by_xpath("//*[@id='line_chosen']/a/div[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='line_chosen']/div/ul/li[2]").click()

        """ 键盘操作
        driver.find_element_by_xpath("//*[@id='line_chosen']/a/div[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='line_chosen']/a/span").send_keys(Keys.DOWN)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='line_chosen']/a/span").send_keys(Keys.ENTER)
        """

        log.info("产品线：id=line")

        # 选择产品类型
        sel = driver.find_element_by_id("type")
        Select(sel).select_by_value("branch")
        log.info("选择产品类型:id=type")


        # 产品描述
        xf = driver.find_element_by_css_selector(".ke-edit-iframe")  # iframe没有id和name，使用css元素赋值然后访问
        driver.switch_to.frame(xf)
        driver.find_element_by_class_name("article-content").send_keys("测试")
        log.info("产品描述输入：测试")
        sleep(5)

        # 从frame中切回主文档中
        driver.switch_to.default_content()
        sleep(1)

        # 将滚动条拖到最底部
        js = "var action=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        sleep(2)

        # 访问控制
        driver.find_element_by_id("aclprivate").click()
        log.info("访问控制：id=aclprivate")

        # 点击保存
        driver.find_element_by_id("submit").click()
        log.info("点击保存按钮：id=submit")
        time.sleep(2)

        # 获取浏览器弹出保存成功的提示信息
        prompt = Alert(driver)
        print('prompt text : ' + prompt.text)

        #######获取断言信息进行断言#######

        self.assertEqual(prompt.text, u"保存成功")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(AddChanPing("def test_addchanping"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
