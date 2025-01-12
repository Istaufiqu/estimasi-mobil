import pickle
import streamlit as st
import numpy as np

# Memuat model yang sudah disimpan
try:
    model = pickle.load(open('estimasi_mobil.sav', 'rb'))
except Exception as e:
    st.error(f'Error saat memuat model: {e}')
    st.stop()

st.title('Estimasi Harga Mobil Bekas')

# Input data: Mengubah tipe input menjadi bilangan bulat (integer)
year = st.number_input('Input Tahun Mobil', min_value=0, max_value=2025, step=1, format="%d") 
mileage = st.number_input('Input Km Mobil', min_value=0, step=1, format="%d")
tax = st.number_input('Input Pajak Mobil', min_value=0, step=1, format="%d")
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0, step=1, format="%d")
engineSize = st.number_input('Input Engine Size', min_value=0, step=1, format="%d")

# Menginisialisasi variabel prediksi
predict = ''

# Tombol untuk estimasi harga
if st.button('Estimasi Harga'):
    # Validasi: pastikan semua input lebih dari 0
    if year == 0 or mileage == 0 or tax == 0 or mpg == 0 or engineSize == 0:
        st.warning('Harap isi semua input terlebih dahulu!')
    else:
        try:
            # Memastikan input berupa array 2D yang sesuai dengan model
            input_data = np.array([[year, mileage, tax, mpg, engineSize]])
            
            # Melakukan prediksi
            predict = model.predict(input_data)
            
            # Menampilkan hasil prediksi dalam Pounds dan IDR
            st.write(f'Estimasi harga mobil bekas dalam Pounds: {predict[0]:,.2f}')
            st.write(f'Estimasi harga mobil bekas dalam IDR (Juta): {predict[0] * 19000:,.2f}')
        except Exception as e:
            st.error(f'Error saat melakukan prediksi: {e}')
