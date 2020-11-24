"""
sum = 0
i = 1
while i<1001:
  i=i+1
  if(i%3==0):
    sum=sum+i
print(sum)

"""
"""
i = 0
j = 0
for i in range(0,6):
  for j in range(0,i):
    print("*",end="")
  print()
"""
"""
for i in range(1,101):
  print(i)
"""
sum = 0
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for point in score:
   sum=sum+point
print(sum/len(score))
