#coding=utf-8
import configparser
import codecs
import os

#专门读取配置文件.ini文件格式

class ReadConfig:
    def __init__(self,filename):
        #configpath=os.path.join(prjDir,filename)
        configpath=filename
        #print(configpath)
        fd=open(configpath)
        data=fd.read()
        #remove BOM
        if data[:3]==codecs.BOM_UTF8:
            data=data[3:]
            files=codecs.open(configpath,"w")
            files.write(data)
            files.close()
        fd.close()

        self.cf=configparser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self,env,name):
        return self.cf.get(env,name)