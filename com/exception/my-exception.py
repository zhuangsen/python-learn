# -*- coding: utf-8 -*-
class FileError(IOError):
    pass


try:
    raise FileError, 'test file error'
except FileError, e:
    print e


class CustomError(Exception):
    def __init__(self, info):
        Exception.__init__(self)
        self.errorinfo = info
        print id(self)

    def __str__(self):
        return 'CustomError:%s' % self.errorinfo


try:
    raise CustomError('test CustomError')
except CustomError, e:
    print "ErrorInfo:%d %s" % (id(e), e)
