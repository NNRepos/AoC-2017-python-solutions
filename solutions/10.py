input=\
"""106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118"""
size=256;
list=range(size)
#print list
lengths=input.split(',')
skip=0;
curr=0;
for length in lengths:
  length=int(length)
  temp=[]
  for i in range(curr, curr+length): #take out relevant items
    temp.append(list[i%size])
  for index,item in enumerate(reversed(temp)): #put them back in
    list[(curr+index)%size]=item
  curr+=length+skip;
  skip+=1;
print "final list:\n" + str(list)
print "\nfinal answer: " + str(list[0]*list[1])