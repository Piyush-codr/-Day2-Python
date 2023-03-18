def f1(str1):
    if(len(str1)<2):
       return -1
    else:
        return str1[0:2]+ str1[-2:]
f1("W3resource")
f1("W3")
f1("B")
