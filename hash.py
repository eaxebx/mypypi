# -*- coding: utf-8 -*-

import sys
import hashlib

def getmd5(fname):
    """获取文件的md5值.
    
    :param str: 文件名
    :return: md5值
    :rtype: str
    """
    m = hashlib.md5()
    with open(fname, 'rb') as f:
        while True:
            data = f.read(10240)
            if not data:
                break
            m.update(data)
            
    return m.hexdigest()
        
def getsha1(fname):
    """获取文件的sha1值.
    
    :param str: 文件名
    :return: sha1值
    :rtype: str
    """
    m = hashlib.sha1()
    with open(fname, 'rb') as f:
        while True:
            data = f.read(10240)
            if not data:
                break
            m.update(data)
            
    return m.hexdigest()
    
if __name__ == '__main__':
    fname = sys.argv[1]
    print(fname)
    print('md5:  ', getmd5(fname))
    print('sha1: ', getsha1(fname))