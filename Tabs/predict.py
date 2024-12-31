import streamlit as st

from web_functions import predict_DT,predict_KNN,predict_NBC

def app(df, x, y):
    # Judul Halaman Aplikasi
    st.title("Halaman Prediksi Jenis Tanaman Iris")

    col1, col2 = st.columns(2)

    with col1:
        SepalLengthCm = st.text_input('Input Panjang Sepal (dalam cm) : ')
    with col1:
        SepalWidthCm = st.text_input('Input Lebar Sepal (dalam cm) : ')
    with col2:
        PetalLengthCm = st.text_input('Input Panjang Petal (dalam cm) : ')
    with col2:
        PetalWidthCm = st.text_input('Input Lebar Petal (dalam cm) : ')
    
    features = [SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]
    
    tipe_model = {
        "KNN": predict_KNN,
        "NBC" : predict_NBC,
    }
    
    predict = st.radio(label="Pilih Model ",options=["KNN","NBC"])

    #Tombol Prediksi
    if st.button("Prediksi"):
        if predict == "KNN":
            prediction, score = predict_KNN(x,y,features) # type: ignore
            score = score
            st.info("TERMASUK JENIS BUNGA")

            if(prediction == "Iris-setosa"):
                st.success("Iris jenis Setosa")
                st.image("https://i.etsystatic.com/20845839/r/il/86ac74/3108398608/il_fullxfull.3108398608_6l57.jpg", caption="Iris-setosa", use_column_width=True)
                st.write("Iris setosa memiliki ciri khas berupa petal (kelopak bunga) yang kecil dan pendek dengan ukuran panjang petal sekitar 1,0–1,9 cm dan lebar 0,1–0,6 cm. Sepalnya (daun pelindung) relatif panjang dibandingkan petalnya.")
            elif prediction == "Iris-versicolor":
                st.success("Termasuk kedalam Iris jenis Versicolor")
                st.image("https://www.latour-marliac.com/3033-large_default/iris-versicolor-iris-versicolore.jpg", caption="Iris-versicolor", use_column_width=True)
                st.write("Iris versicolor memiliki petal berukuran sedang, dengan panjang sekitar 3,0–5,1 cm dan lebar 1,0–1,8 cm. Warnanya cenderung ungu kebiruan dengan corak yang khas, dan biasanya tumbuh di tanah yang sedikit lebih kering dibandingkan habitat Iris setosa. Spesies ini memiliki petal berbentuk elips yang lebih lebar dibandingkan Iris setosa.")
            elif prediction == "Iris-virginica":
                st.success("Termasuk kedalam Iris jenis Virginica")
                st.image("https://daylily-phlox.eu/wp-content/uploads/2023/10/Iris-virginica-Pond-Crown-Point.jpg", caption="Iris-virginica", use_column_width=True)
                st.write("Iris virginica adalah spesies dengan petal paling besar dan lebar di antara ketiganya, dengan panjang petal mencapai 4,5–6,9 cm dan lebar 1,2–2,5 cm. Warnanya bervariasi dari biru keunguan hingga ungu pekat, dengan ujung petal yang sedikit melengkung.")

            st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")
        # elif predict == "DT":
        #     prediction, score = predict_DT(x,y,features) # type: ignore
        #     score = score
        #     st.info("Prediksi Sukses....")

        #     if(prediction == "Iris-setosa"):
        #         st.success("Termasuk kedalam Iris jenis Setosa")
        #     elif(prediction == "Iris-versicolor"):
        #         st.success("Termasuk kedalam Iris jenis Versi Color")
        #     elif(prediction == "Iris-virginica"):
        #         st.success("Termasuk kedalam Iris jenis Virginica")

        #     st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")
        else:
            prediction, score = predict_NBC(x,y,features) # type: ignore
            score = score
            st.info("Prediksi Sukses....")

            if(prediction == "Iris-setosa"):
                st.success("Iris jenis Setosa")
                st.image("https://i.etsystatic.com/20845839/r/il/86ac74/3108398608/il_fullxfull.3108398608_6l57.jpg", caption="Iris-setosa", use_column_width=True)
                st.write("Iris setosa memiliki ciri khas berupa petal (kelopak bunga) yang kecil dan pendek dengan ukuran panjang petal sekitar 1,0–1,9 cm dan lebar 0,1–0,6 cm. Sepalnya (daun pelindung) relatif panjang dibandingkan petalnya.")
            elif prediction == "Iris-versicolor":
                st.success("Termasuk kedalam Iris jenis Versicolor")
                st.image("https://www.latour-marliac.com/3033-large_default/iris-versicolor-iris-versicolore.jpg", caption="Iris-versicolor", use_column_width=True)
                st.write("Iris versicolor memiliki petal berukuran sedang, dengan panjang sekitar 3,0–5,1 cm dan lebar 1,0–1,8 cm. Warnanya cenderung ungu kebiruan dengan corak yang khas, dan biasanya tumbuh di tanah yang sedikit lebih kering dibandingkan habitat Iris setosa. Spesies ini memiliki petal berbentuk elips yang lebih lebar dibandingkan Iris setosa.")
            elif prediction == "Iris-virginica":
                st.success("Termasuk kedalam Iris jenis Virginica")
                st.image("https://daylily-phlox.eu/wp-content/uploads/2023/10/Iris-virginica-Pond-Crown-Point.jpg", caption="Iris-virginica", use_column_width=True)
                st.write("Iris virginica adalah spesies dengan petal paling besar dan lebar di antara ketiganya, dengan panjang petal mencapai 4,5–6,9 cm dan lebar 1,2–2,5 cm. Warnanya bervariasi dari biru keunguan hingga ungu pekat, dengan ujung petal yang sedikit melengkung.")

                st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")
