# coding=utf-8
# 添加项目
import time
from time import sleep

from selenium.webdriver.support.select import Select

from public.common import mytest
from public.common.log import Log
from public.pages.loginPage import LoginPage

log = Log()


class AddXiangMu(mytest.MyTest):
    '''添加项目'''

    def test_addxiangmu(self):
        driver = self.driver

        # 调用登录函数
        LoginPage.login(self, "admin", "admin1234")  # 输入登录用户名和密码
        sleep(5)

        # 点击项目
        driver.find_element_by_link_text("项目").click()
        log.info("点击按钮：link_text=项目")

        # 点击项目主页下拉框
        driver.find_element_by_class_name("btn-group").click()
        log.info("点击下拉框：class_name=btn-group")
        sleep(3)

        # 选择添加项目,点击
        driver.find_element_by_link_text("添加项目").click()
        log.info("选择点击：link_text=添加项目")
        sleep(2)

        # 获取当前时间，用于参数设置
        now_time = time.strftime('%H%M%S')
        print(now_time)

        # 输入项目名称
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"不动如山" + now_time)
        log.info("项目名称输入：id=name")
        text1 = "不动如山" + now_time
        print(text1)

        # 输入项目代号
        driver.find_element_by_id("code").clear()
        driver.find_element_by_id("code").send_keys(now_time)
        log.info("项目代号输入:id=code")

        # 选择起始日期
        driver.find_element_by_id("delta7").click()
        log.info("起始日期选择：id=delta7")

        # 输入团队名称
        driver.find_element_by_id("team").click()
        driver.find_element_by_id("team").send_keys(u"动如脱兔" + now_time)
        log.info("团队名称：id=team")

        # 选择项目类型
        sel1 = driver.find_element_by_id("type")
        Select(sel1).select_by_index(0)
        log.info("项目类型选择下拉框第一个选项")

        # 项目描述
        xf1 = driver.find_element_by_css_selector(".ke-edit-iframe")
        driver.switch_to.frame(xf1)
        driver.find_element_by_class_name("article-content").send_keys("测试项目")
        log.info("项目描述：class_name=article-content")

        # 从frame中切回到主文档中
        driver.switch_to.default_content()

        # 访问控制选择
        driver.find_element_by_id("aclopen").click()
        log.info("访问控制：id=aclopen")

        # 点击保存按钮
        driver.find_element_by_id("submit").click()
        log.info("保存：id=submit")
