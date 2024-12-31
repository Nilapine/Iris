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
        .stRadio > div {{
            text-align: center;  /* Menyelaraskan radio button di tengah */
        }}
        .stRadio label {{
            display: inline-block;
            margin: 0 10px;  /* Jarak antar tab */
            cursor: pointer;
            padding: 10px 20px;
            background-color: #f4f4f4;
            border-radius: 5px;
            border: 2px solid transparent;
            transition: background-color 0.3s;
        }}
        .stRadio label:hover {{
            background-color: rgba(0, 0, 0, 0.1);
        }}
        .stRadio input[type="radio"]:checked + label {{
            background-color: #4CAF50;
            color: white;
            border-color: #4CAF50;
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

# Fungsi untuk menampilkan tabs horizontal
def display_tabs():
    tabs = list(Tabs.keys())
    selected_tab = st.radio(
        "",  # Kosongkan label agar tidak ada teks di depan radio
        tabs, 
        index=0, 
        horizontal=True, 
        key="tab_selector",
        format_func=lambda x: x  # Menampilkan hanya nama tab, tanpa ikon atau deskripsi lainnya
    )
    
    return selected_tab

# Display tabs horizontally at the top
selected_tab = display_tabs()

# Kondisi Call App Function
if selected_tab in ["Prediction", "Visualisation"]:
    Tabs[selected_tab].app(df, x, y)
else:
    Tabs[selected_tab].app(df, x, y)  # type: ignore
