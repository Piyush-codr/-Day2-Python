#list
'''n=int(input())
s=input()
print("",len(s),len(n))'''

def f1(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
             continue
    return [l_count, d_count]
print(f1("Infosys 123"))
