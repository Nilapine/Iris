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

    # Menambahkan Gambar Iris Berjejeran
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.squarespace-cdn.com/content/v1/61eeea89d60f57793d9e114b/1706854176756-Y4XKV9Q0OQ5F2C0ICPDI/iris%2Bsetosa%2B%25282%2529.jpg?format=1000w.jpg", caption="Iris Setosa", width=150)
    with col2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAhHAQgQSBvRdWjZS3rp0wVvLum8zgHC0djx-rGJupnYYyKaGkMvGoQNTa3GV4FjBe8d0&usqp=CAU", caption="Iris Versicolor", width=150)
    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg", caption="Iris Virginica", width=150)

    # Menampilkan Data
    st.write("""
    Dataset yang digunakan dalam prediksi bunga iris :
    """)
    df.drop('Id', axis=1, inplace=True)
    st.write(df)

    
