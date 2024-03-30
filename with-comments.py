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
answer_array=[0]*n

# the function that cheacks that is it possible to inflate all ballons withing this many minutes
def check(minutes):
    # total balons Inflated 
    done=0

    # Ballons inflated by each worker = worked []
    worked=[0]*n

    # looping through each worker and cheacking how many ballons they can possibly inflate in the given minutes

    for i in range(n):
        # this variable is used to keep track how many ballons did the current worker inflate

        this=0
        # cheacking if the worker need to take a break while inflating the ballons
        # if yes then we will need to add the break time and stuff

        if (minutes//tt[i])>zz[i]:
            # (minutes//((zz[i]*tt[i])+yy[i])) denotes how many time will the worker need break..multiplies by total ballons inflated in that 
            this+=(minutes//((zz[i]*tt[i])+yy[i]))*zz[i]

            # we remove the minutes taken to perform the above step
            # how many times the worker need break multiplies by time taken to do that (inflate z ballions and take rest) we would subtract this from minutes to see spare minutes left..
            
            minus=(minutes//((zz[i]*tt[i])+yy[i]))*((zz[i]*tt[i])+yy[i])
            left_min=minutes-minus

            # there can still be some minutes left where the worker doesn't need break
            this+=left_min//tt[i]

        # in case worker doesn't need break then we simply add the number of ballons the worker can inflate
        else:
            this+=minutes//tt[i]
        
        # addind the current work to total 
        done+=this

        # keeping track of the worked done by individual worker
        worked[i]=this

        # if our goal to inflate all ballons is done then no need to cheack further
        if done>=m:
                return [True,worked]

    # once the loop is over means there was no feasible solution
    return [False]


# Binary search from max minutes to minimum minutes to cheack the minimum required minutes to perform the task
while(left<=right and m>0):
    mid=(left+right)//2
    if check(mid)[0]==True:
        # if it's possible to inflate all ballons in this much minutes store the current answer and look for smaller answer (less minutes)
        ans=mid
        answer_array=check(mid)[1]
        right=mid-1
    else:
        # increase the left in case the current minutes are not enough to inflate all ballons
        left=mid+1
print(ans)
print(*answer_array)
