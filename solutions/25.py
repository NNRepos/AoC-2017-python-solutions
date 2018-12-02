import sys
import re
import operator as op
input="""\
Begin in state A.
Perform a diagnostic checksum after 12794428 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state F.

In state B:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state D.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.

In state D:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state E:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
""" 
try:
  steps=12794428
  tape=[0]*(steps*2)
  minCurr=maxCurr=curr=steps
  state='A'
  for i in range(steps):
    minCurr=min(minCurr,curr);
    maxCurr=max(maxCurr,curr);
    if not i%100000:
      print i,':',minCurr,maxCurr
    #states
    if (state == 'A'): 
      if not tape[curr]: #0
        tape[curr]=1
        curr+=1
        state='B'
      else:
        tape[curr]=0
        curr-=1
        state='F'
    elif (state == 'B'):
      if not tape[curr]: #0
        curr+=1
        state='C'
      else:
        tape[curr]=0
        curr+=1
        state='D'
    elif (state == 'C'):
      if not tape[curr]: #0
        tape[curr]=1
        curr-=1
        state='D'
      else:
        curr+=1
        state='E'
    elif (state == 'D'):
      if not tape[curr]: #0
        curr-=1
        state='E'
      else:
        tape[curr]=0
        curr-=1
        state='D'
    elif (state == 'E'):
      if not tape[curr]: #0
        curr+=1
        state='A'
      else:
        curr+=1
        state='C'
    elif (state == 'F'):
      if not tape[curr]: #0
        tape[curr]=1
        curr-=1
        state='A'
      else:
        curr+=1
        state='A'
    else:
      raise Exception("bad state")
    
  print sum(tape)
    
        
    
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()