import pandas as pd
import matplotlib.pyplot as plt

# Get data from listings.csv and set x and y for the hexbin
data = pd.read_csv('../data/raw/listings.csv')
x = data['longitude']
y = data['latitude']

# The Hexbin Plot display between 5th and 95th percentile
x05 = data['longitude'].quantile(.05)
x95 = data['longitude'].quantile(.95)
y05 = data['latitude'].quantile(.05)
y95 = data['latitude'].quantile(.95)

# Create plot and set color
plt.hexbin(x,y, cmap = 'pink_r')

# Describe the meaning of the cbar/cmap
cbar = plt.colorbar()
cbar.set_label('Number of Listings')

# Set axis limit
ax = plt.subplot(111)
ax.set_xlim([x05,x95])
ax.set_ylim([y05,y95])

# Add Labels and Title
ax.set_title("Berlin Airbnb Listing Frequency by Latitude and Longitude")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Improve graph readability by reducing extra lines and tick labels
plt.box(False)
plt.locator_params(axis='y', nbins=6)
plt.locator_params(axis='x', nbins=3)

# Annotations for the median
ax.annotate('MD', xy = (x.quantile(.5),y.quantile(.5)))
# Atles Musuem, located on Musuem Island and close to numerous other attractions
ax.annotate('AM', xy = (13.3965558,52.5194665))
# Großer Tiergarten, major urban park that is home to multiple Berlin landmarks
ax.annotate('GB', xy = (13.3652706,52.5169585))

# Show plot
plt.show()