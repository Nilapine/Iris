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

# Header with logo and menu
title_container = st.container()

# Add CSS for styling
st.markdown("""
    <style>
        /* Container for logo and menu aligned horizontally */
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1px;  /* Space below the header */
        }
        .header-logo {
            margin-right: 1px;  /* Space between logo and menu */
        }
        div[role='tablist'] {
            display: flex;
            justify-content: center;
        }
        div[role='tablist'] > div {
            margin-right: 50px;  /* Space between individual tabs */
        }
    </style>
""", unsafe_allow_html=True)

# Create a container for logo and tabs in one header
with title_container:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    # Add the tabs below the image, in the same header section
    selected_tab = st.tabs(list(Tabs.keys()))
    st.markdown('</div>', unsafe_allow_html=True)
    df,x,y = load_data()

# Kondisi Call App Function
if selected_tab in ["Prediction", "Visualisation"]:
    Tabs[selected_tab].app(df, x, y)
else:
    Tabs[selected_tab].app(df, x, y)  # type: ignore
