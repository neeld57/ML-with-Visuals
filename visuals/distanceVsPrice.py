import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# Get data from listings.csv and set x and y for the hexbin
data = pd.read_csv('../data/raw/listings.csv')
x = data['longitude']
y = data['latitude']
distance = []

# The Point from which we will take distance and price
# In this case we use AM: Atles Musuem as our point
pointlong = 13.3965558
pointlat  = 52.5194665

# Now we will append distance with its distance in km and price,
# Note data is limited in order to show the distribution in-depth
for a,b,c in zip(x,y,data['price']):
    if(c<300 and (sqrt((pointlong-a)*(pointlong-a) + (pointlat-b)*(pointlat-b)))*(0.000001107042925553966/0.00000001)<20):
        distance.append([(sqrt((pointlong-a)*(pointlong-a) + (pointlat-b)*(pointlat-b)))*(0.000001107042925553966/0.00000001),c])

# Shape Distance and then convert it to a DataFrame
distance = np.reshape(distance,(-1,2))
DistancePrice = pd.DataFrame({'Distance (km)' : distance[:,0],'Price (€)' : distance[:,1]})
print(DistancePrice)


# Plot using DF data
# Scatter Plot
ax1 = plt.subplot(121)
ax1.set_xlabel('Distance (km)')
ax1.set_ylabel('Price (€)')
ax1 = plt.scatter(DistancePrice['Distance (km)'],DistancePrice['Price (€)'], c = 'tan')
plt.box(False)
plt.title('Scatter Plot')

# Hexbin Plot
ax2 = plt.subplot(122)
ax2.set_xlabel('Distance (km)')
ax2 = plt.hexbin(DistancePrice['Distance (km)'],DistancePrice['Price (€)'], gridsize=25,cmap = 'copper_r')
cbar = plt.colorbar()
cbar.set_label('Number of Listings')
plt.yticks([], [])
plt.title('Hexbin Plot')
plt.box(False)

plt.suptitle("Distance (km) from Atles Musuem versus Pricing of a Listing")
plt.show()