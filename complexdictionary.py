names=[]
sum=0
for i in range (0,5,1):
    nametemp=""
    fdbktemp=""
    nametemp= input("Enter your Name")
    fdbktemp= int(input("Enter feedback rating out of 10"))
    sum+=fdbktemp
    dictionarytemp={"name": nametemp, "fdbk":fdbktemp }
    names.append(dictionarytemp)

for i in range (0,5,1):
    print(names[i])

print((str(sum/5)) + "is the average")