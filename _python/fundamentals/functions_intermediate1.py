import random
def randInt(min=0   , max=100  ):
  while(min < max and max > 0):
    num = random.random()*(max-min)+min
    return round(num)
print(randInt()) 	
print(randInt(max=50))
print(randInt(min=50)) 	
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
