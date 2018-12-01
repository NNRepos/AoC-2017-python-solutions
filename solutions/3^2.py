import math
input=277678
size=12; #arbitrary, has to be big enough for range to fit in
grid=[[0 for row in range(size)] for col in range(size)]
grid[0][0]=1;
flag=True
for curr in range(2,60): #2,24 for grid in example
  sqrt=math.sqrt(curr)
  sqrt=math.ceil(sqrt)
  if(not sqrt%2):
    sqrt+=1;
  # print "sqrt is " + str(sqrt)
  innerCircle=(sqrt-2)*(sqrt-2)
  outerRing=sqrt*sqrt-innerCircle
  
  #discover row and column of square
  if (curr<(innerCircle+outerRing/4)):     #number on the right quarter
    row=(( innerCircle + (sqrt-1)/2 ) - curr) % size #negative distance
    col=((sqrt-1) / 2) % size
  elif (curr<(innerCircle+2*outerRing/4)): #top quarter
    row=(-(sqrt-1) / 2) % size
    col=(( innerCircle + 3*(sqrt-1)/2 ) - curr) % size
  elif (curr<(innerCircle+3*outerRing/4)): #left
    row=(curr - ( innerCircle + 5*(sqrt-1)/2 )) % size
    col=(-(sqrt-1) / 2) % size
  else:                                 #bottom
    row=((sqrt-1) / 2) % size
    col=(curr - ( innerCircle + 7*(sqrt-1)/2 )) % size
  
  #set square value
  # print "float row is " + str(row), "int row is " + str(int(row))
  row=int(row)
  col=int(col)
  grid[row][col]= \
  grid[(row-1)%size][(col-1)%size] + grid[(row-1)%size][(col)%size] + grid[(row-1)%size][(col+1)%size] + \
  grid[(row)%size][(col-1)%size]                +                   grid[(row)%size][(col+1)%size] + \
  grid[(row+1)%size][(col-1)%size] + grid[(row+1)%size][(col)%size] + grid[(row+1)%size][(col+1)%size]; #modulo is probably not necessary but meh 
  if (grid[row][col] > input and flag):
    ans=grid[row][col];
    flag=False;
  # print "grid changed to: \n"
  # for gri in grid:
    # print gri
print "answer is " + str(ans)