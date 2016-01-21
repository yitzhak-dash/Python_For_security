class MyClass_1(object):
    a = 1


print MyClass_1.a
# print MyClass.b -> error

MyClass_1.b = "hello"
print MyClass_1.b


class MyClass(object):
    def __init__(self, msg, num):
        self.msg = msg
        self.num = num
        print self.msg
        print self.num
        return


mc = MyClass("message here", 543)


class CustomException(Exception):
    def __init__(self, error):
        super(Exception, self).__init__(error)
        self.message = error
        return

    def __str__(self):
        return "Error: %s" % self.message
