input="""Generator A starts with 277
Generator B starts with 349"""
divisor=2147483647;
factorA=16807;
factorB=48271;
modulus=2**16;
rounds=40*1000*1000;
currA=int(((input.split('\n'))[0].split(' '))[4])
currB=int(((input.split('\n'))[1].split(' '))[4])
matches=0;
for i in range(rounds):
  if not (i%(rounds/20) or i==0):
    print str((100*i/rounds)) + "%"
  currA= (currA*factorA) % divisor;
  currB= (currB*factorB) % divisor;
  if ( (currA%modulus) == (currB%modulus)):
    matches+=1;
print matches,"matches."