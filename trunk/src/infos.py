__author__ = 'xxp'
'''

'''
class FileInfo:
    def __init__(self,size,time,crc):
        print "hello"
        self.size=size
        self.creatTime=time
        self.crc32=crc
'''

'''
class ServerInfo:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port

    def connect(self):
        return None
    
class NameValuePair:
    def __init__(self,name,value):
        self.name=name
        self.value=value
        
if __name__=="__main__":
    ff=FileInfo(10,100,12)
    print ff.crc32
    print ff.size
    print ff.creatTime
    

        