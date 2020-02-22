import folium
import pandas

data=pandas.read_csv('techcompanies.txt')
lat=list(data["LAT"])
long=list(data["LONG"])
name=list(data["NAME"])



m=folium.Map(location=[37.37,-122.04],zoom_start=6,tiles="Stamen Terrain")
#print(type(m))
fg=folium.FeatureGroup(name="My Map")

for lt,ln,na in zip(lat,long,name):

    fg.add_child(folium.Marker(location=[lt,ln],popup=na,tooltip=na,icon=folium.Icon(color='green')))
m.add_child(fg)
m.save("techmap.html")




