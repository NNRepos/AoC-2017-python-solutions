input=363;
steps=input;
insertions=50*1000*1000; #no data this time so it's not that slow
curr=0;
second=1;
for i in range(1, insertions):
  curr = ((curr + steps) % i) + 1;
  if (curr == 1): #after 0
    second=i;
print "it's", second