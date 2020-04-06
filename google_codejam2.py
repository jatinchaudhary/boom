test=int(input())

kk=1


while kk<=test:



    a=list(input())

    b=list(map(int,a))


    def brac(start,end,minn):
        tar=-1
        length=len(a)
        i=0
        done=0
        while i<length:
            if a[i]!=')' and a[i]!='(':
                tar+=1

        
            if tar==start and done!=1:
                cp=i
                for j in range(minn):
                    a.insert(cp,'(')
                    cp+=1
                i=i+minn-1
                tar-=1
                done=1
                length=length+minn
       

            if tar==end:
                cp=i+1
                for j in range(minn):
                    a.insert(cp,')')
                break
            i+=1
        


    def cut(start,end,minn):
        for i in range(start,end+1):
            b[i]=b[i]-minn


    i=0
    start=-1
    minn=0
    end=-1
    length=len(b)

    while i<length:

        if b[i]!=0:
            if start==-1:
                start=i
                end=i
                minn=b[i]
            else:
                end=i
                if b[i]<minn:
                    minn=b[i]

        if (i==length-1 or b[i]==0) and start!=-1:
            brac(start,end,minn)
            cut(start,end,minn)
            i=-1
            start=-1
            minn=0
            end=-1


        i+=1
    
    a="".join(a)
    print("Case #{}: {}".format(kk,a))

    kk+=1
