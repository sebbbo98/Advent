f=open(r"/content/Day3.txt", 'r', encoding='utf-8')
geology=f.read().splitlines()
k=len(geology)

Treecountfinal=[0,0,0,0,0]
slope=[1,3,5,7,1]

for x in range(4):
  j=0
  Treecount=0
  for i in range(k):
    line=geology[i]
  
    if line[j] == "#" :
      Treecount+=1

    if j<(31-slope[x]):
      j+=slope[x]
    else:
     j-=(31-slope[x])
  Treecountfinal[x]=Treecount
j=0
Treecount=0
for i in range(int(k/2+1)):
  line=geology[2*i]
  if line[j] == "#" :
      Treecount+=1 
  if j<(31-slope[4]):
      j+=slope[4]
  else:
     j-=(31-slope[4])
Treecountfinal[4]=Treecount

final=1
for z in range(len(Treecountfinal)):

  final*=Treecountfinal[z]
print(geology[0])
print("Task1:", Treecountfinal)
print("Task2:", final)
