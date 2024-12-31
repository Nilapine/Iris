import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise

# Fungsi untuk menambahkan latar belakang gambar
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL gambar dari GitHub
background_image_url = "https://github.com/Nilapine/Iris/blob/main/background.png?raw=true"

# Set latar belakang
set_background_image(background_image_url)

# Membuat Tabs
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise,
}

# Load Dataset
df, x, y = load_data()

# Fungsi untuk menampilkan tabs di sidebar
def display_sidebar_tabs():
    st.sidebar.title("Navigation")
    tabs = list(Tabs.keys())
    selected_tab = st.sidebar.radio("Go to:", tabs, index=0, key="tab_selector")
    return selected_tab

# Display tabs di sidebar
selected_tab = display_sidebar_tabs()

# Kondisi Call App Function
if selected_tab in Tabs:
    Tabs[selected_tab].app(df, x, y)
