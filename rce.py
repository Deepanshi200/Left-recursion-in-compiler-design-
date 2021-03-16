t = int(input("Enter the NUMBER productions "))
pro=[]
remm=[]
for tt in range(t):
    pro.append(input())
print("****#######*******************************")
for trr in pro:
    rr=trr
    #rr=input()
    qr = rr[0]
    rr=rr.split('=')[1]
    rr=rr.split('|')
    lr=[]
    nlr=[]
    for q in rr:
        if(q[0]==qr):
            lr.append(q)
        else:
            nlr.append(q)
    if(len(lr)>0):

        print("LEFT RECURSION IN: ")
        for k in lr:
            print(str(k[0])+"="+k)
    if(len(lr)==0):
        remm.append(trr)
    if(len(lr)>0):
        print(" ")
        print("REMOVAL")
        for k in nlr:
            rem1 = (str(qr)+"="+str(k)+str(qr)+"'"+"|")
            print(rem1)
            remm.append(rem1)
        
        for k in lr:
            rem2 = (str(qr)+"'="+(str(k))[1:len(k)]+str(qr)+"'"+"|"+"eps")
            print(rem2)
            remm.append(rem2)
        
        
        print(" ")
        print("****#######*******************************")
print("FINAL GRAMMAR")
for k in remm:
    print(k)