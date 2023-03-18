def find_pair(l,n):
    count=0
    a=len(l)
    for i in range(0,a-1):
        for j in range(i+1,a):
            if(l[i]+l[j]==n):
                count=count+1
    return count
print(find_pair([1,2,7,4,5,6,0,3],6))

