a = lambda x: x + 1
print a(1)
print a(a(a(10)))


def lambdaconstuct(increaseval):
    return lambda x: x + increaseval


a = lambdaconstuct(4)
print a(1)
