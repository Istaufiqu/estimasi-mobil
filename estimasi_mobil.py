import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# Mengatur input kosong secara default
year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=2025, step=1, format="%d", value=0)
mileage = st.number_input('Input Km Mobil', min_value=0, step=1, format="%d", value=0)
tax = st.number_input('Input Pajak Mobil', min_value=0, step=1, format="%d", value=0)
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0, step=1, format="%d", value=0)
engineSize = st.number_input('Input Engine Size', min_value=0, step=1, format="%d", value=0)

predict = ''

# Validasi input: jika ada input yang kosong (masih bernilai 0), tampilkan pesan peringatan
if st.button('Estimasi Harga'):
    if year == 0 or mileage == 0 or tax == 0 or mpg == 0 or engineSize == 0:
        st.warning('Harap isi semua input terlebih dahulu!')
    else:
        predict = model.predict([[year, mileage, tax, mpg, engineSize]])
        st.write('Estimasi harga mobil bekas dalam Pounds:', predict)
        st.write('Estimasi harga mobil bekas dalam IDR (Juta):', predict * 19000)
