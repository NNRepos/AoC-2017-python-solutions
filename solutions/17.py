input=363;
steps=input;
insertions=2018;
curr=0;
spinSpan=[0]
for i in range(1, insertions):
  curr = ((curr + steps) % i) + 1;
  spinSpan.insert(curr, i);
print spinSpan[curr+1]