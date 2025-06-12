import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="📊 Tableau Dashboard", layout="wide")

st.title("📊 Embedded Tableau Dashboard")

html_code = """
<div style="transform: scale(0.7); transform-origin: top left; width: 125%; height: 1100px;">
    <div class='tableauPlaceholder' id='viz1749758561977' style='position: relative'>
        <noscript>
            <a href='#'>
                <img alt='Combined ' src='https://public.tableau.com/static/images/La/LawrencePDPublicData/Dashboard4/1_rss.png' style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='LawrencePDPublicData/Dashboard4' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/La/LawrencePDPublicData/Dashboard4/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1749758561977');
        var vizElement = divElement.getElementsByTagName('object')[0];
        vizElement.style.width='1000px';
        vizElement.style.height='1100px';
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
</div>
"""

components.html(html_code, height=950, scrolling=True)
