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
        .sidebar {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;  /* Optional: To make text more visible on the image */
        }}
        .sidebar-title {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .sidebar select {{
            cursor: pointer;
        }}
        .sidebar-button {{
            cursor: pointer;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL gambar dari GitHub (replace this with your own image URL)
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

# Fungsi untuk menampilkan tabs di sidebar dengan selectbox
def display_sidebar_tabs():
    st.sidebar.markdown('<div class="sidebar-title">Menu</div>', unsafe_allow_html=True)
    tabs = list(Tabs.keys())
    
    # Using a selectbox for tab selection
    selected_tab = st.sidebar.selectbox("Choose a tab", tabs, key="selected_tab")

    return selected_tab

# Display tabs di sidebar dengan selectbox
selected_tab = display_sidebar_tabs()

# Kondisi Call App Function
if selected_tab in Tabs:
    Tabs[selected_tab].app(df, x, y)
