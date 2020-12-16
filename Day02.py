f=open(r"/content/Day2.txt", 'r', encoding='utf-8')
codes=f.read().splitlines()

Noofvalidpasswords1=0
Noofvalidpasswords2=0
k = len(codes)

for i in range(k):
  split1=codes[i].split(':')
  password=split1[1]
  split2=split1[0].split(' ')
  code=split2[1]
  split3=split2[0].split('-')
  leftbound=int(split3[0])  
  rightbound=int(split3[1])

  count = 0
  for char in password:
    if char == code:
      count += 1
  
  if leftbound<=count<=rightbound:
    Noofvalidpasswords1+=1

  
  if (password[leftbound] == code and password[rightbound] != code) or (password[leftbound] != code and password[rightbound] == code):
    Noofvalidpasswords2+=1


print("Task 1:", Noofvalidpasswords1)
print("Task 2:", Noofvalidpasswords2)
