import sys
import re
import operator as op
input="""\
14/42
2/3
6/44
4/10
23/49
35/39
46/46
5/29
13/20
33/9
24/50
0/30
9/10
41/44
35/50
44/50
5/11
21/24
7/39
46/31
38/38
22/26
8/9
16/4
23/39
26/5
40/40
29/29
5/20
3/32
42/11
16/14
27/49
36/20
18/39
49/41
16/6
24/46
44/48
36/4
6/6
13/6
42/12
29/41
39/39
9/3
30/2
25/20
15/6
15/23
28/40
8/7
26/23
48/10
28/28
2/13
48/14\
""" 
try:
  cables=input.split('\n')
  cables= [cable.split('/') for cable in cables]
  cables = [[int(port) for port in cable] for cable in cables]
  currPort=0;
  maxStrength=currStrength=0;
  maxLength=currLength=0;
  longest=[]
  def build(port, strength, lst, length):
    try:
      global maxLength
      global longest
      if length > maxLength:
        longest=[]
        maxLength=length;
      if length == maxLength:
        longest.append(strength)
      for cable in lst:
        if (cable[0] == port):
          newlst=list(lst)
          newlst.remove(cable)
          build(cable[1], strength + sum(cable), newlst, length+1)
        elif (cable[1] == port):
          newlst=list(lst)
          newlst.remove(cable)
          build(cable[0], strength + sum(cable), newlst, length+1)
    except Exception as e:
      print str(e),sys.exc_info()[2].tb_lineno
      
    
  #main
  build(0,0,cables,currLength)
  # print longest
  print max(longest)
        
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()