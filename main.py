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

# Fungsi untuk menampilkan tabs horizontal dengan kontenerisasi
def display_tabs_with_columns():
    tabs = list(Tabs.keys())
    selected_tab = None

    # Kontainer untuk tab
    container = st.container()
    with container:
        cols = st.columns(5)  # Membagi area menjadi 5 kolom

        for i, tab_name in enumerate(tabs):
            if i < len(cols):
                if cols[i].button(tab_name):
                    selected_tab = tab_name

    # Mengatur tab pertama sebagai default jika belum dipilih
    if not selected_tab:
        selected_tab = tabs[0]

    return selected_tab

# Tampilkan tabs horizontal di atas
selected_tab = display_tabs_with_columns()

# Kondisi Call App Function
if selected_tab in ["Prediction", "Visualisation"]:
    Tabs[selected_tab].app(df, x, y)
else:
    Tabs[selected_tab].app(df, x, y)  # type: ignore
