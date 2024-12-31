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
        .stSidebar {{
            position: relative;
            top: 0;
            left: 0;
            width: 200px;
            height: 100%;
        }}
        .stTabs {{
            display: flex;
            flex-direction: column;  /* Menyusun tab secara vertikal seperti sidebar */
            padding: 10px;
        }}
        .stTab {{
            padding: 10px 20px;
            cursor: pointer;
            border: 2px solid transparent;
            border-radius: 5px;
            transition: background-color 0.3s;
        }}
        .stTab:hover {{
            background-color: rgba(0, 0, 0, 0.1);
        }}
        .stTabSelected {{
            background-color: #4CAF50;
            color: white;
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

# Membuat Sidebar
st.sidebar.title("Navigasi")

# Load Dataset
df, x, y = load_data()

# Fungsi untuk menampilkan tabs di sidebar
def display_tabs():
    tabs = list(Tabs.keys())
    selected_tab = st.sidebar.radio("Pilih Tab", tabs, index=0, key="tab_selector")
    
    return selected_tab

# Display tabs in sidebar
selected_tab = display_tabs()

# Kondisi Call App Function
if selected_tab in ["Prediction", "Visualisation"]:
    Tabs[selected_tab].app(df, x, y)
else:
    Tabs[selected_tab].app(df, x, y)  # type: ignore
