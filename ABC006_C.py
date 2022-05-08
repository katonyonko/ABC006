import io
import sys

_INPUT = """\
6
3 9
7 23
10 41
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  if M<N*2 or M>N*4: print(-1,-1,-1)
  elif M<=N*3: print(N-M+2*N,M-2*N,0)
  else: print(0,N*4-M,N-N*4+M)