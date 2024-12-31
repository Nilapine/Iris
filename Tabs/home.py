import streamlit as st
from web_functions import load_data

def app(df, x, y):
    # Judul Halaman Aplikasi
    st.title("Aplikasi Prediksi Jenis Tanaman Iris")

    # Informasi Tentang Bunga Iris
    st.write("""
    Bunga iris adalah salah satu jenis tanaman berbunga yang terkenal karena keindahan bentuk dan warna bunganya. 
    Nama 'iris' berasal dari bahasa Yunani yang berarti 'pelangi', sesuai dengan ragam warna bunga ini. 
    Tiga jenis iris yang paling umum adalah Iris-setosa, Iris-versicolor, dan Iris-virginica. 
    Setiap spesies memiliki karakteristik unik yang membuatnya menarik untuk dipelajari.
    """)

    # Menampilkan Data
    df.drop('Id', axis=1, inplace=True)
    st.write(df)

    # Menambahkan Gambar Iris Berjejeran
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_setosa2.jpg", caption="Iris Setosa", width=150)
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/a/a7/Iris_versicolor_3.jpg", caption="Iris Versicolor", width=150)
    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg", caption="Iris Virginica", width=150)
