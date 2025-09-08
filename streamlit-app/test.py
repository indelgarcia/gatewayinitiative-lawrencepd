# test.py — minimal sandbox for the unemployment layer

import os
import json
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components

st.set_page_config(page_title="Test Unemployment Layer", layout="wide")
st.title("Test Map, Unemployment Layer")

# ===========================================
# Cached loaders
# ===========================================
@st.cache_data
def load_checkpoint11():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "checkpoint11_combined_data.csv")
    return pd.read_csv(path)

@st.cache_data
def load_unemployment_geojson():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "boundaries", "unemployment_boundary.geojson")
    with open(path, "r") as f:
        return json.load(f)

# ===========================================
# Tabs
# ===========================================
tab_map, tab_two = st.tabs(["Map", "Tab 2"])

with tab_map:
    # Sidebar lives only for Map tab
    with st.sidebar:
        st.header("Controls")
        unemployment_enabled = st.toggle("Unemployment data", value=False)

    # Try reading checkpoint 11 so you can see it is wired
    try:
        df = load_checkpoint11()
        st.caption(f"Checkpoint 11 loaded with {len(df):,} rows")
    except Exception as e:
        st.error(f"Could not load checkpoint11_combined_data.csv. {e}")

    # Map
    m = folium.Map(
        location=[42.70, -71.155],
        zoom_start=14,
        control_scale=True,
        tiles="CartoDB positron",
    )

    # Small CSS pad like your main app
    m.get_root().html.add_child(folium.Element("""
    <style>
    .leaflet-bottom.leaflet-right {
        margin-bottom: 10px;
        margin-right: 10px;
    }
    </style>
    """))

    # Unemployment layer renderer
    if unemployment_enabled:
        try:
            unemployment_geo = load_unemployment_geojson()

            unemployment_df = pd.DataFrame([
                {
                    "tract": feat["properties"].get("tract"),
                    "Estimate": feat["properties"].get("Estimate"),
                }
                for feat in unemployment_geo.get("features", [])
                if feat.get("properties")
                and feat["properties"].get("tract")
                and feat["properties"].get("Estimate") is not None
            ])

            if unemployment_df.empty:
                st.warning("Unemployment GeoJSON has no features with tract and Estimate.")
            else:
                est = unemployment_df["Estimate"].astype(float)
                max_est = float(est.max())
                bins = [0, 5, 8, 10, 12, 16, max(max_est, 16) + 0.001]

                folium.Choropleth(
                    geo_data=unemployment_geo,
                    name="Unemployment Rate",
                    data=unemployment_df,
                    columns=["tract", "Estimate"],
                    key_on="feature.properties.tract",
                    fill_color="Blues",
                    fill_opacity=0.7,
                    line_opacity=0.2,
                    legend_name="Unemployment Rate (%)",
                    bins=bins,
                    nan_fill_opacity=0.0,
                ).add_to(m)

                unemployment_legend_html = """
                <div style="
                    position: fixed;
                    bottom: 40px;
                    left: 40px;
                    z-index:9999;
                    background-color: white;
                    padding: 10px;
                    border:2px solid gray;
                    border-radius: 5px;
                    font-size: 14px;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
                ">
                    <strong style="color: black;">Unemployment Rate (%)</strong><br>
                    <span style="color: black;">
                        <i style="background:#f7fbff;width:20px;height:10px;display:inline-block;"></i> 0–5%<br>
                        <i style="background:#deebf7;width:20px;height:10px;display:inline-block;"></i> 5–8%<br>
                        <i style="background:#c6dbef;width:20px;height:10px;display:inline-block;"></i> 8–10%<br>
                        <i style="background:#9ecae1;width:20px;height:10px;display:inline-block;"></i> 10–12%<br>
                        <i style="background:#6baed6;width:20px;height:10px;display:inline-block;"></i> 12–16%<br>
                        <i style="background:#2171b5;width:20px;height:10px;display:inline-block;"></i> 16%+
                    </span>
                </div>
                """
                m.get_root().html.add_child(folium.Element(unemployment_legend_html))
        except FileNotFoundError:
            st.error("Could not find boundaries/unemployment_boundary.geojson. Make sure the file exists.")
        except Exception as e:
            st.error(f"There was an error while drawing the unemployment layer. {e}")

    folium.LayerControl().add_to(m)
    st_folium(m, width="100%", height=750)

with tab_two:
    st.subheader("Tab 2")
    st.write("The side bar should automatically be closed here")

# ===========================================
# JS to hide sidebar only when Tab 2 is active
# ===========================================
components.html(
    """
<script>
(function() {
  const HIDE_STYLE_ID = "hideSidebarStyleForTab2";
  const css = `
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    header [data-testid="baseButton-headerNoPadding"] { display: none !important; }
  `;

  function setHidden(hidden) {
    const head = window.parent.document.head;
    let style = window.parent.document.getElementById(HIDE_STYLE_ID);
    if (hidden) {
      if (!style) {
        style = window.parent.document.createElement("style");
        style.id = HIDE_STYLE_ID;
        style.textContent = css;
        head.appendChild(style);
      }
    } else {
      if (style) style.remove();
    }
  }

  function activeTabLabel() {
    // Find all tab buttons, then the one with aria-selected true
    const doc = window.parent.document;
    const tabs = Array.from(doc.querySelectorAll('button[role="tab"]'));
    const active = tabs.find(btn => btn.getAttribute("aria-selected") === "true");
    return active ? active.innerText.trim() : "";
  }

  function applyByActiveTab() {
    const label = activeTabLabel();
    // Hide on "Tab 2", show otherwise
    setHidden(label === "Tab 2");
  }

  // Initial apply
  applyByActiveTab();

  // Observe tab header for changes
  const doc = window.parent.document;
  const tablist = doc.querySelector('[role="tablist"]');
  if (tablist) {
    tablist.addEventListener("click", () => setTimeout(applyByActiveTab, 0), { passive: true });
  }

  // Also watch for attribute changes like aria-selected flips
  const mo = new MutationObserver(() => applyByActiveTab());
  if (tablist) mo.observe(tablist, { attributes: true, subtree: true, attributeFilter: ["aria-selected", "class"] });

  // Re-apply on hash changes or resize just in case
  window.addEventListener("hashchange", applyByActiveTab);
  window.addEventListener("resize", applyByActiveTab);
})();
</script>
    """,
    height=0,
)
