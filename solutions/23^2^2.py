try:
  import sys
  import math
  def prime(num):
    div=2;
    while (div <math.sqrt(num)+1):
      if (not num%div):
        # print "num:",num,"div:",div
        return True
      div+=1
    print num,"is prime",num%17
    return False
  #main
  primes=0
  for i in range(1001):
    if prime(105700+17*i):
      primes+=1
  print "primes:",primes
except Exception as e:
  print str(e), sys.exc_info()[2].tb_lineno
finally:
  raw_input()

print "running original code:"
#what the code really does, O(primeSize*primeSize*primeCount)
a=1
b=105700
c=122700
h=0

#count NOT primes between b and c
while(b!=c): #outer loop
  f=1
  for d in range(3,b): #middle loop
    for e in range(3,b): #inner loop
    #f stays 1 only if b is not divisible by d,e
      if ((e-1)*(d-1)-b) == 0:
        f=0;
  if (f==0):
    h+=1
  b+=17
