#! /usr/bin/python
r=[550,215]
q=[0]
x=[1,0]
y=[0,1]
target=0

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
  if target != 0 and target >= remainder:
  	d = target/remainder
  	result_x = calculate_x*d
  	result_y = calculate_y*d

  	break
  
print('R=', r)
print('Q=', q)
print('X=', x)
print('Y=', y)
if target != 0:
	print('result x to target', result_x)
	print('result y to target', result_y)

a