n=int(input())
for i in range(2,n):
    s=0
    for j in range(2,i):
        if i%j==0:
            s=1
    if s==0:
        print(i,end=" ")
