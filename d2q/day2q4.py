def dn(n):
    n1=str(n*2)
    n=str(n)
    count=0
    for x in n:
        if x in n1:
            count+=1
        else:
            return False
    if count==len(n):
        return True
print(dn(125874))
