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
        .sidebar-title {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .sidebar-button {{
            display: block;
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #f4f4f4;
            border: none;
            border-radius: 5px;
            text-align: left;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
        }}
        .sidebar-button:hover {{
            background-color: #ddd;
        }}
        .sidebar-button-selected {{
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
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

# Fungsi untuk menampilkan tabs di sidebar dengan tombol untuk setiap tab
def display_sidebar_tabs():
    st.sidebar.markdown('<div class="sidebar-title">Menu</div>', unsafe_allow_html=True)
    tabs = list(Tabs.keys())
    selected_tab = st.session_state.get("selected_tab", tabs[0])

    for tab in tabs:
        if tab == selected_tab:
            button_class = "sidebar-button sidebar-button-selected"
        else:
            button_class = "sidebar-button"

        if st.sidebar.button(tab, key=f"tab_{tab}"):
            st.session_state.selected_tab = tab
            selected_tab = tab

        st.sidebar.markdown(f'<button class="{button_class}">{tab}</button>', unsafe_allow_html=True)

    return selected_tab

# Display tabs di sidebar sebagai tombol
selected_tab = display_sidebar_tabs()

# Kondisi Call App Function
if selected_tab in Tabs:
    Tabs[selected_tab].app(df, x, y)
