import io
import sys

_INPUT = """\
6
2
9
3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=input()
  if '3' in N or int(N)%3==0: print('YES')
  else: print('NO')