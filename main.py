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
        .stTabs {{
            display: flex;
            justify-content: center;  /* Menyelaraskan tab di tengah */
            padding: 10px;
            border-bottom: 2px solid #ddd;  /* Menambahkan garis bawah */
        }}
        .stTab {{
            padding: 10px 20px;
            cursor: pointer;
            border: 2px solid transparent;
            border-radius: 5px;
            transition: background-color 0.3s;
            background-color: #f4f4f4;  /* Warna latar belakang tab */
        }}
        .stTab:hover {{
            background-color: rgba(0, 0, 0, 0.1);
        }}
        .stTabSelected {{
            background-color: #4CAF50;
            color: white;
            border-color: #4CAF50;  /* Menambahkan border saat tab terpilih */
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
        " ", 
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
