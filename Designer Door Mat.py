import math

n, m = map(int,input().split())
mid = int(n/2)
#print(mid)

ch = '.|.'

# we will have 3 sections -- 1st (0 -> mid), 2nd (mid section), 3rd(mid+1 -> end)
for i in range(n):
    if(i == mid):
        print('WELCOME'.center(m,'-'),end='')
    elif(i<mid):
        print((ch*(2*i+1)).center(m,'-'),end='')
        #print()
    else:
        print((ch*(2*(n-i)-1)).center(m,'-'),end='')
        
    print()    
     

