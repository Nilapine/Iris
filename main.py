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
            gap: 40px;
            padding: 20px;
            font-size: 24px;
            font-weight: bold;
        }}
        .tab {{
            cursor: pointer;
            transition: color 0.3s;
        }}
        .tab:hover {{
            color: #4CAF50;
        }}
        .tab-selected {{
            color: #4CAF50;
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

# Fungsi untuk menampilkan tabs horizontal di bagian atas
def display_tabs():
    tabs = list(Tabs.keys())
    selected_tab = st.session_state.get('selected_tab', "Home")  # Default to "Home"

    # Display tabs as text, and change the selected tab when clicked
    tab_html = ""
    for tab in tabs:
        if tab == selected_tab:
            tab_html += f'<span class="tab tab-selected" onclick="window.parent.postMessage({{"tab":"{tab}"}}, "*")">{tab}</span>'
        else:
            tab_html += f'<span class="tab" onclick="window.parent.postMessage({{"tab":"{tab}"}}, "*")">{tab}</span>'

    st.markdown(f'<div class="tabs-container">{tab_html}</div>', unsafe_allow_html=True)

    return selected_tab

# Display tabs at the top and center them
selected_tab = display_tabs()

# Kondisi Call App Function
if selected_tab in Tabs:
    Tabs[selected_tab].app(df, x, y)
