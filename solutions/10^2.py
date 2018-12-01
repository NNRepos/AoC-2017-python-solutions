input=\
"""106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118"""
suffix=[17, 31, 73, 47, 23]
rounds=64;
asciiput=[]
for i in input:
  asciiput.append(ord(i))
asciiput.extend(suffix)
lengths=asciiput;
lengths=lengths*64;
size=256;
list=range(size)
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
sparse=list;
# print "sparse:",sparse
dense=[0]*16;
for index,val in enumerate(sparse): #xor the blocks
  dense[index/16]^=val;
# print "dense",dense
hash=[]
for d in dense: #get nonhex values
  hash.append(d/16)
  hash.append(d%16)
for h in range (len(hash)):
  if hash[h]<10:
    hash[h]=chr(ord('0')+hash[h])
  else:
    hash[h]=chr(ord('a')+hash[h]-10)
hash=''.join(hash)
print "hash:",hash
