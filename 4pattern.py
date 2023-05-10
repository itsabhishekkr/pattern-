

n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print("@", end="")#end="" is use for prevent the line change
        j=j+1
    print()
    i=i+1
# 1111
# 3333 this types 0f pattern
# 4444
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(i,end="")
        j=j+1
    print()
    i=i+1
#1234
# 1234
# 1234
# 1234
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(j,end="")
        j=j+1
    print()
    i=i+1  
#4321
# 4321
# 4321
# 4321
# 4321
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(((n+1)-j),end="")
        j=j+1
    print()
    i=i+1      