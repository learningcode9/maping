import folium
import pandas
import json
import os


state_geo ='geo_json.json'
state_data = pandas.read_csv('states_homeless.csv')

#Let Folium determine the scale

m = folium.Map(location=[48, -102], zoom_start=3)


choropleth=folium.Choropleth(
    geo_data=state_geo,
    name='homeless',
    data=state_data,
    columns=['State','Homeless'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    hoverinfo='hello',
    legend_name='Homeless (%)',
    
    highlight=True
).add_to(m)
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(fields=['name','Homeless %'],
    aliases=['State','Homeless %'])
)

m.save("place1.html")
folium.LayerControl().add_to(m)