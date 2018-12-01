from collections import deque
input=\
"""set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 464
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19\
"""
registers=[0]*2;
registers[0]=dict()
registers[1]=dict({'p':1})
curr=[0]*2;
curr[0]=0;
curr[1]=0;
sent=[0]*2;
sent[0]=deque()
sent[1]=deque()
deadlock=[0]*2;
deadlock[0]=0;
deadlock[1]=0;
running=0; #which of the 2 processes is active?
instructions = input.split('\n')
instCount= len(instructions);
sentBy1=0;
for i in range (123456):#while (8):
  if (curr[running] not in range(instCount)):
    print "error - leaked out"
    exit()
  instruct = instructions[curr[running]];
  args = instruct.split(' ')
  command= args[0];
  regOrNum=0;
  if (args[1].isalpha()):
    reg = args[1];
    regOrNum=1;
  if (regOrNum and (reg not in registers[running])): # add reg to dict
    registers[running][reg]=0;

  if (len(args) > 2): #3 args instruction
    value = args[2];
#set value to int or register value
    if (value.isalpha()):
      if (value not in registers[running]):
        print "error, third argument not in registers[running]"
      else:
        value = registers[running][value];
    else:
      value = int(value);
#pick command and execute
    if (command == 'set'):
      registers[running][reg]=value;
    elif(command == 'add'):
      registers[running][reg]+=value;
    elif(command == 'mul'):
      registers[running][reg]*=value;
    elif(command == 'mod'):
      registers[running][reg]%=value;
    elif(command == 'jgz'): #pay attention: reg can be a number
      if regOrNum:
        comparator=registers[running][reg];
      else:
        comparator=args[1];
      if (comparator > 0):
        curr[running]+= (value-1);
    else:
      print "error, wrong command 3 args"
      exit()
  else: # 2 args instruction
    other = int(not(running));
    if (command == 'snd'):
      if (running == 1):
        sentBy1+=1;
      sent[running].append(registers[running][reg]); #add to my queue
      deadlock[other]=0;
    elif(command == 'rcv'):
      # print "before",
      if (len(sent[other]) == 0): #deck empty
        deadlock[running] = 1;
        running = other; #switcheroo
        curr[running]-=1;
      else:
        received = sent[other].popleft(); #get value from deck
        registers[running][reg] = received;
      if (deadlock[0] and deadlock[1]):
        print "is dead, program 1 sent", sentBy1, "values."
        exit()
      # print "after",running
    else:
      print "error, wrong command 2 args"
      exit()
  #finally
  curr[running]+=1;