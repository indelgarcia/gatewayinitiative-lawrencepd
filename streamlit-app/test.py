import overpy
import folium
import streamlit as st

# Initialize Overpass API
api = overpy.Overpass()

# Define bounding box for Lawrence, MA (approximate bbox)
# (south latitude, west longitude, north latitude, east longitude)
lawrence_bbox = (42.6901, -71.1767, 42.7276, -71.1385)

# Overpass QL query to get grocery stores, parks, liquor stores within bbox
query = f"""
(
  node["shop"="supermarket"]({lawrence_bbox[0]},{lawrence_bbox},{lawrence_bbox},{lawrence_bbox});
  node["shop"="convenience"]({lawrence_bbox},{lawrence_bbox},{lawrence_bbox},{lawrence_bbox});
  node["shop"="greengrocer"]({lawrence_bbox},{lawrence_bbox},{lawrence_bbox},{lawrence_bbox});
  node["shop"="酒屋"]({lawrence_bbox},{lawrence_bbox},{lawrence_bbox},{lawrence_bbox});  # Japanese for liquor store
  node["shop"="liquor"]({lawrence_bbox},{lawrence_bbox},{lawrence_bbox},{lawrence_bbox});
  node["leisure"="park"]({lawrence_bbox},{lawrence_bbox},{lawrence_bbox},{lawrence_bbox});
  way["leisure"="park"]({lawrence_bbox},{lawrence_bbox},{lawrence_bbox},{lawrence_bbox});
);
out center;
"""

# Run the query
result = api.query(query)

# Create Folium Map
m = folium.Map(location=[42.707, -71.155], zoom_start=14)

# Add grocery stores, convenience stores, greengrocers as green markers
for node in result.nodes:
    tags = node.tags
    lat = node.lat
    lon = node.lon

    # Determine type for popup and icon color
    if tags.get("shop") in ["supermarket", "convenience", "greengrocer"]:
        folium.Marker(
            location=[lat, lon],
            popup=f"{tags.get('name', 'Grocery Store')} (Grocery)",
            icon=folium.Icon(color="green", icon="shopping-cart", prefix='fa')
        ).add_to(m)

    # Liquor store
    elif tags.get("shop") in ["liquor", "酒屋"]:
        folium.Marker(
            location=[lat, lon],
            popup=f"{tags.get('name', 'Liquor Store')} (Liquor Store)",
            icon=folium.Icon(color="blue", icon="beer", prefix='fa')
        ).add_to(m)

    # Park
    elif tags.get("leisure") == "park":
        folium.Marker(
            location=[lat, lon],
            popup=f"{tags.get('name', 'Park')} (Park)",
            icon=folium.Icon(color="darkgreen", icon="tree", prefix='fa')
        ).add_to(m)

# Plot ways (parks as polygons) with their center point
for way in result.ways:
    if way.tags.get("leisure") == "park":
        lat = way.center_lat
        lon = way.center_lon
        folium.Marker(
            location=[lat, lon],
            popup=f"{way.tags.get('name', 'Park')} (Park Area)",
            icon=folium.Icon(color="darkgreen", icon="tree", prefix='fa')
        ).add_to(m)

# Show map in Streamlit
st.title("OSM Points of Interest in Lawrence, MA")
st_folium = st.components.v1.html

# Use the st_folium component from streamlit-folium
from streamlit_folium import st_folium
st_data = st_folium(m, width="100%", height=600)
