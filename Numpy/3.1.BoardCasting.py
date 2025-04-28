prices = [100,200,300,400]

discount = 10

finalPrices = []

for price in prices:
    finalPrice = price - (price * discount / 100)
    finalPrices.append(finalPrice)
    
print("Final Array: ", finalPrices)

# [90.0, 180.0, 270.0, 360.0]
  
# /////////////////////////////////////  
# Here we gonna use BoardCasting
# /////////////////////////////////////  



import numpy as np

newPrice = np.array(prices)

finalPrice2 = newPrice - (newPrice * discount / 100)

print("Numpy Array: ",finalPrice2)


# [ 90. 180. 270. 360.]

# new I gonna double the Prices of invertory in shope.

# with Single Value
newPrices = finalPrice2 * 2
print(newPrices)

# [180. 360. 540. 720.]
