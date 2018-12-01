import time
time0=time.time()
input="0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"
blocks=[int(block) for block in input.split('\t')]
size=len(blocks)
steps=0
states=[blocks[:]]
high=0
while (8):
  max=0
  start=0
  for index,block in enumerate(blocks): #get max
    if (block>max):
      max=block;
      start=index;
  blocks[start]=0;
  for i in range(max): #spread block contents
    k=(i+start+1)%size;
    blocks[k]+=1;
  steps+=1;
  for state in states: #check loop
    for i,old in enumerate(state):
	  new=blocks[i];
	  if (not new==old):
	    if (i>high):
		  high=i;
		  print high
	    break;
    else:
      time1=time.time()
      delta=time1-time0;
      print "looped in " + str(steps) + " steps, and", delta, "seconds"
      exit()
  states.append(blocks[:])