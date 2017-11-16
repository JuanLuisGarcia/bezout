#! /usr/bin/python
r=[23,10]
q=[0]
x=[1,0]
y=[0,1]

while r[-1] != 0:
  list_position = len(q)
  result = r[list_position-1]//r[-1]
  remainder = r[list_position-1]%r[-1]
  
  q.append(result)
  r.append(remainder)

  list_position=len(q)
  calculate_x = x[list_position-2]- (x[-1]*q[-1])
  x.append(calculate_x)
  calculate_y = y[list_position-2]- (y[-1]*q[-1])
  y.append(calculate_y)
  
  
print('R=', r)
print('Q=', q)
print('X=', x)
print('Y=', y)
