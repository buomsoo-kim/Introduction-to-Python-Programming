import pandas as pd

title = ['Skyfall', 'Lose Yourself', 'Another Brick in the Wall', 'Use Somebody', 'Treasure']
artist = ['Adele', 'Eminem', 'Pink Floyd', 'Kings of Leon', 'Bruno Mars']
length = ['4:46', '5:26', '3:59', '3:51', '2:58']
year = [2012, 2002, 1979, 2008, 2013]
data = pd.DataFrame({'Title': title, 'Artist': artist, 'Length': length, 'Year': year})

print(data)