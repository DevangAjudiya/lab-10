f=open("C:\\Users\\lab\\Desktop\\marks.csv")
ls=[]
ls1=[]
ls2=[]
ls3=[]
ls4=[]
ls5=[]
dic={"rlno":ls1,"name":ls2,"cpi":ls3,"maths":ls4,"chem":ls5}
contant=f.readline()
while(contant):
    contant=f.readline()
    ls.append(contant.split(","))
l=len(ls[0])
for i in range(l):
    ls1.append(ls[i][0])
for i in range(l):
    ls2.append(ls[i][1])
for i in range(l):
    ls3.append(ls[i][2])
for i in range(l):
    ls4.append(ls[i][3])
for i in range(l):
    ls5.append(ls[i][4])
print(dic)
    
        
f.close()
