vov_count=0
con_count=0
a = open("l.txt","r")
for i in a.read():
        # print(i)
        if i =='a' or i =='e' or i =='i' or i =='o' or i =='u':
            vov_count+=1
        # elif i ==" ":
        #     continue
        else:
            con_count+=1
print(vov_count,'\n',con_count)