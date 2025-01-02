import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
import streamlit as st
import numpy as np
import pandas as pd

from web_functions import train_model_DT, train_model_KNN, train_model_NBC, load_data

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.title("Visualisasi Prediksi Tanaman Iris")

    # Display the pairplot
    st.title("Pairplot")
    pairplot_fig = sns.pairplot(df, hue="Species").fig
    st.pyplot(pairplot_fig)

    # Penjelasan menggunakan laci
    with st.expander("Dataset Iris"):
        st.markdown("""
        Dataset ini terdiri dari tiga spesies bunga Iris—*Iris-setosa* (biru), *Iris-versicolor* (oranye), dan *Iris-virginica* (hijau)—yang diklasifikasikan berdasarkan empat fitur:
        - **SepalLengthCm**: Panjang kelopak bunga (sepal) dalam cm.
        - **SepalWidthCm**: Lebar kelopak bunga dalam cm.
        - **PetalLengthCm**: Panjang mahkota bunga (petal) dalam cm.
        - **PetalWidthCm**: Lebar mahkota bunga dalam cm.
        - **Id**: Indeks untuk identifikasi.
        """)

    with st.expander("Distribusi diagonal"):
        st.markdown("""
        Di sepanjang diagonal, terlihat distribusi (plot densitas atau histogram) dari masing-masing fitur secara individu. Warna-warna pada distribusi ini mewakili spesies yang berbeda.
        """)

    with st.expander("Scatter plot non-diagonal"):
        st.markdown("""
        Di bagian lain dari pair plot ini, terlihat plot pencar (scatter plot) yang menunjukkan hubungan antara dua fitur. Setiap titik pada scatter plot mewakili satu contoh dari dataset, dengan warnanya mencerminkan spesiesnya. 
        """)

    with st.expander("Klasifikasi visual"):
        st.markdown("""
        Gambar ini memberikan indikasi seberapa mudah atau sulit spesies bunga dapat diklasifikasikan berdasarkan fitur tertentu. Beberapa pasangan fitur memperlihatkan pemisahan yang lebih jelas antar spesies, sedangkan beberapa pasangan lainnya menunjukkan tumpang tindih yang lebih besar.
        """)
