# im terminal eingeben zum starten -> streamlit run app.py
import streamlit as st
import streamlit.components.v1 as components

# Title of the app
st.title("SocialWifi Map")

# Read the HTML file
with open("mymapSocialWifi.html", 'r', encoding='utf-8') as html_file:
    map_html = html_file.read()

# Embed the HTML file in the Streamlit app
components.html(map_html, height=700, width=1000)

# Custom CSS to adjust text width, size, and alignment
st.markdown("""
    <style>
    .custom-text {
        max-width: 1300px;
        margin: auto;
        font-size: 30px;  /* Verkleinert die Textgröße */
        text-align: left;  /* Kein Blocksatz, linksbündig */
        line-height: 2;  /* Erhöht den Zeilenabstand für bessere Lesbarkeit */
    }
    </style>
    """, unsafe_allow_html=True)

# Add your text in a div with the custom CSS class
st.markdown('<div class="custom-text"><p>In einer vernetzten Welt ist eine ausreichende Breitbandverfügbarkeit essentiell, um die eigenen Potenziale (z.B. durch Online-Schulungen oder Remote-Working) ausschöpfen zu können.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="custom-text"><p>In einer Heatmap zeigen wir auf, in welchen Kreisen Deutschlands Risikogebiete bestehen, in denen der Infrastrukturausbau durch ein geringes verfügbares Einkommen der Einwohner unterstützt werden sollte. Diese sind auf einen Blick durch eine Einfärbung der Karte nach verfügbarem Einkommen und/oder Breitbandverfügbarkeit per Mausklick ersichtlich. Zusätzlich können verschiedene Kreise und Städte per Suchfunktion gesucht werden. Durch unsere Karte ist eine schnelle Auskunft und Unterstützung bei der gezielten Ausrichtung von Bemühungen gegen soziale Ungleichheit möglich.</p></div>', unsafe_allow_html=True)
