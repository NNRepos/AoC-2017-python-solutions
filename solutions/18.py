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
registers=dict()
curr=0;
instructions = input.split('\n')
instCount= len(instructions);
lastPlayed=0;
while (8):
  if (curr not in range(instCount)):
    print "error - leaked out"
    exit()
  instruct = instructions[curr];
  args = instruct.split(' ')
  command, reg = args[0:2]
  if reg not in registers: # add reg to dict
    registers[reg]=0;

  if (len(args) > 2): #3 args instruction
    value = args[2];
#set value to int or register value
    if (value.isalpha()):
      if (value not in registers):
        print "error, third argument not in registers"
      else:
        value = registers[value];
    else:
      value = int(value);
#pick command and execute
    if (command == 'set'):
      registers[reg]=value;
    elif(command == 'add'):
      registers[reg]+=value;
    elif(command == 'mul'):
      registers[reg]*=value;
    elif(command == 'mod'):
      registers[reg]%=value;
    elif(command == 'jgz'):
      if (registers[reg] > 0):
        curr+= (value-1);
    else:
      print "error, wrong command 3 args"
      exit()
  else: # 2 args instruction
    if (command == 'snd'):
      lastPlayed = registers[reg];
      # print "played reg",reg,"with value",registers[reg]
    elif(command == 'rcv'):
      print "lastPlayed is",lastPlayed;
      exit()
    else:
      print "error, wrong command 2 args"
      exit()
  #finally
  curr+=1;