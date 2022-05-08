import io
import sys

_INPUT = """\
6
7
1
1000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  n=int(input())
  tri=[0,0,1]
  if n<=3: print(tri[n-1])
  else:
    for i in range(n-3):
      tri.append((tri[-1]+tri[-2]+tri[-3])%10007)
    print(tri[-1])