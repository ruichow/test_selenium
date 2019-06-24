# coding=utf-8

from time import sleep

from public.common.log import Log

log = Log()


def test_login(self, name, password):
    driver = self.driver
    # 选择版本
    driver.find_element_by_id("zentao").click()
    log.info("点击按钮:id=zentao")
    sleep(2)

    # 输入用户名
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(name)
    log.info("输入用户名：")

    # 输入密码
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    log.info("输入密码：")

    # 点击登录按钮
    driver.find_element_by_id("submit").click()
    log.info("点击按钮：id=submit")

    # 获取断言信息进行断言
    # 异常判断
    try:
        text = driver.find_element_by_id("companyname").text
    except:
        print("不存在此元素")
    try:
        text = driver.find_element_by_xpath("//*[@id='companyname']/a").text
    except:
        print("叫爸爸")
    print(text)
    self.assertEqual(text, u"易软天创")
