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

# Membuat Menu Tab Horizontal
st.markdown(
    """
    <style>
    .tabs-container {{
        display: flex;
        justify-content: space-around;
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 5px;
    }}
    .tab {{
        font-size: 16px;
        font-weight: bold;
        color: #007bff;
        cursor: pointer;
        padding: 10px 20px;
        text-decoration: none;
        border: 1px solid #ddd;
        border-radius: 5px;
    }}
    .tab:hover {{
        background-color: #007bff;
        color: white;
    }}
    .active-tab {{
        background-color: #007bff;
        color: white;
    }}
    </style>
    <div class="tabs-container">
        <a href="?page=Home" class="tab {active_home}">Home</a>
        <a href="?page=Prediction" class="tab {active_prediction}">Prediction</a>
        <a href="?page=Visualisation" class="tab {active_visualisation}">Visualisation</a>
    </div>
    """.format(
        active_home="active-tab" if st.experimental_get_query_params().get("page", ["Home"])[0] == "Home" else "",
        active_prediction="active-tab" if st.experimental_get_query_params().get("page", [""])[0] == "Prediction" else "",
        active_visualisation="active-tab" if st.experimental_get_query_params().get("page", [""])[0] == "Visualisation" else ""
    ),
    unsafe_allow_html=True,
)

# Menangkap Halaman yang Dipilih
selected_page = st.experimental_get_query_params().get("page", ["Home"])[0]

# Load Dataset
df, x, y = load_data()

# Memanggil Fungsi Berdasarkan Tab yang Dipilih
Tabs[selected_page].app(df, x, y)  # type: ignore
