# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)


# **********************************Biggie Size****************************************

def convert (a):
  for i in range (0,len(a),1):
    if a[i]>0:
      a[i]='big'
  return a
print(convert([-1, 3, 5, -5]))

# *******************************Count Positives***************************************************

def positive(a):
  count=0
  for i in range (0,len(a),1):
    if a[i]>0:
      count+=1
  a[len(a)-1]=count
  return a

print(positive([1,6,-4,-2,-7,-2]))

# ******************************Sum total****************************************************

def add(a):
  sum=0
  for i in range (0,len(a),1):
    sum+=a[i]
  return sum
# print(add([1,2,3,4]))
print(add([6,3,-2]))



# ******************************Average ****************************************************

def average(a):
  sum=0
  for i in range(0,len(a),1):
    sum+=a[i]
  avg=sum/(len(a))
  return avg

print(average([1,2,3,4]))



# ******************************Length****************************************************

def example(a):
  return len(a)

# print(example([]))
print(example([37,2,1,-9]))


# *****************************Minimum*****************************************************

def minimum(a):
  min=0
  if len(a)==0:
    return 'false'
  for i in range(0,len(a),1):
    if min>a[i]:
      min=a[i]
      return min
    
    

print(minimum([37,2,1,-9]))
# print(minimum([]))
# **********************************Maximum************************************************

def maximum(a):
  max=0
  if len(a)==0:
    return 'false'
  for i in range (0,len(a),1):
    if max < a[i]:
      max=a[i]
  return max

print(maximum([37,2,1,-9]))


# *********************************Ultimate Analysis*************************************************


def specs(a):
  details ={'sumTotal': 0, 'average': 0, 'minimum': 0, 'maximum':0, 'length': len(a) }
  for i in range (0,len(a),1):
    details['sumTotal']+=a[i]
    
    if details['maximum'] < a[i]:
      details['maximum']=a[i]
    if details['minimum']>a[i]:
      details['minimum']=a[i]
  details['average']=details['sumTotal']/len(a)
  
  return details



# print(specs([1,2,3,4,5]))
# print(specs(([37,2,1,-9])))

# **************************************Reverse List********************************************

def Reverse_List(list):
    for i in range(0, int(len(list)/2)):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
print(Reverse_List([37,2,1,-9]))