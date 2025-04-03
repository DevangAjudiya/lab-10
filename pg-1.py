f=open("C:\\Users\\lab\\Desktop\\marks.csv","a+")
rlno=input("enter roll no.[enter to end]")
while rlno:
    nm,cp2,math,ch = input("enter name,marks of cpi,math and chem").split()
    f.write(rlno+','+nm+','+cp2+','+math+','+ch+','+'\n')
    rlno=input("enter roll no.[enter to end]")
f.close()

