import sys
import re
import operator as op

input="""\
..#..##...##.######.##...
..#...#####..#.#####..#..
...##.#..##.#.##....#...#
#.#.#.#..###...#....##..#
..#..#####.....##..#.#..#
.##.#####.#.....###.#..#.
##..####...#.##.#...##...
###.#.#####...##.#.##..#.
#.##..##.#....#.#..#.##..
###.######......####..#.#
###.....#.##.##.######..#
...####.###.#....#..##.##
#..####.#.....#....###.#.
#..##..#.####.#.##..#.#..
#..#.#.##...#...#####.##.
#.###..#.##.#..##.#######
...###..#..####.####.#.#.
.#..###..###.#....#######
.####..##.#####.#.#..#.#.
#.#....##.....##.##.....#
....####.....#..#.##..##.
######..##..#.###...###..
..##...##.....#..###.###.
##.#.#..##.#.#.##....##.#
.#.###..##..#....#...##.#""" 
size=1000;
start=500;
iterations=10000000;
try:
  input=input.split('\n')
  lenInputY=len(input)
  lenInputX=len(input[0])
  map = ['.'*size for i in range(size)]
  # print lenInputX,lenInputY
  for i in range(len(input)):
    map[start+i]=map[start+i][:start]+input[i]+map[start+i][start+len(input[i]):]
  directions=['up','right','down','left'];
  dirLen=len(directions);
  
  def isValid(x, y):
    if (x>0 and x<size and y>0 and y<size):
      return True
    return False
  
  def advance(x, y, direction):
    toMyRight=(direction+1)%dirLen
    toMyLeft=(direction-1)%dirLen
    toMyBack=(direction+2)%dirLen
    if (map[y][x] == '.'):
      # print "b4:",y,x,map[y][x-5:x+5],"and",map[y][x],len(map[y])
      map[y]=map[y][:x]+'W'+map[y][x+1:]
      # print "after:",y,x,map[y][x-5:x+5],"and",map[y][x],len(map[y])
      # raw_input()
      if(isValid(*forward(x,y,toMyLeft))):
        return forward(x,y,toMyLeft) + [toMyLeft]
      else:
        raise Exception("out of map premises")
    elif (map[y][x] == '#'):
      map[y]=map[y][:x]+'F'+map[y][x+1:]
      if (isValid(*forward(x,y,toMyRight))):
        return forward(x,y,toMyRight) + [toMyRight]
      else:
        raise Exception("out of map premises")
    elif (map[y][x] == 'F'):
      map[y]=map[y][:x]+'.'+map[y][x+1:]
      if (isValid(*forward(x,y,toMyBack))):
        return forward(x,y,toMyBack) + [toMyBack]
      else:
        raise Exception("out of map premises")
    elif (map[y][x] == 'W'):
      map[y]=map[y][:x]+'#'+map[y][x+1:]
      if (isValid(*forward(x,y,direction))):
        return forward(x,y,direction) + [direction]
      else:
        raise Exception("out of map premises")
    else:
      raise Exception("bad character detected on map")
  
  def forward(x, y, direction):
    if (direction==0):
      return [x,y-1];
    elif (direction==1):
      return [x+1,y];
    elif (direction==2):
      return [x,y+1];
    elif (direction==3):
      return [x-1,y];
    else:
      raise Exception("bad direction")
  #main
  startY=start+lenInputY/2
  startX=start+lenInputX/2
  currX, currY = startX, startY;
  oneDirection=0;
  infected=0;
  #mainloop
  for counter in range(iterations):
    if (not counter%100000):
      print counter,"iterations"
    if (map[currY][currX] == 'W'):
      infected+=1;
    currX,currY,oneDirection=advance(currX,currY,oneDirection);
  print infected
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()