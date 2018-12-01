def main():
  # import sys
  input="wenycdww"
  grid=[]
  gridsize=128;
  for g in range(gridsize):
    if not (g%16 or g==0):
      print str(12.5*g/16) + "%", "done"
    key=input + "-" + str(g);
    suffix=[17, 31, 73, 47, 23]
    rounds=64;
    asciiput=[]
    for k in key:
      asciiput.append(ord(k))
    asciiput.extend(suffix)
    lengths=asciiput;
    lengths=lengths*rounds;
    size=256;
    leest=range(size)
    skip=0;
    curr=0;
    for length in lengths:
      length=int(length)
      temp=[]
      for i in range(curr, curr+length): #take out relevant items
        temp.append(leest[i%size])
      for index,item in enumerate(reversed(temp)): #put them back in
        leest[(curr+index)%size]=item
      curr+=length+skip;
      skip+=1;
    sparse=leest;
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
    grid.append(hash)
  #until here it all stays the same
  # sys.stdout=open('grid.txt', 'w');
  formatArg="0" + str(gridsize) + "b";
  for i,hush in enumerate(grid):
    grid[i]=format((int(hush,16)), formatArg) 
  # sys.stdout = sys.__stdout__;
  for i,line in enumerate(grid):
    grid[i]=list(str(line));
  curr=1;
  for i,line in enumerate(grid):
    for j,dig in enumerate(line):
      if (dig == '1'):
        curr+=1;
        infect(i, j, curr, grid)
  print "number of regions is",curr-1 #we started counting from 2

def infect(row, col, region, grid):
  grid[row][col]=str(region);
  if (row > 0 and grid[row-1][col] == '1'):
    infect(row-1, col, region, grid);
  if (row < 127 and grid[row+1][col] == '1'):
    infect(row+1, col, region, grid);
  if (col > 0 and grid[row][col-1] == '1'):
    infect(row, col-1, region, grid);
  if (col < 127 and grid[row][col+1] == '1'):
    infect(row, col+1, region, grid);

if __name__=="__main__":
  main();