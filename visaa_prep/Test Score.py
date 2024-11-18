a,b,c=map(int,input().split())
x=a*b
if(c<=x and c%b==0):
    print("YES")
else:
    print("NO")
