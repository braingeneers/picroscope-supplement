txt = ""
for i in range(1,417):
    txt = txt + ",LED" + str(i)
    if(i%104==0):
        print(txt)
        txt = ""
for i in range(1,417):
    txt = txt + ",R"+ str(i)
print(txt)
