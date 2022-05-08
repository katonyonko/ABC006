import io
import sys

_INPUT = """\
6
6
1
3
5
2
4
6
5
5
4
3
2
1
7
1
2
3
4
5
6
7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from bisect import bisect_left
  def LIS(A: list):
      L = [A[0]]
      ID=[0]*len(A)
      for i in range(1,len(A)):
          if A[i] > L[-1]:
              L.append(A[i])
              ID[i]=len(L)-1
          else:
              tmp=bisect_left(L, A[i])
              L[tmp] = A[i]
              ID[i]=tmp
      L2=[]
      L3=[]
      m=len(L)-1
      for i in range(len(A)-1,-1,-1):
          if ID[i]==m:
              L2.append(A[i])
              L3.append(i)
              m-=1
      return len(L), L2[::-1], L3[::-1] #それぞれ最長増加部分列の長さ、復元した部分列、そのインデックス
  N=int(input())
  c=[int(input()) for _ in range(N)]
  print(N-LIS(c)[0])