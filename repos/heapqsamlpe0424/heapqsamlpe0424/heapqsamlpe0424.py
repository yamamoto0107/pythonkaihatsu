N,M,K=20,20,4#map(int,input("20 20 4 ,1 2 3 4").split())
A=[1,2,3,4]#list(map(int,input().split()))
N=abs(M-N)
print("N,M,K is",N,M,K)
print("A is",A)
print("N,M,K is",type(N),type(M),type(K))
print("A is",type(A))
from heapq import *
MAX=25000
G=[[] for i in range(MAX)]
D=[0]*MAX
INF=10**17
def ijk(s):
  global D,INF,G
  for i in range(len(G)):
    D[i]=INF
  D[s]=0
  Q=[]
  heapify(Q)
  heappush(Q,(0,s))
  p,v,e=0,0,0
  while len(Q):
    p=heappop(Q)
    v=p[1]
    if D[v]<p[0]:
      continue
    for i in range(len(G[v])):
      e=G[v][i]
      if D[e[0]]>D[v]+e[1]:
        D[e[0]]=D[v]+e[1]
        heappush(Q,(D[e[0]],e[0]))

for i in range(MAX):
  print("i is ",i)
  for j in range(K):
    print("j is ",j,"A[j] is ",A[j])
    if A[j]<=i:
      print("A[j]<=i is ",A[j],i)
      G[i].append((i-A[j],1))
    if i+A[j]<MAX:
      print("A[j]+i<=MAX is ",A[j]+i,MAX)
      G[i].append((i+A[j],1))
      print(G[i])
ijk(0)
if D[N]>=INF:
  print(-1)
else:
  print(D[N])
