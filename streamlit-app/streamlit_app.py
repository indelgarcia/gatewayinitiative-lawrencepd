# streamlit_app.py
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster, HeatMap
from streamlit_folium import st_folium
from pathlib import Path
from folium.plugins import MarkerCluster
import os
import json


st.set_page_config(page_title="Police Incident Map", layout="wide")

st.title("Lawrence Police Daily Logs")
# -----------------------------
# 📍 LOAD LAWRENCE BOUNDARY 
# -----------------------------
@st.cache_data
def load_lawrence_boundary():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "lawrence_boundary.geojson")
    with open(file_path, "r") as f:
        lawrence_geojson = json.load(f)
        return lawrence_geojson
lawrence_geojson = load_lawrence_boundary()
# -----------------------------
# 📊 LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "checkpoint7_serious_crimes_subset.csv")
    df = pd.read_csv(file_path)
    data = df[['Latitude', 'Longitude', 'category', 'crime_severity', 'Incident #', 'Date']].dropna()
    data['Date'] = pd.to_datetime(data['Date'])
    data['year'] = data['Date'].dt.year
    return data

data = load_data()


incident_types = ["All"] + sorted(data['category'].dropna().unique())
# incident_types = data['category'].unique()
# -----------------------------
# 🧰 SIDEBAR FILTERS
# -----------------------------
with st.sidebar:
    st.header("🔍 Filters")
    # selected_year = st.selectbox("📅 Select Year", sorted(data['year'].unique()))
    selected_year = st.multiselect(
    "📅 Select Year(s)",
    sorted(data['year'].unique()),
    default=sorted(data['year'].unique())  # show all years by default
    )
    st.markdown("---")
    st.subheader("📌 Incident Categories")
    selected_incidents = st.multiselect("Choose incidents to view:", incident_types, default="VIOLENT_AND_WEAPON_OFFENSES")
    serious_crime_filter = st.selectbox(
    "🚨 Filter by Serious Crime",
    ["All", "Serious Only", "Non-Serious Only"])
    heatmap_enabled = st.sidebar.checkbox("Show Heatmap", value=False)


# -----------------------------
# 🧹 FILTER DATA
# -----------------------------
# filtered_data = data[(data['year'].isin(selected_year)) & (data['category'].isin(selected_incidents))]
if "All" in selected_incidents:
    filtered_data = data[data['year'].isin(selected_year)]
else:
    filtered_data = data[(data['category'].isin(selected_incidents)) & 
                         (data['year'].isin(selected_year))]


filtered_data = filtered_data.dropna(subset=['Latitude', 'Longitude'])
if serious_crime_filter == "Serious Only":
    filtered_data = filtered_data[filtered_data['crime_severity'] == 'Serious']
elif serious_crime_filter == "Non-Serious Only":
    filtered_data = filtered_data[filtered_data['crime_severity'] == 'Not-Serious']
else:
    filtered_data = filtered_data

st.markdown(f"### 🗓️ {selected_year} | {len(filtered_data)} incident(s) shown")

# -----------------------------
# 🗺️ CREATE MAP
# -----------------------------
if not filtered_data.empty:
    m = folium.Map(location=[42.707, -71.163], zoom_start=14)#, tiles="CartoDB positron")
    
    # Add the boundary to the map
    folium.GeoJson(
        lawrence_geojson,
        name="Lawrence Border",
        style_function=lambda x: {
        'color': 'red',
        'weight': 2,
        'fillOpacity': 0
    }).add_to(m)
    if heatmap_enabled:
        #  Add Heatmap
        heat_data = filtered_data[['Latitude', 'Longitude']].dropna()
        heat_data = heat_data[(heat_data['Latitude'].apply(lambda x: isinstance(x, (float, int)))) &
                            (heat_data['Longitude'].apply(lambda x: isinstance(x, (float, int))))]

        heat_list = heat_data[['Latitude', 'Longitude']].values.tolist()

        if heat_list:
            HeatMap(heat_list).add_to(m)
    else:
    #     style_function=lambda x: {
    #         "fillColor": "#00000000",  # Transparent fill
    #         "color": "red",            # Red outline
    #         "weight": 3,
    #         "dashArray": "5, 5"
    #     }
    # ).add_to(m)
        marker_cluster = MarkerCluster().add_to(m)
        for _, row in filtered_data.iterrows():
            popup_text = f"{row['Date']}<br>{row['category']}"
            folium.CircleMarker(
                location=(row['Latitude'], row['Longitude']),
                radius=8,
                color="crimson",
                fill=True,
                fill_opacity=0.7,
                popup=popup_text
            ).add_to(marker_cluster)
        

    # for _, row in filtered_data.iterrows():
    #     folium.Marker(
    #         location=[row['Latitude'], row['Longitude']],
    #         popup=f"{row['category']}<br>{row['Date']}",
    #         icon=folium.Icon(color='blue')
    #     ).add_to(marker_cluster)

    st_data = st_folium(m, width=2000, height=800)

else:
    st.warning("No data to display on the map for the selected filters.")

