# Objects Explained
inty = 5
listy = [6,7]

stringy = "Hi"

import folium
azores = folium.folium.Map(location = (38, -27),
                    zoom_start = 6)

#This azores map object can also be saved as an html file
azores = folium.folium.Map(location = (38, -27),
                    zoom_start = 6).save("output.html")