def printinfo(arg1, **var):
    print('arg1', arg1)
    print('*', var)


# 调用printinfo 函数
printinfo(10, a=1, b=2)
