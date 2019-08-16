# ML-with-Visuals
+ [Project Description](#Project Description)
+ [Findings](#Findings)
+ [Setting up the Envirnonment](#Setting up the Envirnonment)
+ [Acknowledgements](#Acknowledgements)

## Project Description
This repo seeks to explore Berlin Airbnb data and determine how listing are distributed across the city as well as to make predictions on the pricing of such listings.

## Findings
So far, it has been determined that Airbnb listings are centered around 52.509824 N, 13.406107 E. This location is very close to Museum Island, which is surrounded by numerous attractions and landmarks. Interestingly enough, the "mean" location listing is some distance removed from Großer Tiergarten, a major urban park that encompasses numerous Berlin landmarks including the Reichstag. This is probably due to the airport being on the western side of the city, thus reducing the number of listing available in that area as well as the park itself, which does cover a large part of the city. This visualization below was created in `visuals/visualHexbin.py` and shows the frequency of Airbnb listings based on location. Note that the graph only displays data that fell between the 5th and 95th percentile for both latitude and longitude. This was done to account of geographic outliers as well as provide an enlarged view of the data.

![graph](visuals/HexbinofLatLonFrequency.png)

Graph Annotations:
* MD: calculated median of data
* AT: The Altes Museum, which is located on Museum Island
* GT: Major Urban Park that encompasses the Reichstag

## Setting up the Envirnonment
* `pip install -r requirements.txt`

## Acknowledgements
* Data taken from [Kaggle](https://www.kaggle.com/brittabettendorf/berlin-airbnb-data) 
* Project organization is based on [Cookie Cutter Data Science](https://github.com/drivendata/cookiecutter-data-science)
