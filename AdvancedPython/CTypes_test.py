from ctypes import *

print c_int(1)
a = c_int(1)
print(a)

cdll.msvcrt.printf("aaa")
print cdll.user32
print windll.user32.MessageBoxA(0, "click yes or no\n", "This a title\n", 4)
