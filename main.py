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
            justify-content: center;
            margin-top: 20px;
            gap: 20px;
        }}
        .tab {{
            padding: 10px 20px;
            border-radius: 5px;
            background-color: #f0f0f0;
            cursor: pointer;
            text-align: center;
            font-weight: bold;
            transition: background-color 0.3s;
        }}
        .tab:hover {{
            background-color: #dcdcdc;
        }}
        .tab-selected {{
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

# Load Dataset
df, x, y = load_data()

# Fungsi untuk menampilkan tabs horizontal dengan navigasi interaktif tanpa tombol
def display_tabs_with_columns():
    tabs = list(Tabs.keys())
    selected_tab = st.session_state.get("selected_tab", tabs[0])  # Default tab adalah yang pertama

    # Kontainer untuk tab
    st.markdown("<div class='tab-container'>", unsafe_allow_html=True)
    for tab_name in tabs:
        css_class = "tab tab-selected" if tab_name == selected_tab else "tab"
        tab_html = f"<div class='{css_class}' onclick="window.location.href='#{predict}'">{visualise}</div>"
        st.markdown(tab_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Memperbarui tab yang dipilih berdasarkan hash URL
    selected_tab = st.experimental_get_query_params().get("tab", [tabs[0]])[0]
    st.experimental_set_query_params(tab=selected_tab)

    return selected_tab

# Tampilkan tabs horizontal di atas
selected_tab = display_tabs_with_columns()

# Kondisi Call App Function
if selected_tab in ["Prediction", "Visualisation"]:
    Tabs[selected_tab].app(df, x, y)
else:
    Tabs[selected_tab].app(df, x, y)  # type: ignore
