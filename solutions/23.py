import sys
import re
import operator as op
input="""\
set b 57
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23""" 
try:
  registers=dict()
  curr=0;
  instructions = input.split('\n')
  instCount= len(instructions);
  muls=0
  while (8):
    # print curr
    # print registers
    # raw_input()
    if (curr not in range(instCount)):
      raise Exception('leak')
    instruct = instructions[curr];
    args = instruct.split(' ')
    command, reg = args[0:2]
    if (reg not in registers):
      if (str(reg).isalpha()): # add reg to dict
        registers[reg]=0;
      else:
        reg = int(reg) #reg is num
    if (len(args) != 3):
      raise Exception ("bad argc")
    else: #commands af
      value = args[2];
      #set value to int or register value
      if (value.isalpha()):
        if (value not in registers):
          raise Exception("using uninitialized register")
        else:
          value = registers[value];
      else:
        value = int(value);
  #pick command and execute
      if (command == 'set'):
        registers[reg]=value;
      elif(command == 'sub'):
        registers[reg]-=value;
      elif(command == 'mul'):
        muls+=1;
        registers[reg]*=value;
      elif(command == 'jnz'):
        if (str(reg).isalpha()):
          if (registers[reg] != 0):
            curr+=value-1
        else:
          if (reg != 0):
            curr+=value-1
      else:
        raise Exception("bad command")
    curr+=1; #iterate
except Exception as e:
  print muls,"muls"
  print str(e), sys.exc_info()[2].tb_lineno
finally:
  raw_input()