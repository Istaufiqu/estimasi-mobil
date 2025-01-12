import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# Mengubah tipe input menjadi bilangan bulat (integer)
year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=2025, step=1, format="%d")
mileage = st.number_input('Input Km Mobil', min_value=0, step=1, format="%d")
tax = st.number_input('Input Pajak Mobil', min_value=0, step=1, format="%d")
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0, step=1, format="%d")
engineSize = st.number_input('Input Engine Size', min_value=0, step=1, format="%d")

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write('Estimasi harga mobil bekas dalam Pounds:', predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta):', predict * 19000)
