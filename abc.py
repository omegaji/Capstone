t=int(input())

while t!=0:
    global maxSize
    maxSize=1
    nums=[]
    n=int(input())
    nums=list(map(int,input().split(" ")))
    nums=sorted(nums)
    mindiff=-1
    if len(nums)==1:
        print(1)
    else:
        res=[]
        for i in range(len(nums)):
            if len(res)==0:
                res.append(nums[i])
                continue
            else:
                if mindiff==-1 or abs(res[-1]-nums[i])<mindiff:
                    mindiff=abs(res[-1]-nums[i])
                if mindiff>=nums[i]:
                    res.append(nums[i])
                else:
                    break
        print(len(res))




    

    
    

    


    t=t-1