import math
input=277678
sqrt=math.sqrt(input)
# print "initial sqrt == " + str(sqrt)
sqrt=math.ceil(sqrt)
if(not sqrt%2):
  sqrt+=1;
# print sqrt
innerCircle=(sqrt-2)*(sqrt-2)
outerRing=sqrt*sqrt-innerCircle
# print "circles are " + str(innerCircle) + " + " + str(outerRing) + \
# " = " + str(innerCircle+outerRing)
#pick a quarter
if (input<(innerCircle+outerRing/4)):     #number on the right quarter
  distance=input - ( innerCircle + (sqrt-1)/2 )
elif (input<(innerCircle+2*outerRing/4)): #top quarter
  distance=input - ( innerCircle + 3*(sqrt-1)/2 )
elif (input<(innerCircle+3*outerRing/4)): #left
  distance=input - ( innerCircle + 5*(sqrt-1)/2 )
else:                                  #bottom
  distance=input - ( innerCircle + 7*(sqrt-1)/2 )
# print "dist so far: " + str(distance)
distance = abs(distance) + (sqrt-1)/2
print distance