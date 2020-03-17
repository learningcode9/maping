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
fgp = folium.FeatureGroup(name = "Homeless opulation")

fgp.add_child(folium.GeoJson(data=open('geo_json.json','r',encoding='utf-8-sig').read(),
style_function=lambda  x:{"fillColor":'blue' if x['properties']['Homeless %']<1.0 
else 'orange' if 1.0 <= x['properties']['Homeless %']<3.5 else 'red'},

tooltip=folium.GeoJsonTooltip(fields=['Homeless %'])))

m.add_child(fgp)

m.add_child(fg)
m.add_child(folium.LayerControl())
m.save("place.html")





