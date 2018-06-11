from ctypes import *
libtest = cdll.LoadLibrary(r"C:\Users\User\Documents\dersler\ders4\test.dll")
print(libtest.multiply(2, 2))
