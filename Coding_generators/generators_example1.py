import time

def generate_values(n):
  while n >= 0:
    yield n
    n-=1

g = generate_values(10)
for x in g:
  print(x)
  time.sleep(1)

'''
output:
10
9
8
7
6
5
4
3
2
1
0
'''
