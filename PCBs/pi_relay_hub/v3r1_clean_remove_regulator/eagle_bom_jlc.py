f = open('eagle_bom.csv','r')
fo = open('jlc_bom.csv','w')
fo.write('Comment,Designator,Footprint,LCSC Part #(optional)\n')
index_count = 0
skip = 10
for line in f:
    if(index_count>=skip):

        #temp = line.split('      ')
        #temp = line.split('      ')
        temp = line.split(';')
        print(index_count,len(temp[1]))
        if(temp[1])!='':
            print('1',len(temp),temp)
            fo.write(temp[1] + ',' + temp[0] + ',' + temp[3] + ',,\n')
        else:
            temp = line.split('     ')
            print('2',len(temp),temp)
            fo.write(temp[1] + ',' + temp[0] + ',' + temp[3] + ',,\n')
    index_count = index_count + 1
fo.close()
