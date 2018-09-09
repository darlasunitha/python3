num=int(raw_input())
k=0
for i in range(3,num//3+1):
    if(num%i==0):
        k=k+1
if(k<=0):
    print("yes")
else:
    print("no")
