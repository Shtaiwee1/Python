# ************************************BASICS**************************
for x in range(0,151,1):
  print(x)

# ***********************Multiples of Five********************************************
for x in range(5 , 1000 ,5):
  print(x)
# *******************Counting, the Dojo Way************************************************

for x in range(100):
  if x%5==0:
    print("coding")
  elif x%10==0:
    print("dojo")

# *********************Whoa. That Sucker's Huge**********************************************
sum = 0
min=0
max=500000
for x in range(0,500000,1):
  if x%3==0:
    sum+=x
  else:
    continue
  print("the sum of odd numbers from {}to{} is {} ".format(min,max,sum))
# **********************Countdown by Fours*********************************************
for x in range(2018,0,-4):
  print(x)
# **************************Flexible Counter *********************************************************

lowNum=2
highNum=100
mult=3
for x in range(2,100,1):
  if x%mult==0:
    print (x)
  else:
    continue
