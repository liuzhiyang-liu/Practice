f = open('file created','w')

for i in range(1,11111):
    data='step %d\n' %i
    f.write(data)

f.close()
