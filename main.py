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

# Membuat Menu Tab Manual
st.markdown(
    """
    <style>
    div.stButton > button {
        margin: 0 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 1, 1])

# Pilihan Tab
with col1:
    if st.button("Home"):
        selected_page = "Home"
with col2:
    if st.button("Prediction"):
        selected_page = "Prediction"
with col3:
    if st.button("Visualisation"):
        selected_page = "Visualisation"

# Load Dataset
df, x, y = load_data()

# Memanggil Fungsi Berdasarkan Tab yang Dipilih
Tabs[selected_page].app(df, x, y)  # type: ignore
