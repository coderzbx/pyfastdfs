__author__ = 'xxp'

class TrackerServer:
    def __init__(self,sock,address):
       self.sock=sock
       self.address=address

    def getSock(self):
        return self.sock

    def getAddress(self):
        return self.address

    def getInputStream(self):
        pass

    def getOutputStream(self):
        pass

    def close(self):
        pass

class TrackerGroup:
    def __init__(self,trackerServers):
        self.trackerServers=trackerServers
        self.trackerServerIndex=0
        
    def getConnection(self,index=-1):
        pass



class StorageServer(TrackerServer):
    def __init__(self,storePath):
        if  storePath<0:
            self.storePathIndex=256+storePath
        else:
            self.storePathIndex=storePath


class TrackerClient:
    def __init__(self,group=None):
        self.trackerGroup=group

class StorageClient:
    pass

        