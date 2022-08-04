for i in open("ck.txt","r"):
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
    elif "shimla" in i :
        f=open("shimla.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
    else:
        f=open("other.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
print("succussfull !!!")