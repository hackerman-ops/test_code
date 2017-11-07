
# # -*- coding:utf-8 -*-

import cPickle as pickle
import json
import os

# dumps and loads
# 将内存对象dump为字符串，或者将字符串load为内存对象
# t = {'name': ['v1', 'v2']}
# print(json.dumps(t))
# with open('test.txt', 'w') as fp:
#     fp.write(json.dumps(t))
# with open('test.txt', 'w') as fp:
#     pickle.dump(t, fp)
#
# print t
#
# o = pickle.dumps(t)
# print 'len o: ', len(o)
#
# p = pickle.loads(o)
# print p


# # 关于HIGHEST_PROTOCOL参数，pickle 支持3种protocol，0、1、2：
# # http://stackoverflow.com/questions/23582489/python-pickle-protocol-choice
# # 0：ASCII protocol，兼容旧版本的Python
# # 1：binary format，兼容旧版本的Python
# # 2：binary format，Python2.3 之后才有，更好的支持new-sytle class
# print 'HIGHEST_PROTOCOL: ', pickle.HIGHEST_PROTOCOL
#
# t = {'name': ['v1', 'v2']}
# print t
#
# o = pickle.dumps(t, pickle.HIGHEST_PROTOCOL)
# print o
# print 'len o: ', len(o)
#
# p = pickle.loads(o)
# print p
# print "_-----------"
#
#
# # new-style class
# class TT(object):
#     def __init__(self, arg, **kwargs):
#         super(TT, self).__init__()
#         self.arg = arg
#         self.kwargs = kwargs
#
#     def test(self):
#         print self.arg
#         print self.kwargs
#         print "~~~~~~~~~~~~~"
#
# # ASCII protocol
# t = TT('test', a=1, b=2)
# o1 = pickle.dumps(t)
# print o1
# print "~~~~~~~~~~~~~"
#
# print 'o1 len: ', len(o1)
# p = pickle.loads(o1)
# p.test()
#
# # HIGHEST_PROTOCOL对new-style class支持更好，性能更高
# o2 = pickle.dumps(t, pickle.HIGHEST_PROTOCOL)
# print 'o2 len: ', len(o2)
# print "~~~~~~~~~~~~~"
#
# p = pickle.loads(o2)
# p.test()
# print "_-----------"

#
# dump and load
# 将内存对象序列化后直接dump到文件或支持文件接口的对象中
# 对于dump，需要支持write接口，接受一个字符串作为输入参数，比如：StringIO
# 对于load，需要支持read接口，接受int输入参数，同时支持readline接口，无输入参数，比如StringIO
#
# # 使用文件，ASCII编码
# t = {'name': ['v1', 'v2']}
#
# # ASCII format
# with open('test.txt', 'w') as fp:
#     pickle.dump(t, fp)
#
# with open('test.txt', 'r') as fp:
#     p = pickle.load(fp)
#     print p
# print "_-----------"
#

# 使用文件，二进制编码
# t = {'name': ['v1', 'v2']}
# print os.path.abspath("text.txt")
# dir = os.path.dirname(os.path.abspath("text.txt"))
# dir1 = dir + "/temp/"
# if not os.path.exists(dir1):
#     os.mkdir(dir1)
# with open(dir1+"temp.txt", 'wb') as fp:
#     pickle.dump(t, fp, pickle.HIGHEST_PROTOCOL)
#
# with open(dir1+"temp.txt", 'rb') as fp:
#     p = pickle.load(fp)
#     print p
# print "_-----------"


# # 使用StringIO，二进制编码
# import StringIO
#
# t = {'name': ['v1', 'v2']}
#
# fp = StringIO.StringIO()
# print fp
# pickle.dump(t, fp, pickle.HIGHEST_PROTOCOL)
# print pickle.dump(t, fp, pickle.HIGHEST_PROTOCOL)
#
# fp.seek(0)
# print fp.seek(0)
# p = pickle.load(fp)
# print p
#
# fp.close()
# print "_-----------"
#
#
# 使用自定义类
# 这里演示用户自定义类，只要实现了write、read、readline接口，
# 就可以用作dump、load的file参数
# import StringIO
#
# class FF(object):
#     def __init__(self):
#         self.buf = StringIO.StringIO()
#
#     def write(self, s):
#         self.buf.write(s)
#         print 'len: ', len(s)
#
#     def read(self, n):
#         return self.buf.read(n)
#
#     def readline(self):
#         return self.buf.readline()
#
#     def seek(self, pos, mod=0):
#         return self.buf.seek(pos, mod)
#
#     def close(self):
#         self.buf.close()
#
# fp = FF()
# t = {'name': ['v1', 'v2']}
# pickle.dump(t, fp, pickle.HIGHEST_PROTOCOL)
#
# fp.seek(0)
# p = pickle.load(fp)
# print p
#
# fp.close()
# print "_-----------"
#

# Pickler/Unpickler
# Pickler(file, protocol).dump(obj) 等价于 pickle.dump(obj, file[, protocol])
# Unpickler(file).load() 等价于 pickle.load(file)
# Pickler/Unpickler 封装性更好，可以很方便的替换file
t = {'name': ['v1', 'v2']}

f = file('test.bin', 'wb')
print f
pick = pickle.Pickler(f, pickle.HIGHEST_PROTOCOL)
pick.dump(t)
f.close()

f = file('test.bin', 'rb')
unpick = pickle.Unpickler(f)
p = unpick.load()
print p
f.close()
print "_-----------"


