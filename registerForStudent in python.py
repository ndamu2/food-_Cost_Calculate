#===a program that allow students to register for an exam=================
ofile=open("RegForm.txt","w")

student=int(input("how many students are registering"))
print(student)


for i in range (1,student):
    
    iD=input("please enter your ID")
    ofile.write(str(iD) +"\n")
    print(iD)
ofile.close()


