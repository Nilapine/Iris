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
        .tabs-container {{
            display: flex;
            justify-content: center;
            gap: 20px;
            padding: 20px;
        }}
        .stButton {{
            font-size: 18px;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
        }}
        .stButton:hover {{
            background-color: rgba(0, 0, 0, 0.1);
        }}
        .stButtonSelected {{
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

# Fungsi untuk menampilkan menu tabs di tengah
def display_tabs():
    tabs = list(Tabs.keys())
    selected_tab = None

    # Create a button for each tab
    for tab in tabs:
        if st.button(tab, key=tab):
            selected_tab = tab

    return selected_tab

# Display tabs at the top and center them
selected_tab = display_tabs()

# Kondisi Call App Function
if selected_tab:
    Tabs[selected_tab].app(df, x, y)
else:
    Tabs["Home"].app(df, x, y)  # Default to Home tab
