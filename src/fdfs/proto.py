__author__ = 'xxp'

class RecvPackageInfo:
    def __init__(self,error,body):
        self.errorNo=error
        self.body=body

class RecvHeaderInfo:
    def __init__(self,error,len):
        self.errorNo=error
        self.bodyLength=len

class Proto:
    FDFS_PROTO_CMD_QUIT      = 82
    TRACKER_PROTO_CMD_SERVER_LIST_GROUP     = 91
    TRACKER_PROTO_CMD_SERVER_LIST_STORAGE   = 92
    TRACKER_PROTO_CMD_SERVER_DELETE_STORAGE = 93
    TRACKER_PROTO_CMD_SERVICE_QUERY_STORE_WITHOUT_GROUP_ONE = 101
    TRACKER_PROTO_CMD_SERVICE_QUERY_FETCH_ONE = 102
    TRACKER_PROTO_CMD_SERVICE_QUERY_UPDATE = 103
    TRACKER_PROTO_CMD_SERVICE_QUERY_STORE_WITH_GROUP_ONE = 104
    TRACKER_PROTO_CMD_SERVICE_QUERY_FETCH_ALL = 105
    TRACKER_PROTO_CMD_SERVICE_QUERY_STORE_WITHOUT_GROUP_ALL = 106
    TRACKER_PROTO_CMD_SERVICE_QUERY_STORE_WITH_GROUP_ALL = 107
    TRACKER_PROTO_CMD_RESP = 100
    FDFS_PROTO_CMD_ACTIVE_TEST = 111
    STORAGE_PROTO_CMD_UPLOAD_FILE  = 11
    STORAGE_PROTO_CMD_DELETE_FILE= 12
    STORAGE_PROTO_CMD_SET_METADATA = 13
    STORAGE_PROTO_CMD_DOWNLOAD_FILE = 14
    STORAGE_PROTO_CMD_GET_METADATA = 15
    STORAGE_PROTO_CMD_UPLOAD_SLAVE_FILE   = 21
    STORAGE_PROTO_CMD_QUERY_FILE_INFO     = 22
    STORAGE_PROTO_CMD_UPLOAD_APPENDER_FILE= 23  #create appender file
    STORAGE_PROTO_CMD_APPEND_FILE         = 24  #append file
    STORAGE_PROTO_CMD_RESP = TRACKER_PROTO_CMD_RESP
    FDFS_STORAGE_STATUS_INIT        = 0
    FDFS_STORAGE_STATUS_WAIT_SYNC   = 1
    FDFS_STORAGE_STATUS_SYNCING     = 2
    FDFS_STORAGE_STATUS_IP_CHANGED  = 3
    FDFS_STORAGE_STATUS_DELETED     = 4
    FDFS_STORAGE_STATUS_OFFLINE     = 5
    FDFS_STORAGE_STATUS_ONLINE      = 6
    FDFS_STORAGE_STATUS_ACTIVE      = 7
    FDFS_STORAGE_STATUS_NONE        = 99
    #for overwrite all old metadata
    STORAGE_SET_METADATA_FLAG_OVERWRITE = 'O'
    # for replace, insert when the meta item not exist, otherwise update it
    STORAGE_SET_METADATA_FLAG_MERGE = 'M'
    FDFS_PROTO_PKG_LEN_SIZE= 8
    FDFS_PROTO_CMD_SIZE= 1
    FDFS_GROUP_NAME_MAX_LEN  = 16
    FDFS_IPADDR_SIZE = 16
    FDFS_DOMAIN_NAME_MAX_SIZE = 128
    FDFS_VERSION_SIZE = 6
    FDFS_RECORD_SEPERATOR= "\u0001"
    FDFS_FIELD_SEPERATOR  = "\u0002"
    TRACKER_QUERY_STORAGE_FETCH_BODY_LEN = FDFS_GROUP_NAME_MAX_LEN+ FDFS_IPADDR_SIZE - 1 + FDFS_PROTO_PKG_LEN_SIZE
    TRACKER_QUERY_STORAGE_STORE_BODY_LEN = FDFS_GROUP_NAME_MAX_LEN+ FDFS_IPADDR_SIZE + FDFS_PROTO_PKG_LEN_SIZE
    PROTO_HEADER_CMD_INDEX   = FDFS_PROTO_PKG_LEN_SIZE
    PROTO_HEADER_STATUS_INDEX = FDFS_PROTO_PKG_LEN_SIZE+1
    FDFS_FILE_EXT_NAME_MAX_LEN  = 6
    FDFS_FILE_PREFIX_MAX_LEN    = 16
    FDFS_FILE_PATH_LEN          = 10
    FDFS_FILENAME_BASE64_LENGTH = 27
    ERR_NO_ENOENT    = 2
    ERR_NO_EIO       = 5
    ERR_NO_EBUSY     = 16
    ERR_NO_EINVAL    = 22
    ERR_NO_ENOSPC    = 28
    ECONNREFUSED     = 61
    ERR_NO_EALREADY  = 114
    INFINITE_FILE_SIZE = 256 * 1024L * 1024 * 1024 * 1024 * 1024L
    
    @classmethod
    def getStorageStatusCaption(cls,status):
        if status==Proto.FDFS_STORAGE_STATUS_INIT:
            return "INIT"
        elif status==Proto.FDFS_STORAGE_STATUS_WAIT_SYNC:
            return "WAIT_SYNC"
        elif status==Proto.FDFS_STORAGE_STATUS_SYNCING:
            return "SYNCING"
        elif status==Proto.FDFS_STORAGE_STATUS_IP_CHANGED:
            return "IP_CHANGED"
        elif status==Proto.FDFS_STORAGE_STATUS_DELETED:
            return "DELETED"
        elif status==Proto.FDFS_STORAGE_STATUS_OFFLINE:
            return "OFFLINE"
        elif status==Proto.FDFS_STORAGE_STATUS_ONLINE:
            return "ONLINE"
        elif status==Proto.FDFS_STORAGE_STATUS_ACTIVE:
            return "ACTIVE"
        elif status==Proto.FDFS_STORAGE_STATUS_NONE:
            return "NONE"
        else:
            return "UNKOWN"
    @classmethod
    def packHeader(cls,cmd,pkgLen,errno):
        return None
    @classmethod
    def recvHeader(cls,input,cmd,bodyLen):
        return None
    @classmethod
    def recvPackage(cls,input,cmd,bodyLen):
        return  None
    @classmethod
    def splitMetadata(cls,metaBuff):
        return  None
    @classmethod
    def splitMetadata(cls,metaBuff,recordSeperator,filedSeperator):
        return  None
    @classmethod
    def packMetadata(cls,metaList):
        return None
    @classmethod
    def closeSocket(cls,sock):
        return None
    @classmethod
    def activeTest(cls,sock):
        return False
    @classmethod
    def long2buff(cls,long):
        return None
    @classmethod
    def buff2long(cls,buf,offset):
        return None
    @classmethod
    def buff2int(cls,buf,offset):
        return None
    @classmethod
    def getIpAddress(cls,buf,offset):
        return None
    @classmethod
    def md5(cls,source):
        return None
    @classmethod
    def getToken(cls):
        return None
    @classmethod
    def genSlaveFilename(cls,fileName,prefix,ext):
        return None
    

def decode():
    pass

    
    
    


        
        


if __name__=="__main__":
    print Proto.getStorageStatusCaption(1)