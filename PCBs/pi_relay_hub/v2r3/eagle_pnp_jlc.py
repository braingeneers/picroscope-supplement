f = open('picrocope_hub_v2r3.mnt','r')
fo = open('jlc_pnp.csv','w')
fo.write('Designator,Mid X,Mid Y,Layer,Rotation\n')
index_count = 0
skip = 0
for line in f:
    if(index_count>=skip):

        #temp = line.split('      ')
        temp = line.split(',')

        fo.write(temp[0] + ',' + temp[1] + ',' + temp[2] + ',Top,' + temp[3]+ ',\n')

    index_count = index_count + 1
fo.close()
