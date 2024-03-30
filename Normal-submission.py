m,n=map(int,input().split())
tt=[0]*n
zz=[0]*n
yy=[0]*n

# Input 
for i in range(n):
    t,z,y=map(int,input().split())
    tt[i],zz[i],yy[i]=t,z,y

# Setting the boundried for binary search
# maximum / minimum time it can possibly take to inflate the ballons using the worst case scenario
left=0
right=(m//min(zz))*max(yy)
right+=max(tt)*m

# Intializing the answer in case the ballons to be inflated is Zero
ans=0
res=[0]*n

# the function that cheacks that is it possible to inflate all ballons withing this many minutes
def check(minutes):
    done=0
    worked=[0]*n
    for i in range(n):
        this=0
        if (minutes//tt[i])>zz[i]:
            this+=(minutes//((zz[i]*tt[i])+yy[i]))*zz[i]
            minus=(minutes//((zz[i]*tt[i])+yy[i]))*((zz[i]*tt[i])+yy[i])
            left_min=minutes-minus
            this+=left_min//tt[i]
        else:
            this+=minutes//tt[i]
        done+=this
        worked[i]=this
        if done>=m:
                return [True,worked]
    return [False]


# Binary search from max minutes to minimum minutes to cheack the minimum required minutes to perform the task
while(left<=right and m>0):
    mid=(left+right)//2
    if check(mid)[0]==True:
        ans=mid
        array=check(mid)[1]
        right=mid-1
    else:
        left=mid+1
print(ans)
print(*array)
