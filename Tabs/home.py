import streamlit as st
from web_functions import load_data

def app(df,x,y):
    # Judul Halaman Aplikasi
    st.title("Aplikasi Prediksi Jenis Tanaman Iris")
    df.drop('Id',axis=1)
    st.write(df)
    
