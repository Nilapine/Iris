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
        .tab-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }}
        .tab {{
            padding: 10px 20px;
            background-color: #f4f4f4;
            border: 1px solid #ccc;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
            transition: background-color 0.3s, color 0.3s;
        }}
        .tab:hover {{
            background-color: #ddd;
        }}
        .tab-selected {{
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

# Fungsi untuk menampilkan tabs dengan gaya kotakan
def display_tabs():
    tabs = list(Tabs.keys())
    selected_tab = st.session_state.get("selected_tab", tabs[0])

    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    for tab in tabs:
        if tab == selected_tab:
            button_class = "tab tab-selected"
        else:
            button_class = "tab"

        if st.button(tab, key=f"tab_{tab}"):
            st.session_state.selected_tab = tab
            selected_tab = tab

        st.markdown(f'<div class="{button_class}">{tab}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    return selected_tab

# Display tabs di area utama dengan gaya kotakan
selected_tab = display_tabs()

# Kondisi Call App Function
if selected_tab in Tabs:
    Tabs[selected_tab].app(df, x, y)
