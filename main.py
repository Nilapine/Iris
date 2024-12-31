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
        }}
        .stTab {{
            padding: 10px 20px;
            cursor: pointer;
            border: 2px solid transparent;
            border-radius: 5px;
            transition: background-color 0.3s;
            margin: 0 10px;
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

# Fungsi untuk menampilkan tabs horizontal dan berada di tengah
def display_tabs():
    tabs = list(Tabs.keys())
    tab_html = f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    """
    
    for tab in tabs:
        tab_html += f"""
        <div style="padding: 10px 20px; cursor: pointer; border: 2px solid transparent; border-radius: 5px; margin: 0 10px;" 
             onclick="window.location.href = '/{tab.lower()}'">
            {tab}
        </div>
        """
        
    tab_html += "</div>"

    st.markdown(tab_html, unsafe_allow_html=True)

# Display tabs horizontally at the top
display_tabs()

# Logika pemanggilan fungsi aplikasi berdasarkan tab yang dipilih
selected_tab = st.session_state.get("selected_tab", "Home")

if selected_tab in ["Prediction", "Visualisation"]:
    Tabs[selected_tab].app(df, x, y)
else:
    Tabs[selected_tab].app(df, x, y)  # type: ignore
