#coding=utf-8

import unittest
import HTMLTestRunner
import time
from config import globalparam
from public.common import sendmail

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_*.py')
    print(test_dir)
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='自动化测试报告',
            description='用例执行情况'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

if __name__=='__main__':
    run()


