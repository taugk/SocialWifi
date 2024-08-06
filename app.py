
# im terminal eingeben zum starten -> streamlit run app.py
import streamlit as st


#iframe
import streamlit.components.v1 as components

# Title of the app
st.title("SocialWifi Map")

# Read the HTML file
with open("mymapSocialWifi.html", 'r', encoding='utf-8') as html_file:
    map_html = html_file.read()
    
# Embed the HTML file in the Streamlit app
components.html(map_html, height = 700, width = 1000)

st.write("Das ist unser cooles Projekt und hier sind einige Infos dazu.")
