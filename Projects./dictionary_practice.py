"""" EXIT TICKET """
# Rename this file here & call it week4_exit.py

## Part I: Create a dictionary

# Create your food table here via key:value pairs
# (input the food & prices from lines 73-76):
food_prices = {
  "grapes": 1.36,
  "cheeseburger": 2.76,
  "avocados": 1.67,
  "steak": 4.59
  }

print(food_prices)

# Retrieve any value from the food prices dictionary by using its corresponding key along with the bracket notation
# For example, to get the price for cheese, run this:
avocado_price = food_prices["avocados"]
print(avocado_price)

# Access the prices for each item & store into their own variable, just like the milk example.  
grapes_price = food_prices["grapes"]
cheeseburger_price = food_prices["cheeseburger"]
steak_price = food_prices["steak"]

# Print those variables to check that you get the right value. Write the code to print on the line below:
print(food_prices)

## Part II. Create a list of the Spotify playlist

# First, add the songs in your section's list in 
playlist = [
  "The Kid LAROI, Justin Bieber - STAY",
  "Meqobitey Ketema - Diacon Brhane",
  "Stranger Things | Title Sequence",
  "Panjabi MC - Mundian To Bach Ke "
]

# Print the playlist in the line below:
print(playlist)
first_song = playlist[0]
# Lists have an index, which is a number assigned to each item in the list based on the oder in which they appear in the list, starting at 0. 
# What's the first song on your list?
#WE(Warm Embrace) - Chris Brown

print(first_song)

# Pick your top 2 favorite songs from the list & print them using the list's index to access them
fave_songs = playlist[2:3]
print(fave_songs)

# Update your playlist by changing the last song to something else
playlist[3] = "Nicky Youre, dazy - Sunroof"
# print the playlist to show that you have updated it
print(playlist)

# Add another song to the end of the list using append()
playlist.append(" Begenay Yelil Aleku (በገናይ የልዕል ኣለኹ) ")
# print the playlist to show that you added a new song
print(playlist)

# You changed your mind & want to delete the last song you just added
playlist.pop()
# Print the playlist to show that you deleted the last song
print(playlist)

# How many songs are in your list? Use len()
print(len(playlist))
# Write here how many songs are in your playlist = 

# Sort your playlist in alphabetical order using sorted()
print(sorted(playlist))
# Write here the order of the songs in your playlist:
# 
