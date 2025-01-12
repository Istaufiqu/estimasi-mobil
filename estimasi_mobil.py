import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# Mengatur input kosong secara default
year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=2025, step=1, value=0)
mileage = st.number_input('Input Km Mobil', min_value=0, step=1, value=0)
tax = st.number_input('Input Pajak Mobil', min_value=0, step=1, value=0)
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0, step=1, value=0)
engineSize = st.number_input('Input Engine Size', min_value=0, step=1, value=0)

predict = ''

# Validasi input: jika ada input yang kosong (masih bernilai 0), tampilkan pesan peringatan
if st.button('Estimasi Harga'):
    if year == 0 or mileage == 0 or tax == 0 or mpg == 0 or engineSize == 0:
        st.warning('Harap isi semua input terlebih dahulu!')
    else:
        # Pastikan data yang diberikan dalam format array 2D
        input_data = [[year, mileage, tax, mpg, engineSize]]
        
        # Melakukan prediksi harga mobil bekas
        predict = model.predict(input_data)
        
        # Mengambil hasil prediksi yang berupa array dan mengakses nilai pertama
        harga_pounds = predict[0]  # Model return array, kita butuh nilai pertama
        
        # Tampilkan hasil estimasi harga dalam Pounds dan IDR
        st.write(f'Estimasi harga mobil bekas dalam Pounds: {harga_pounds}')
        st.write(f'Estimasi harga mobil bekas dalam IDR (Juta): {harga_pounds * 19000}')
