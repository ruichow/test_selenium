#重要的全局参数，如log、report的路径配置等
#coding=utf-8

import os
from public.common.readconfig import ReadConfig

#读取配置文件
config_file_path=os.path.split(os.path.realpath(__file__))[0]
print(config_file_path)
read_config=ReadConfig(os.path.join(config_file_path,"config.ini"))
#项目参数设置
prj_path=read_config.getValue("projectConfig","project_path")
#日志路径
log_path=os.path.join(prj_path,"report","log")
print(log_path)
#截图文件路径
img_path=os.path.join(prj_path,"report","image")
#测试报告路径
report_path=os.path.join(prj_path,"report","testreport")
print(report_path)
#默认浏览器
browser="Chrome"
#测试数据路径
data_path=os.path.join(prj_path,"data","testdata")